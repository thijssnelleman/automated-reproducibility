"""Compiles all reviews into a statistical representation."""
from pathlib import Path
import json
import pandas as pd
import re

integer_pattern = r"\[(?P<integer>-?\d+)\]"
x_pattern = r"^\s*\[[xX]\]"


df = []
#df.concat( ["a", "b", "c", "d"])

def process_hypothesis(lines: list[str], df: list):
    score = None
    corrected_hypothesis = None
    hypothesis_id = lines[0].split(" ")[1].strip()
    for line_n, line in enumerate(lines):
        if not score:
            match = re.search(x_pattern, line)
            if match:
                if "captures the hypothesis (nearly) perfectly." in line:
                    score = 1
                elif "has stated a hypothesis capturing the general spirit of our work." in line:
                    score = 2
                elif "has stated an incomplete hypothesis; the answer is correct but is missing key information." in line:
                    score = 3
                elif "has stated the general hypothesis but has introduced false or incorrect information." in line:
                    score = 4
                elif "has stated a hypothesis similar to ours, but is far too innaccurate to consider correct." in line:
                    score = 5
                elif "has stated a hypothesis that has (nearly) no overlap with our work." in line:
                    score = 6
                elif "has stated a hypothesis of lesser quality than described above: " in line:
                    score = 7
        
        if line.startswith("- If you consider the answer completely wrong, feel free to rephrase completely in your own wording."):
            corrected_hypothesis = "\n".join([v.strip() for v in lines[line_n+1:] if v.strip() != ""])
            break
    if not score:
        raise ValueError(f"No box marked in {hypothesis_id} of {review}")
    df.append([review.stem, hypothesis_id, "Hypothesis Likert Score", score])
    df.append([review.stem, hypothesis_id, "Hypothesis Corrected", corrected_hypothesis])
    return

def process_experiment(lines: list[str], df: list):
    experiment_id = lines[0].split(" ")[1].strip()
    lines = lines[1:]
    description_score = None
    detail_score = None
    description_score_reason = None
    corrected_hypotheses = None
    corrected_metrics = None
    corrected_statistics = None
    corrected_strategy = None
    corrected_test_description = None
    for line_idx, line in enumerate(lines):
        match = re.search(x_pattern, line)
        if match:
            if "has described the experiment (nearly) perfectly" in line:
                description_score = 1
            elif "has described the experiment but is lacking information" in line:
                description_score = 2
            elif "has described the experiment but has introduced false information or made mistakes" in line:
                description_score = 3
            elif "has described an experiment which has nearly no overlap with that found in our work" in line:
                description_score = 4
            elif "Other. If it has hallucinated, please describe below." in line:
                description_score = 5
                description_score_reason = []
                for l in lines[line_idx+1:]:
                    if l.startswith("#"):
                        break
                    elif l.strip() != "":
                        description_score_reason.append(l.strip())
            elif "Very well (No major mistakes and/or missing information)" in line:
                detail_score = 1
            elif "Well (Missing some information and/or minor mistakes)" in line:
                detail_score = 2
            elif "Okay (Missing important information and/or substantial mistakes)" in line:
                detail_score = 3
            elif "Poorly (Missing crucial information and/or severe mistakes)" in line:
                detail_score = 4
            elif "Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)" in line:
                detail_score = 5
        elif line.startswith("Your corrected "):
            if "This experiment is used for the following hypotheses" in lines[line_idx-1]:
                corrected_hypotheses = line.strip("Your corrected list (empty if correct):").strip()
            elif "The measured metrics in this experiment are" in lines[line_idx-1]:
                corrected_metrics = line.strip("Your corrected list (empty if correct):").strip()
            elif "The statistics for the metrics used are" in lines[line_idx-1]:
                corrected_statistics = line.strip("Your corrected list (empty if correct):").strip()
            elif "The experiment strategy is summarised as" in lines[line_idx-1]:
                corrected_strategy = line.strip("Your corrected answer (empty if correct):").strip()
            elif "The experiment test is summarised as" in lines[line_idx-1]:
                corrected_test_description = line.strip("Your corrected answer (empty if correct):").strip()
            else:
                raise ValueError(f"Unclear correction line {experiment_id} of {review}: {line}")
        elif line.startswith("The results of the experiment are as follows:"):
            json_start = line_idx + 1
        elif line.startswith("#### General"):
            json_end = line_idx - 1

    assert description_score is not None
    assert detail_score is not None

    results_original = llm_output["Experiment"][experiment_id]["results"]
    try:
        results_corrected = json.loads("".join(lines[json_start:json_end]))
    except Exception as e:
        print("Error parsing results for experiment", experiment_id, "in", review)
        raise e
    missing, wrong, correct = 0, 0, 0
    
    def get_keys(d, curr_key=[]):
        for k, v in d.items():
            if isinstance(v, dict):
                yield from get_keys(v, curr_key + [k])
            elif isinstance(v, list):
                for i in v:
                    yield from get_keys(i, curr_key + [k])
            else:
                yield '-KEYSEP-'.join(curr_key + [k])

    keys_corrected = set(get_keys(results_corrected))
    keys_original = set(get_keys(results_original))

    for key in keys_corrected:
        if key not in keys_original:
            missing += 1
        else:
            current_left, current_right = results_corrected, results_original
            for subkey in key.split("-KEYSEP-"):
                if not isinstance(current_left, dict) or not isinstance(current_right, dict):
                    break
                current_left = current_left[subkey]
                current_right = current_right[subkey]
            if isinstance(current_left, list) and isinstance(current_right, list):
                for item in current_left:
                    if item not in current_right:
                        missing += 1
                    else:
                        correct += 1
                for item in current_right:
                    if item not in current_left:
                        wrong += 1
            elif current_left != current_right:
                wrong += 1
            else:
                correct += 1

    for key in keys_original:
        if key not in keys_corrected:
            wrong += 1

    df.append([review.stem, experiment_id, "Experiment Description Likert Score", description_score])
    df.append([review.stem, experiment_id, "Experiment Details Likert Score", detail_score])
    df.append([review.stem, experiment_id, "Experiment Description Score Reason", description_score_reason])
    df.append([review.stem, experiment_id, "Experiment Corrected Hypotheses", corrected_hypotheses])
    df.append([review.stem, experiment_id, "Experiment Corrected Metrics", corrected_metrics])
    df.append([review.stem, experiment_id, "Experiment Corrected Statistics", corrected_statistics])
    df.append([review.stem, experiment_id, "Experiment Corrected Strategy", corrected_strategy])
    df.append([review.stem, experiment_id, "Experiment Corrected Test Description", corrected_test_description])
    df.append([review.stem, experiment_id, "Experiment Results Missing", missing])
    df.append([review.stem, experiment_id, "Experiment Results Wrong", wrong])
    df.append([review.stem, experiment_id, "Experiment Results Correct", correct])
    return

def process_interpretation(lines: list[str], df: list):
    interpretation_id = lines[0].split(" ")[1].strip()
    lines = lines[1:]
    interpretation_score = None
    interpretation_corrected = None
    interpretation_hypothesis_corrected = ""
    interpretation_experiment_corrected = ""
    interpretation_support_corrected = ""
    interpretation_hallucination_explanation = None
    lines = [l for l in lines if l.strip() != ""]
    for l_index, line in enumerate(lines):
        match = re.search(x_pattern, line)
        if match:
            if "Correct" in line:
                interpretation_score = 1
            elif "Almost correct" in line:
                interpretation_score = 2
            elif "Acceptable" in line:
                interpretation_score = 3
            elif "(Partially) Incorrect" in line:
                interpretation_score = 4
            elif "Incorrect" in line:
                interpretation_score = 5
            elif "Hallucinatory" in line:
                interpretation_score = 6
                interpretation_hallucination_explanation = []
                for l in lines[lines.index(line)+1:]:
                    if l.startswith("This interpretation is to support (or not)"):
                        break
                    elif l.strip() != "":
                        interpretation_hallucination_explanation.append(l.strip())
        elif line.startswith("- If you consider the answer completely wrong, feel free to rephrase completely in your own wording."):
            interpretation_corrected = []
            for l in lines[lines.index(line)+1:]:
                if l.startswith("This interpretation is for the outcome of the following "):
                    break
                elif l.strip() != "":
                    interpretation_corrected.append(l.strip())
        elif line.startswith("Your corrected answer (empty if correct):"):
            if lines[l_index-1].startswith("This interpretation is for the outcome of the following experiment"):
                interpretation_experiment_corrected = line.split(":", maxsplit=1)[1].strip()
            elif lines[l_index-1].startswith("This interpretation is to support (or not) the following hypothesis:"):
                interpretation_hypothesis_corrected = line.strip("Your corrected answer (empty if correct):").strip()
            elif lines[l_index-1].startswith("This interpretation supports the hypothesis"):
                interpretation_support_corrected = line.strip("Your corrected answer (empty if correct):").strip()
            else:
                raise ValueError(f"Unclear correction line {interpretation_id} of {review}: {l_index}, {lines[l_index-1]}, {line}")
    df.append([review.stem, interpretation_id, "Interpretation Likert Score", interpretation_score])
    df.append([review.stem, interpretation_id, "Interpretation Corrected", "\n".join(interpretation_corrected)])
    df.append([review.stem, interpretation_id, "Interpretation Corrected Hypotheses", interpretation_hypothesis_corrected])
    df.append([review.stem, interpretation_id, "Interpretation Corrected Experiments", interpretation_experiment_corrected])
    df.append([review.stem, interpretation_id, "Interpretation Corrected Support", interpretation_support_corrected])
    df.append([review.stem, interpretation_id, "Interpretation Hallucination Explanation", interpretation_hallucination_explanation])
    return


for review in Path("reviews").glob("*.md"):
    print(review)
    with review.open() as review_file:
        review_text = review_file.readlines()[16:]  # First 16 lines are description

    with Path(f"llm_output/{review.stem}.json").open() as llm_output_file:
        llm_output = json.load(llm_output_file)

    title = review.stem
    authors = llm_output["Meta"]["authors"]

    # Add LLM responses
    for hypothesis_id in llm_output["Hypothesis"]:
        df.append([review.stem, hypothesis_id, "Hypothesis", llm_output["Hypothesis"][hypothesis_id]["hypothesis"]])
        df.append([review.stem, hypothesis_id, "Explicit", llm_output["Hypothesis"][hypothesis_id]["explicit"]])

    for experiment_id in llm_output["Experiment"]:
        df.append([review.stem, experiment_id, "Hypotheses", llm_output["Experiment"][experiment_id]["hypothesis"]])
        df.append([review.stem, experiment_id, "Metrics", llm_output["Experiment"][experiment_id]["metrics"]])
        df.append([review.stem, experiment_id, "Statistics", llm_output["Experiment"][experiment_id]["statistics"]])
        df.append([review.stem, experiment_id, "Strategy", llm_output["Experiment"][experiment_id]["strategy"]])
        df.append([review.stem, experiment_id, "Test", llm_output["Experiment"][experiment_id]["test"]])

    for interpretation_id in llm_output["Interpretation"]:
        df.append([review.stem, interpretation_id, "Interpretation", llm_output["Interpretation"][interpretation_id]["reason"]])
        df.append([review.stem, interpretation_id, "Support", llm_output["Interpretation"][interpretation_id]["support"]])
        df.append([review.stem, interpretation_id, "Hypothesis", llm_output["Interpretation"][interpretation_id]["hypothesis"]])
        df.append([review.stem, interpretation_id, "Experiment", llm_output["Interpretation"][interpretation_id]["experiment"]])

    # 1. Extract all hypothesis answers
    if review_text[0].startswith("## Hypotheses"):
        review_text = review_text[1:]  # Remove title
        general_section_index = None
        end_index = None
        section_starts = []
        for index, line in enumerate(review_text):
            if line.startswith("#"):
                if line.startswith("### General Hypothesis questions"):
                    section_starts.append(index)
                    general_section_index = index
                elif line.startswith("### hypothesis_"):
                    section_starts.append(index)
                else:
                    end_index = index
                    break
        for index, section_start in enumerate(section_starts[:-1]):
            process_hypothesis(review_text[section_start:section_starts[index+1]], df)
        
        # Process General Hypothesis section
        reasoning = False
        
        for index, line in enumerate(review_text[general_section_index:end_index]):
            if line.startswith("Please write the amount of hypothesis you had for the study:"):
                match = re.search(integer_pattern, line)
                hp_count = int(match.group(1))
                if hp_count > len(llm_output["Hypothesis"]):
                    for i in range(len(llm_output["Hypothesis"]), hp_count):
                        df.append([review.stem, f"hypothesis_{i+1}", "Hypothesis Likert Score", 8])
            if line.startswith("If this amount does not overlap with the LLMs answer, feel free to specify reasons below;"):
                reasoning = True
            if reasoning:
                reasoning = review_text[general_section_index+index:end_index]
                break
        # TODO: Add the reasoning to the dataset?
        review_text = review_text[end_index:]
    
    # 2. Extract all experiment answers
    if review_text[0].startswith("## Experiments"):
        review_text = review_text[1:]
        general_section_index = None
        end_index = None
        section_starts = []
        for index, line in enumerate(review_text):
            if line.startswith("#"):
                if line.startswith("### General Experiment Questions"):
                    section_starts.append(index)
                    general_section_index = index
                elif line.startswith("### experiment_"):
                    section_starts.append(index)
                elif line.startswith("## "):
                    end_index = index
                    break

        for index, section_start in enumerate(section_starts[:-1]):
            process_experiment(review_text[section_start:section_starts[index+1]], df)
    
        # Process general experiment section
        reason = False
        for index, line in enumerate(review_text[general_section_index:end_index]):
            if line.startswith("Please write the amount of experiments you had for the study"):
                match = re.search(integer_pattern, line)
                exp_count = int(match.group(1))
                # The following papers would seperate experiments, but do not think experiments are missing (See reason in the review)
                excluded_papers = ["Robustness Distributions in Neural Network Verification",
                                   "Combining Automated Optimisation of Hyperparameters and Reward Shape",
                                   "Hyperparameters in Reinforcement Learning and How To Tune Them",
                                   "Growing with Experience- Growing Neural Networks in Deep Reinforcement Learning",
                                   ]
                if exp_count > len(llm_output["Experiment"]) and review.stem not in excluded_papers:
                    for i in range(len(llm_output["Experiment"]), exp_count):
                        df.append([review.stem, f"experiment_{i+1}", "Experiment Description Likert Score", 6])
            if line.startswith("If this amount does not overlap with the LLMs answer, feel free to specify reasons below;"):
                reason = True
            if reason:
                reason = review_text[general_section_index+index:end_index]
                break
        # TODO: Add the reason to the dataset?
        review_text = review_text[end_index:]
    
    # 3. Extract all interpretation answers
    if review_text[0].startswith("## Interpretation"):
        review_text = review_text[1:]
        general_section_index = None
        end_index = None
        section_starts = []
        for index, line in enumerate(review_text):
            if line.startswith("### interpretation_"):
                section_starts.append(index)
        section_starts.append(len(review_text)-1)
        for index, section_start in enumerate(section_starts[:-1]):
            process_interpretation(review_text[section_start:section_starts[index+1]], df)
    #break

df = pd.DataFrame(columns=["Paper", "section", "field", "value"], data=df)
df.to_csv("output.csv", index=False)
print(df)