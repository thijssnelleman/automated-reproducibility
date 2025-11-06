"""Compiles all reviews into a statistical representation."""
from pathlib import Path
import json
import pandas as pd
import re

integer_pattern = r"\[(?P<integer>-?\d+)\]"
x_pattern = r"\[[^\]]*\](\s*([^\s]+)\s*)"

df = pd.DataFrame()

def process_hypothesis(lines: list[str], df: pd.DataFrame):
    score = None
    corrected_hypothesis = None
    hypothesis_id = lines[0].split(" ")[1]
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
                else:
                    raise ValueError(f"No box marked in {hypothesis_id} of {review}")
        
        if line.startswith("- If you consider the answer completely wrong, feel free to rephrase completely in your own wording."):
            corrected_hypothesis = "\n".join([v.strip() for v in lines[line_n+1:] if v.strip() != ""])
            break
    # TODO: add score and corrected hypothesis under the hypothesis id
    #print(score)
    #print(corrected_hypothesis)
    return

def process_experiment(lines: list[str], df: pd.DataFrame):
    experiment_id = lines[0].split(" ")[1]
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
            #print(line)
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
    results_corrected = json.loads("".join(lines[json_start:json_end]))
    # TODO Calculate some stuff over the json
    # TODO add values to df
    return

def process_interpretation(lines: list[str], df: pd.DataFrame):
    interpretation_id = lines[0].split(" ")[1].strip()
    lines = lines[1:]
    interpretation_score = None
    interpretation_corrected = None
    interpretation_hypothesis_corrected = None
    interpretation_experiment_corrected = None
    interpretation_support_corrected = None
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
    # TODO add values to the DF
    print(interpretation_id)
    print(interpretation_score)
    print(interpretation_corrected)
    print(interpretation_hypothesis_corrected)
    print(interpretation_experiment_corrected)
    print(interpretation_support_corrected)
    print(interpretation_hallucination_explanation)
    return


for review in Path("reviews").glob("*.md"):
    print(review)
    with review.open() as review_file:
        review_text = review_file.readlines()[16:]  # First 16 lines are description

    with Path(f"llm_output/{review.stem}.json").open() as llm_output_file:
        llm_output = json.load(llm_output_file)

    title = review.stem
    authors = llm_output["Meta"]["authors"]

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
                #print("HP count:", hp_count)
                # TODO: Add this value to the DF
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
                #print("Exp count:", exp_count)
                # TODO: Add this value to the DF
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
        #print(section_starts)
        for index, section_start in enumerate(section_starts[:-1]):
            #print(review_text[section_start:section_starts[index+1]])
            #input()
            process_interpretation(review_text[section_start:section_starts[index+1]], df)
    break