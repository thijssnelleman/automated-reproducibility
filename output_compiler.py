"""Compiles all reviews into a statistical representation."""
from pathlib import Path
import json
import pandas as pd
import re

integer_pattern = r"\[(?P<integer>-?\d+)\]"
x_pattern = r"^\s*\[[xX]\]"


df = []
#df.concat( ["a", "b", "c", "d"])

def process_research_question(lines: list[str], df: list):
    score = None
    rq_id = lines[0].split(" ")[1].strip()
    for line_n, line in enumerate(lines):
        match = re.search(x_pattern, line)
        if match:
            if "captures the research question (nearly) perfectly." in line:
                score = 1
            elif "has stated a research question capturing the general spirit of our work." in line:
                score = 2
            elif "has stated an incomplete research question; the answer is correct but is missing key information." in line:
                score = 3
            elif "has stated the general research question but has introduced false or incorrect information." in line:
                score = 4
            elif "has stated a research question similar to ours, but is far too innaccurate to consider correct." in line:
                score = 5
            elif "has stated a research question that has (nearly) no overlap with our work." in line:
                score = 6
            elif "has stated a research question of lesser quality than described above: " in line:
                score = 7
        if score:
            break
    df.append([review.stem, "Research Question Likert Score", rq_id, score])
    return

def process_hypothesis(lines: list[str], df: list):
    score = None
    hypothesis_id = lines[0].split(" ")[1].strip()
    for _, line in enumerate(lines):
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
        if score:
            break
    if not score:
        raise ValueError(f"No box marked in {hypothesis_id} of {review}")
    df.append([review.stem, "Hypothesis Likert Score", hypothesis_id, score])
    return

def process_experiment(lines: list[str], df: list):
    experiment_id = lines[0].split(" ")[1].strip()
    lines = lines[1:]
    description_score = None
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
        if description_score:
            break

    assert description_score is not None

    df.append([review.stem, "Experiment Description Likert Score", experiment_id, description_score])
    return

def process_analysis(lines: list[str], df: list):
    analysis_id = lines[0].split(" ")[1].strip()
    lines = lines[1:]
    overall_score = None
    for line_idx, line in enumerate(lines):
        match = re.search(x_pattern, line)
        if match:
            if "Very well (No major mistakes and/or missing information)" in line:
                overall_score = 1
            elif "Well (Missing some information and/or minor mistakes)" in line:
                overall_score = 2
            elif "Okay (Missing important information and/or substantial mistakes)" in line:
                overall_score = 3
            elif "Poorly (Missing crucial information and/or severe mistakes)" in line:
                overall_score = 4
            elif "Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)" in line:
                overall_score = 5
        if overall_score:
            break
    assert overall_score is not None
    df.append([review.stem, "Analysis Likert Score", analysis_id, overall_score])
    return

def process_interpretation(lines: list[str], df: list):
    interpretation_id = lines[0].split(" ")[1].strip()
    lines = lines[1:]
    interpretation_score = None
    
    lines = [l for l in lines if l.strip() != ""]
    for _, line in enumerate(lines):
        match = re.search(x_pattern, line)
        line = line.strip().lower()
        if match:
            if "correct" in line:
                interpretation_score = 1
            elif "almost correct" in line:
                interpretation_score = 2
            elif "acceptable" in line:
                interpretation_score = 3
            elif "(partially) incorrect" in line:
                interpretation_score = 4
            elif "incorrect" in line:
                interpretation_score = 5
            elif "hallucinatory" in line:
                interpretation_score = 6
        if interpretation_score:
            break
    df.append([review.stem, "Interpretation Likert Score", interpretation_id, interpretation_score])
    return

def process_conclusion(lines: list[str], df: list):
    conclusion_id = lines[0].split(" ")[1].strip()
    lines = lines[1:]
    conclusion_score = None
    for _, line in enumerate(lines):
        match = re.search(x_pattern, line)
        if match:
            if "Correct" in line:
                conclusion_score = 1
            elif "Almost correct (few and minor misinterpretations or mistakes)" in line:
                conclusion_score = 2
            elif "Acceptable (some misinterpretations or mistakes)" in line:
                conclusion_score = 3
            elif "(Partially) Incorrect (serious misinterpretations or mistakes)" in line:
                conclusion_score = 4
            elif "Incorrect" in line:
                conclusion_score = 5
            elif "Hallucinatory, if so explain below:" in line:
                conclusion_score = 6
        if conclusion_score:
            break
    df.append([review.stem, "Conclusion Likert Score", conclusion_id, conclusion_score])
    return

def process_future_work(lines: list[str], df: list):
    future_work_id = lines[0].split(" ")[1].strip()
    suggested_type = "Hypothesis" if "hypothesis" in future_work_id else "Research Question"
    lines = lines[1:]
    future_work_score = None
    for _, line in enumerate(lines):
        match = re.search(x_pattern, line)
        if match:
            if "The LLM has (nearly) perfectly captured a future research direction suggested by our work." in line:
                future_work_score = 1
            elif "The LLM has stated a future research direction that was implied by our work, but not strongly suggested." in line:
                future_work_score = 2
            elif "The LLM has stated a future research direction from our work that is partially correct." in line:
                future_work_score = 3
            elif "The LLM has stated a future research direction that has some overlap with our work but has introduced incorrect or false information." in line:
                future_work_score = 4
            elif "The LLM has stated a future research direction that was not stated or implied in our work; the LLM has hallucinated this information." in line:
                future_work_score = 5
        if future_work_score:
            break
    df.append([review.stem, f"Suggested {suggested_type} Likert Score", future_work_id, future_work_score])
    return


for review in Path("reviews").glob("*.md"):
    print("Extracting from;", review)
    with review.open() as review_file:
        review_text = review_file.readlines()[18:]  # First 18 lines are description

    while not review_text[0].startswith("##"):
        review_text = review_text[1:]

    title = review.stem
    # 1. Extract all Research Question answers
    if review_text[0].startswith("## Research Questions"):
        review_text = review_text[1:]  # Remove title
        end_index = 0
        for index, line in enumerate(review_text):
            if line.startswith("## Hypotheses"):
                end_index = index
                break
            if line.startswith("### research_question_"):
                process_research_question(review_text[index:], df)
        review_text = review_text[end_index:]

    # 2. Extract all hypothesis answers
    if review_text[0].startswith("## Hypotheses"):
        review_text = review_text[1:]  # Remove title
        end_index = 0
        for index, line in enumerate(review_text):
            if line.startswith("## Experiments"):
                end_index = index
                break
            elif line.startswith("### hypothesis_"):
                process_hypothesis(review_text[index:], df)
        review_text = review_text[end_index:]

    # 3. Extract all experiment answers
    if review_text[0].startswith("## Experiments"):
        review_text = review_text[1:]
        end_index = 0
        for index, line in enumerate(review_text):
            if line.startswith("## Analysis"):
                end_index = index
                break
            elif line.startswith("### experiment_"):
                process_experiment(review_text[index:], df)
        review_text = review_text[end_index:]

    # 4. Extract all analysis answers
    if review_text[0].startswith("## Analysis"):
        review_text = review_text[1:]
        end_index = None
        for index, line in enumerate(review_text):
            if line.startswith("## Interpretation"):
                end_index = index
                break
            elif line.startswith("### analysis_"):
                process_analysis(review_text[index:], df)
        review_text = review_text[end_index:]

    # 5. Extract all interpretation answers
    if review_text[0].startswith("## Interpretation"):
        review_text = review_text[1:]
        end_index = None
        for index, line in enumerate(review_text):
            if line.startswith("## Conclusions"):
                end_index = index
                break
            elif line.startswith("### interpretation_"):
                process_interpretation(review_text[index:], df)
        review_text = review_text[end_index:]

    # 6. Extract all conclusion answers
    if review_text[0].startswith("## Conclusions"):
        review_text = review_text[1:]
        end_index = None
        for index, line in enumerate(review_text):
            if line.startswith("## Future Work"):
                end_index = index
                break
            elif line.startswith("### conclusion_"):
                process_conclusion(review_text[index:], df)
        review_text = review_text[end_index:]

    # 7. Extract all future work answers
    if review_text[0].startswith("## Future Work"):
        review_text = review_text[1:]
        end_index = None
        for index, line in enumerate(review_text):
            if line.startswith("#### suggested"):
                process_future_work(review_text[index:], df)
        review_text = review_text[end_index:]
        
df = pd.DataFrame(columns=["Paper", "section", "field", "value"], data=df)
df.to_csv("output.csv", index=False)
