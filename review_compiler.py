"""Compiles the LLM output into a review file."""
from pathlib import Path
import json
import sys

def json_to_markdown_bullets(data, indent=0):
    """
    Convert nested JSON (dict/list) to a nested bullet list in Markdown.

    Args:
        data: The JSON data (dict or list).
        indent: Current indentation level (for recursion).

    Returns:
        str: Markdown bullet list.
    """
    markdown = ""
    if isinstance(data, dict):
        for key, value in data.items():
            markdown += "  " * indent + f"- **{key}**:\n"
            markdown += json_to_markdown_bullets(value, indent + 1)
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, (dict, list)):
                markdown += json_to_markdown_bullets(item, indent)
            else:
                markdown += "  " * indent + f"- {item}\n"
    else:
        markdown += "  " * indent + f"- {data}\n"
    return markdown


general_template = Path("review_template/review_general.md").open().read()
research_question_template = Path("review_template/review_research_question.md").open().read()
hypothesis_template = Path("review_template/review_hypothesis.md").open().read()
experiment_template = Path("review_template/review_experiment.md").open().read()
analysis_template = Path("review_template/review_analysis.md").open().read()
interpretation_template = Path("review_template/review_interpretation.md").open().read()
conclusion_template = Path("review_template/review_conclusion.md").open().read()
future_work_template = Path("review_template/review_future_work.md").open().read()

input_path = Path(sys.argv[1])

if not input_path.exists() or input_path.suffix != ".json":
    print("File does not exist or is not a JSON file.")
    sys.exit(1)

with input_path.open() as json_file:
    llm_output = json.load(json_file)

output_path = Path(f"reviews/{input_path.stem}.md")

research_question_sections, hypothesis_sections, experiment_sections, analysis_sections, interpretation_sections, conclusion_sections, future_work_sections_rq, future_work_sections_h = [], [], [], [], [], [], [], []

paper_title = llm_output["Meta"]["title"]
authors = ", ".join(llm_output["Meta"]["authors"])

general_template = general_template.replace("@@@PAPER_TITLE@@@", paper_title)
general_template = general_template.replace("@@@AUTHORS@@@", authors)

for key in llm_output["Research Questions"]:
    rq_o = research_question_template.replace("@@@RESEARCH_QUESTION_ID@@@", key)
    explicit_type = "explicit" if llm_output["Research Questions"][key]["explicit"] else "implied"
    rq_o = rq_o.replace("@@@RESEARCH_QUESTION_TYPE@@@", explicit_type)
    rq_o = rq_o.replace("@@@RESEARCH_QUESTION_VALUE@@@", llm_output["Research Questions"][key]["value"])
    rq_o = rq_o.replace("@@@RESEARCH_QUESTION_REASON@@@", llm_output["Research Questions"][key]["reason"])
    general_template = general_template.replace("@@@RESEARCH_QUESTIONS@@@", "\n".join([rq_o] + general_template.split("@@@RESEARCH_QUESTIONS@@@")))
    research_question_sections.append(rq_o)

for key in llm_output["Hypotheses"]:
    hypo_o = hypothesis_template.replace("@@@HYPOTHESIS_ID@@@", key)
    explicit_type = "explicit" if llm_output["Hypotheses"][key]["explicit"] else "implied"
    hypo_o = hypo_o.replace("@@@HYPOTHESIS_TYPE@@@", explicit_type)
    hypo_o = hypo_o.replace("@@@RESEARCH_QUESTIONS@@@", ", ".join(llm_output["Hypotheses"][key]["links"]))
    hypo_o = hypo_o.replace("@@@HYPOTHESIS_VALUE@@@", llm_output["Hypotheses"][key]["value"])
    hypo_o = hypo_o.replace("@@@HYPOTHESIS_REASON@@@", llm_output["Hypotheses"][key]["reason"])
    hypothesis_sections.append(hypo_o)

for key in llm_output["Experiments"]:
    exp_o = experiment_template.replace("@@@EXPERIMENT_ID@@@", key)
    exp_o = exp_o.replace("@@@EXPERIMENT_DESCRIPTION@@@", llm_output["Experiments"][key]["experiment_description"])
    exp_o = exp_o.replace("@@@HYPOTHESES_IDS@@@", ", ".join(llm_output["Experiments"][key]["hypotheses"]))
    exp_o = exp_o.replace("@@@RESEARCH_QUESTION_IDS@@@", ", ".join(llm_output["Experiments"][key]["research_questions"]))
    exp_o = exp_o.replace("@@@EXPERIMENT_STRATEGY@@@", llm_output["Experiments"][key]["strategy"])
    exp_o = exp_o.replace("@@@EXPERIMENT_DATA@@@", ", ".join(llm_output["Experiments"][key]["data"]) if isinstance(llm_output["Experiments"][key]["data"], list) else llm_output["Experiments"][key]["data"])
    experiment_sections.append(exp_o)

for key in llm_output["Analyses"]:
    ana_o = analysis_template.replace("@@@ANALYSIS_ID@@@", key)
    ana_o = ana_o.replace("@@@REASON@@@", llm_output["Analyses"][key]["reason"])
    ana_o = ana_o.replace("@@@ANALYSIS_METRICS@@@", ", ".join(llm_output["Analyses"][key]["metrics"]))
    ana_o = ana_o.replace("@@@EXPERIMENT_IDS@@@", ", ".join(llm_output["Analyses"][key]["experiments"]))
    statistics = llm_output["Analyses"][key]["statistics"]
    statistics = ", ".join(statistics) if isinstance(statistics, list) else statistics
    ana_o = ana_o.replace("@@@ANALYSIS_STATISTICS@@@", statistics)
    test = llm_output["Analyses"][key]["test"]
    test = ", ".join(test) if isinstance(test, list) else test
    ana_o = ana_o.replace("@@@ANALYSIS_TEST@@@", test)
    results = json_to_markdown_bullets(llm_output["Analyses"][key]["results"])
    ana_o = ana_o.replace("@@@ANALYSIS_RESULTS_LIST@@@", results)
    analysis_sections.append(ana_o)

for key in llm_output["Interpretations"]:
    int_o = interpretation_template.replace("@@@INTERPRETATION_ID@@@", key)
    int_o = int_o.replace("@@@VALUE@@@", llm_output["Interpretations"][key]["value"])
    int_o = int_o.replace("@@@REASON@@@", llm_output["Interpretations"][key]["reason"])
    analyses_ids = ", ".join(llm_output["Interpretations"][key]["analyses"])
    int_o = int_o.replace("@@@ANALYSES_IDS@@@", analyses_ids)
    interpretation_sections.append(int_o)

for key in llm_output["Conclusions"]:
    con_o = conclusion_template.replace("@@@CONCLUSION_ID@@@", key)
    con_o = con_o.replace("@@@VALUE@@@", llm_output["Conclusions"][key]["value"])
    con_o = con_o.replace("@@@REASON@@@", llm_output["Conclusions"][key]["reason"])
    con_o = con_o.replace("@@@INTERPRETATION_ID@@@", ", ".join(llm_output["Conclusions"][key]["interpretations"]))
    con_o = con_o.replace("@@@RESEARCH_QUESTION_IDS@@@", ", ".join(llm_output["Conclusions"][key]["research_questions"]))
    con_o = con_o.replace("@@@HYPOTHESIS_IDS@@@", ", ".join(llm_output["Conclusions"][key]["hypotheses"]))
    con_o = con_o.replace("@@@SUPPORT@@@", str(llm_output["Conclusions"][key]["support"]))
    conclusion_sections.append(con_o)

# Research questions future_work
for key in llm_output["Future Work"]["Suggested Research Questions"]:
    frq = future_work_template.replace("@@@SUGGESTED_ID@@@", key)
    frq = frq.replace("@@@SUGGESTED_VALUE@@@", llm_output["Future Work"]["Suggested Research Questions"][key]["value"])
    frq = frq.replace("@@@SUGGESTED_TYPE@@@", "research question")
    frq = frq.replace("@@@SUGGESTION_NOTE@@@", llm_output["Future Work"]["Suggested Research Questions"][key]["note"])
    frq = frq.replace("@@@SUGGESTION_REASON@@@", llm_output["Future Work"]["Suggested Research Questions"][key]["note"])
    frq = frq.replace("@@@CONCLUSION_IDS@@@", ", ".join(llm_output["Future Work"]["Suggested Research Questions"][key]["conclusions"]))
    future_work_sections_rq.append(frq)

# Hypothesis future_work
for key in llm_output["Future Work"]["Suggested Hypotheses"]:
    frq = future_work_template.replace("@@@SUGGESTED_ID@@@", key)
    frq = frq.replace("@@@SUGGESTED_VALUE@@@", llm_output["Future Work"]["Suggested Hypotheses"][key]["value"])
    frq = frq.replace("@@@SUGGESTED_TYPE@@@", "hypothesis")
    frq = frq.replace("@@@SUGGESTION_NOTE@@@", llm_output["Future Work"]["Suggested Hypotheses"][key]["note"])
    frq = frq.replace("@@@SUGGESTION_REASON@@@", llm_output["Future Work"]["Suggested Hypotheses"][key]["reason"])
    frq = frq.replace("@@@CONCLUSION_IDS@@@", ", ".join(llm_output["Future Work"]["Suggested Hypotheses"][key]["conclusions"]))
    future_work_sections_h.append(frq)


general_template = general_template.replace("@@@RESEARCH_QUESTION_SECTIONS@@@", "\n".join(research_question_sections))
general_template = general_template.replace("@@@HYPOTHESIS_SECTIONS@@@", "\n".join(hypothesis_sections))
general_template = general_template.replace("@@@EXPERIMENT_SECTIONS@@@", "\n".join(experiment_sections))
general_template = general_template.replace("@@@ANALYSIS_SECTIONS@@@", "\n".join(analysis_sections))
general_template = general_template.replace("@@@INTERPRETATION_SECTIONS@@@", "\n".join(interpretation_sections))    
general_template = general_template.replace("@@@CONCLUSION_SECTIONS@@@", "\n".join(conclusion_sections))
general_template = general_template.replace("@@@SUGGESTED_RQS_SECTIONS@@@", "\n".join(future_work_sections_rq))
general_template = general_template.replace("@@@SUGGESTED_HYPOTHESES_SECTIONS@@@", "\n".join(future_work_sections_h))

with output_path.open("w") as output:
    output.write(general_template)

print("Review created at:", output_path)
