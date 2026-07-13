import json
import os
import argparse
from graphviz import Digraph


def get_node_label(key, data, section="", max_chars=90, for_mermaid=False):
    """Creates a label for a node, wrapping the text."""
    if section == "Experiments":
        label = data.get("experiment_description", data.get("value", key))
    elif section == "Analyses":
        label = data.get("reason", data.get("value", key))
    elif section == "Interpretations":
        label = data.get("value", key)
    else:
        label = data.get("value", key)

    # Truncate the label in the middle if it's too long
    if len(label) > max_chars:
        part_len = (max_chars - 5) // 2  # approx length of each part
        
        # Find a good place to cut the first part
        start_cut = label.rfind(' ', 0, part_len)
        if start_cut == -1: start_cut = part_len  # fallback if no space is found
        start_text = label[:start_cut]

        # Find a good place to start the second part
        end_cut = label.find(' ', len(label) - part_len)
        if end_cut == -1: end_cut = len(label) - part_len  # fallback if no space is found
        end_text = label[end_cut+1:]

        label = start_text + " [...] " + end_text

    if not for_mermaid:
        # Escape HTML characters for Graphviz
        label = label.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    # Add word wrapping for better visualization
    words = label.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 > 30:
            lines.append(current_line)
            current_line = word
        else:
            if current_line:
                current_line += " " + word
            else:
                current_line = word
    if current_line:
        lines.append(current_line)

    if for_mermaid:
        # Use Markdown and HTML for Mermaid labels to increase title font size
        bold_key = f'<b><font size="5">{key}</font></b>'
        wrapped_label = "<br>".join(lines)
        return f'"{bold_key}<br>{wrapped_label}"'
    else:
        # Use HTML-like labels for Graphviz formatting
        bold_key = f'<B><FONT POINT-SIZE="16">{key}</FONT></B>'
        wrapped_label = "<BR/>".join(lines)
        return f'<{bold_key}<BR/>{wrapped_label}>'


def visualize_paper_structure(json_path, output_dir, output_format='mmd'):
    """
    Reads a JSON file representing a paper's structure and creates a
    graph visualization.

    Args:
        json_path (str): The path to the input JSON file.
        output_dir (str): The directory to save the output graph.
        output_format (str): The output format ('png' or 'mmd').
    """
    try:
        with open(json_path, 'r') as f:
            paper_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading or parsing {json_path}: {e}")
        return

    # --- Mermaid Specific Setup ---
    mermaid_lines = [
        "graph LR;",
        "    %% Styles",
        "    classDef default fill:#F5F5F5,stroke:#333,stroke-width:1px,rx:5,ry:5;",
        "    classDef hypothesis fill:#F8CECC,stroke:#333,stroke-width:1px,rx:5,ry:5;",
        "    classDef future_work fill:#DAE8FC,stroke:#333,stroke-width:1px,rx:5,ry:5;",
        "",
        "    %% Nodes"
    ]
    node_definitions = []
    edge_definitions = []

    # --- Graphviz Specific Setup ---
    dot = Digraph(comment=paper_data.get("Meta", {}).get("title", "Paper Structure"))
    dot.attr(rankdir='LR', splines='true', overlap='false', nodesep='0.5')


    # Define colors for different node types
    colors = {
        "Research Questions": "#F5F5F5",  # Soft Gray
        "Hypotheses": "#F8CECC",         # Soft Red
        "Experiments": "#F5F5F5",        # Soft Gray
        "Analyses": "#F5F5F5",           # Soft Gray
        "Interpretations": "#F5F5F5",    # Soft Gray
        "Conclusions": "#F5F5F5",        # Soft Gray
        "Future Work": "#DAE8FC"          # Soft Blue
    }

    nodes = {}

    # Group nodes by section to enforce rank
    nodes_by_section = {
        "Research Questions": [],
        "Hypotheses": [],
        "Experiments": [],
        "Analyses": [],
        "Interpretations": [],
        "Conclusions": [],
        "Future Work": []
    }
    # 1. Add all nodes to the graph
    for section, section_data in paper_data.items():
        if isinstance(section_data, dict):
            color = colors.get(section, "white")
            for key, data in section_data.items():
                if isinstance(data, dict):
                    # Handle nested sections like Future Work
                    if section == "Future Work" and key in ["Suggested Research Questions", "Suggested Hypotheses"]:
                         for sub_key, sub_data in data.items():
                             if isinstance(sub_data, dict):
                                  node_id = f"{section}_{sub_key}"
                                  nodes[sub_key] = node_id
                                  if output_format == 'mmd':
                                      label = get_node_label(sub_key, sub_data, section, for_mermaid=True)
                                      node_definitions.append(f"    {node_id}[{label}]")
                                  else:
                                      label = get_node_label(sub_key, sub_data, section, for_mermaid=False)
                                      dot.node(node_id, label, style='filled,rounded', fillcolor=color, shape='box')
                                  if section in nodes_by_section:
                                      nodes_by_section[section].append(node_id)
                    else:
                        node_id = f"{section}_{key}"
                        nodes[key] = node_id
                        if output_format == 'mmd':
                            label = get_node_label(key, data, section, for_mermaid=True)
                            node_definitions.append(f"    {node_id}[{label}]")
                        else:
                            label = get_node_label(key, data, section, for_mermaid=False)
                            dot.node(node_id, label, style='filled,rounded', fillcolor=color, shape='box')
                        if section in nodes_by_section:
                            nodes_by_section[section].append(node_id)

    if output_format == 'mmd':
        mermaid_lines.extend(sorted(node_definitions))
    # 2. Add rank constraints to align nodes of the same type
    for section, node_ids in nodes_by_section.items():
        if node_ids:
            if output_format == 'mmd':
                mermaid_lines.append(f"\n    subgraph {section}")
                for node_id in node_ids:
                    mermaid_lines.append(f"        {node_id}")
                mermaid_lines.append("    end")
            else:
                with dot.subgraph() as s:
                    s.attr(rank='same')
                    for node_id in node_ids:
                        s.node(node_id)

    # 3. Add edges based on relationships
    for section, section_data in paper_data.items():
        if not isinstance(section_data, dict):
            continue

        for key, data in section_data.items():
            if not isinstance(data, dict):
                continue

            if section == "Future Work" and key in ["Suggested Research Questions", "Suggested Hypotheses"]:
                for sub_key, sub_data in data.items(): # sub_key is 'suggested_research_question_1'
                    if isinstance(sub_data, dict):
                        source_node_id = nodes.get(sub_key)
                        if source_node_id:
                            for link_type, target_keys in sub_data.items():
                                if isinstance(target_keys, list): # e.g., "is_based_on": ["conclusion_1"]
                                    for target_key in target_keys:
                                        target_node_id = nodes.get(target_key)
                                        if target_node_id:
                                            if output_format == 'mmd':
                                                edge_definitions.append(f"    {target_node_id} --> {source_node_id}")
                                            else:
                                                dot.edge(target_node_id, source_node_id)
                # After handling Future Work's unique structure, skip to the next item in the section
                continue

            source_node_id = nodes.get(key)
            if not source_node_id:
                continue
            
            # Handle regular node linking
            for link_type, target_keys in data.items():
                if isinstance(target_keys, list):
                    for target_key in target_keys:
                        target_node_id = nodes.get(target_key)
                        if source_node_id and target_node_id:
                            # Determine the source and target for the edge
                            # By default, the edge goes from the dependency (target_key) to the dependent (key)
                            # e.g., RQ -> Hypo, Hypo -> Exp
                            from_node, to_node = target_node_id, source_node_id

                            # Edges generally go from dependency to dependent
                            # e.g., RQ -> Hypo, Hypo -> Exp, etc.
                            # User requested to reverse edges for conclusions.
                            # print(section, link_type)
                            if section == "Conclusions" and link_type in ["research_questions", "hypotheses"]:
                                from_node, to_node = source_node_id, target_node_id

                            if output_format == 'mmd':
                                edge_definitions.append(f"    {from_node} --> {to_node}")
                            else:
                                dot.edge(from_node, to_node)

    # Save the output
    base_name = os.path.splitext(os.path.basename(json_path))[0]
    
    if output_format == 'mmd':
        mermaid_lines.append("\n    %% Edges")
        mermaid_lines.extend(sorted(edge_definitions))

        # Add styling classes to nodes
        mermaid_lines.append("\n    %% Styling")
        for section, node_ids in nodes_by_section.items():
            if section == "Hypotheses":
                style_class = "hypothesis"
            elif section == "Future Work":
                style_class = "future_work"
            else:
                style_class = "default"
            for node_id in node_ids:
                mermaid_lines.append(f"    class {node_id} {style_class}")

        output_path = os.path.join(output_dir, f"{base_name}.mmd")
        try:
            with open(output_path, 'w') as f:
                f.write("\n".join(mermaid_lines))
            print(f"Successfully generated Mermaid code for {base_name} at {output_path}")
        except Exception as e:
            print(f"Error writing Mermaid file for {json_path}: {e}")
    else: # 'png'
        output_path = os.path.join(output_dir, base_name)
        try:
            dot.render(output_path, format='png', view=False, cleanup=True)
            print(f"Successfully generated graph for {base_name} at {output_path}.png")
        except Exception as e:
            print(f"Error rendering graph for {json_path}: {e}")
            print("Please ensure Graphviz is installed and in your system's PATH.")


def main():
    """
    Main function to parse arguments and process JSON files.
    """
    parser = argparse.ArgumentParser(
        description="Visualize the structure of research papers from JSON files."
    )
    parser.add_argument(
        "--input_dir",
        type=str,
        default="ground_truth",
        help="Directory containing the JSON files (e.g., 'ground_truth')."
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="ground_truth/visualizations",
        help="Directory to save the output graph images."
    )
    parser.add_argument(
        "--format",
        type=str,
        default="mmd",
        choices=['mmd', 'png'],
        help="Output format: 'mmd' for Mermaid code or 'png' for an image."
    )
    args = parser.parse_args()

    if not os.path.isdir(args.input_dir):
        print(f"Error: Input directory '{args.input_dir}' not found.")
        return

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    for filename in os.listdir(args.input_dir):
        if filename.endswith(".json"):
            json_path = os.path.join(args.input_dir, filename)
            visualize_paper_structure(json_path, args.output_dir, args.format)


if __name__ == "__main__":
    main()