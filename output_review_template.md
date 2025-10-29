# Automatic Extraction of Hypothesis

You will be presented with the output of an LLM which was tasked to extract the hypothesis from your paper.

The answer is structured into two parts; First the LLM aims to extract the hypothesis from your paper and **formulate it** through paraphrasing or quoting.

Second, the LLM will aim to describe how this hypothesis was tested; Indentify the metrics used, the input data for your method, possible statistical tests or comparisons to test your hypothesis, and under what strategy these values were acquired.

Please answer the following questions:

## Hypothesis

### $HYPOTHESIS_ID$

The LLM states the hypothesis in its answer. Please grade each hypothesis stated from the following options:

The LLM ...

[] captures the hypothesis (nearly) perfectly.

[] has stated an incomplete hypothesis; The answer is correct but is missing key information.

[] has stated the general hypothesis but has introduced false or incorrect information.

[] has stated a hypothesis similar to ours, but is far too innaccurate to consider correct.

[] has stated an hypothesis that has (nearly) no overlap with our work.

[] Other: If it is an hallucination, please explain below.

Based on the LLMs answer, can you improve the answer to more accurately capture the hypothesis?
- If you wish to change nothing, simply state the answer of the LLM
- If you wish to improve the answer, please adapt the original answer
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording

### General questions

The LLM has provided you with one or more hypothesis from your work. Is this the amount of hypothesis the same as the amount you specified?

Please write the amount of hypothesis you had for the study: []

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;

## Experiment

The LLM has found one or more experiment that were used for the empirical evaluation of your hypotheses. 

In each subsection one of the experiments is listed, with key details that describe it.
For each detail, please correct the LLM if necessary;
- You can leave the correction field empty if no corrections are necessary.
- If any changes are required:
    - [!] Copy the output of the LLM into your answer field
    - If an element is partially incorrect, update it there
    - If an element is wrong, remove it from the list
    - If an element is missing, add it at the end

### $EXPERIMENT_ID$

The LLM describes this experiment as follows:
$EXPERIMENT_DESCRIPTION$

The LLM ...
[] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has stated the experiment but has introduced false information or made mistakes
[] has stated the experiment but has nearly no overlap with our work
[] Other. If it has hallucinated, please describe below.



#### Hypothesis list
This experiment is used for the following hypotheses: $LIST_HYPOTHESIS_IDS$
Your corrected list (empty if correct):

#### Metrics list
The measured metrics in this experiment are: $LIST_EXPERIMENT_METRICS$
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: $LIST_EXPERIMENT_STATISTICS$
Your corrected list (empty if correct):

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom.

The results of the experiment are as follows:

$EXPERIMENT_RESULTS_TABLE$

#### General

The LLM has overall captured the experiment details...

[] Very well (No major mistakes and/or missing information)
[] Well (Some missing information and/or minor mistakes)
[] Okay (Substantial missing information and/or mistakes)
[] Poorly (Severe missing information and/or mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)

## Interpretation

Experiment outcomes are analysed and interpreted to determine whether the experiment supports the hypothesis or not. 

The LLM has found the following interpretations of the experiment outcomes;

## $INTERPRETATION_ID$

This interpretation has the following description/reasoning:
$REASON$

This interpretation is for the outcome of the following experiment: $EXPERIMENT_ID$
Your corrected answer (empty if correct):

Answer this question about the (possibly **corrected!**) experiment_id.
This interpretation of the experiment outcome is ...
[] Representative
[] Adequate
[] Acceptable
[] (Partially) Incorrect
[] Incorrect
[] Hallucinatory, if so explain below:



This interpretation is to support (or not) the following hypothesis: $HYPOTHESIS_ID$
Your corrected answer (empty if correct):

This interpretation supports the hypothesis: $SUPPORT$
Your corrected answer (empty if correct):
