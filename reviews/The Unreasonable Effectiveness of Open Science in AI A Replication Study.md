# Automatic Extraction of Hypothesis: The Unreasonable Effectiveness of Open Science in AI: A Replication Study
*Odd Erik Gundersen, Odd Cappelen, Martin Mølnå, Nicklas Grimstad Nilsen*


You will be presented with the output of an LLM which was tasked to extract the hypothesis from your paper, including the experiment used to test the hypothesis and the interpretation of the outcome of the experiment.

We ask you to **open your PDF** that was presented to the LLM, to reflect upon the LLM's answer with your paper.

The answer of the LLM is structured into three parts; Hypothesis, experiments and interpretation (of experiment outcome).
- For each experiment the LLM has linked it to one or more hypothesis
- For each interpretation, the LLM has linked it to **one** experiment and **one** hypothesis.

The LLM has been tasked to extract a hypothesis **including an expected outcome**. This may not always be the case for each study; it should be interpreted as a post-hoc hypothesis.

Please answer the questions in the  following sections.

## Hypotheses

### hypothesis_1

The LLM has found the following **implied** hypothesis:

The authors hypothesise that sharing both code and data (R4 reproducibility type) leads to a higher rate of successful replication than sharing only data (R3 reproducibility type).

The LLM has provided the following reasoning with this hypothesis:

This hypothesis is central to the paper's thesis. The abstract states: 'The availability of code and data correlate strongly with reproducibility, as 86% of articles that shared code and data were fully or partly reproduced, while this was true for 33% of articles that shared only data.' The introduction further lists as a main contribution: 'Empirically establishing the importance of sharing both code and data to ensure the reproducibility of AI research.' (Page 2).

Please grade the hypothesis stated from the following options:

The LLM ...

[] captures the hypothesis (nearly) perfectly.

[] has stated a hypothesis capturing the general spirit of our work.

[] has stated an incomplete hypothesis; the answer is correct but is missing key information.

[] has stated the general hypothesis but has introduced false or incorrect information.

[] has stated a hypothesis similar to ours, but is far too innaccurate to consider correct.

[] has stated a hypothesis that has (nearly) no overlap with our work.

[] has stated a hypothesis of lesser quality than described above: If it is an hallucination, please explain below.



Based on the LLMs answer, would you like to improve the answer to more accurately capture the hypothesis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.


### hypothesis_2

The LLM has found the following **implied** hypothesis:

The authors hypothesise that poor or inadequate data documentation is a primary cause of irreproducibility in AI research.

The LLM has provided the following reasoning with this hypothesis:

This is presented as a key finding. The abstract claims: 'The quality of the data documentation correlates with successful replication.' The introduction states: 'We also found that the quality of the data documentation has a higher correlation with reproducibility than the quality of the code documentation.' (Page 2). The results section identifies specific data-related problems (P15, P18) as the most significant predictors of failed replications (Page 5).

Please grade the hypothesis stated from the following options:

The LLM ...

[] captures the hypothesis (nearly) perfectly.

[] has stated a hypothesis capturing the general spirit of our work.

[] has stated an incomplete hypothesis; the answer is correct but is missing key information.

[] has stated the general hypothesis but has introduced false or incorrect information.

[] has stated a hypothesis similar to ours, but is far too innaccurate to consider correct.

[] has stated a hypothesis that has (nearly) no overlap with our work.

[] has stated a hypothesis of lesser quality than described above: If it is an hallucination, please explain below.



Based on the LLMs answer, would you like to improve the answer to more accurately capture the hypothesis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.


### hypothesis_3

The LLM has found the following **implied** hypothesis:

The authors hypothesise that the quality of code documentation does not significantly impact the success of a replication attempt, provided that the code itself is shared.

The LLM has provided the following reasoning with this hypothesis:

This is framed as a surprising finding in the paper. The abstract notes: 'Surprisingly, the quality of the code documentation does not correlate with successful replication.' The discussion on page 6 elaborates: 'Problems related to the quality of the documentation of code, whether it is partially missing or not versioned, are not important for successful replication as long as code is shared.'

Please grade the hypothesis stated from the following options:

The LLM ...

[] captures the hypothesis (nearly) perfectly.

[] has stated a hypothesis capturing the general spirit of our work.

[] has stated an incomplete hypothesis; the answer is correct but is missing key information.

[] has stated the general hypothesis but has introduced false or incorrect information.

[] has stated a hypothesis similar to ours, but is far too innaccurate to consider correct.

[] has stated a hypothesis that has (nearly) no overlap with our work.

[] has stated a hypothesis of lesser quality than described above: If it is an hallucination, please explain below.



Based on the LLMs answer, would you like to improve the answer to more accurately capture the hypothesis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.



### General Hypothesis questions

The LLM has provided you with one or more hypothesis from your work. Is this the amount of hypothesis the same as the amount you specified?

Please write the amount of hypothesis you had for the study: []

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Experiments

The LLM has found one or more experiment that were used for the empirical evaluation of your hypotheses. 

In each subsection one of the experiments is listed, with key details that describe it.
For each detail, please correct the LLM if necessary;
- You can leave the correction field empty if no corrections are necessary.
- If any changes are required:
    - [!] Copy the output of the LLM into your answer field
    - If an element is partially incorrect, update it there
    - If an element is wrong, remove it from the list
    - If an element is missing, add it at the end

### experiment_1

The LLM describes this experiment as follows:
A systematic replication study was performed on 30 highly-cited AI papers from 2012, 2014, and 2016. After filtering for empirical studies with available materials and rejecting 8 for practical reasons, the authors attempted to reproduce the results of the remaining 22 papers. Each replication attempt was time-boxed to 40 hours. The papers were categorized by the available materials: R3 (data only) or R4 (code and data). The outcome of each replication was classified, and problems encountered were categorized into 20 types. The correlation between problem types and reproducibility outcomes was analyzed using logistic regression.

The LLM ...
[] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.



#### Hypothesis list
This experiment is used for the following hypotheses: hypothesis_1, hypothesis_2, hypothesis_3
Your corrected list (empty if correct):

#### Metrics list
The measured metrics in this experiment are: Replication Outcome (Success, Partial Success, Failure, No Result), Inclusive Success Rate (Percentage of studies with Success or Partial Success), Logistic Regression Weights (wi), True Positive Rate (TPR) of problem types in irreproducible studies
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Counts and percentages of outcomes, Logistic regression model accuracy and feature weights, True Positive Rate
Your corrected list (empty if correct):

#### Strategy and Test
The experiment strategy is summarised as: Systematic replication of selected published papers, with each replication attempt limited to a maximum of 40 hours of focused work.
Your corrected answer (empty if correct):

The experiment test is summarised as: Comparison of percentages (Inclusive Success Rate) between R3 and R4 groups. Logistic regression was used to identify problem types that significantly predict irreproducibility, with feature significance determined by the magnitude of the weights (|wi|). TPR was used to identify problems characteristic of irreproducible studies.
Your corrected answer (empty if correct):

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

The results of the experiment are as follows:

{
    "R3 studies (N=15)": {
        "Replication Outcome (Success, Partial Success, Failure, No Result)": "1 S, 4 PS, 5 F, 5 NR",
        "Inclusive Success Rate": 0.33
    },
    "R4 studies (N=7)": {
        "Replication Outcome (Success, Partial Success, Failure, No Result)": "5 S, 1 PS, 1 F, 0 NR",
        "Inclusive Success Rate": 0.86
    },
    "Problem Types Analysis (across all 22 studies)": {
        "P15 (Mismatch between dataset specified and version found online)": {
            "Logistic Regression Weights (wi)": -1.0,
            "True Positive Rate (TPR) of problem types in irreproducible studies": 1.0
        },
        "P18 (How dataset is partitioned... is not described)": {
            "Logistic Regression Weights (wi)": -0.82,
            "True Positive Rate (TPR) of problem types in irreproducible studies": 1.0
        },
        "P3 (Poor documentation of code)": {
            "Logistic Regression Weights (wi)": 0.12,
            "True Positive Rate (TPR) of problem types in irreproducible studies": 0.0
        }
    }
}

#### General

The LLM has overall captured the experiment details...

[] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)


### General Experiment Questions

The LLM has provided you with one or more experiments from your work. Is this amount of experiments the same as the amount you specified?

Please write the amount of experiments you had for the study: []

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Interpretation

Experiment outcomes are analysed and interpreted to determine whether the experiment supports the hypothesis or not. 

The LLM has found the following interpretations of the experiment outcomes;

### interpretation_1

This interpretation has the following description/reasoning:
The results strongly support the hypothesis. The Inclusive Success rate for R4 studies (code and data available) was 86%, whereas for R3 studies (only data available) it was only 33%. The authors conclude: 'The main findings is that sharing both code and data increases the chance of reproducing results immensely.' (Page 5).

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

This interpretation is for the outcome of the following experiment: experiment_1
Your corrected answer (empty if correct):

Answer this question about the (possibly **corrected!**) experiment_id.
This interpretation of the experiment outcome is ...
[] Correct
[] Almost correct (few and minor misinterpretations or mistakes)
[] Acceptable (some misinterpretations or mistakes)
[] (Partially) Incorrect (serious misinterpretations or mistakes)
[] Incorrect
[] Hallucinatory, if so explain below:



This interpretation is to support (or not) the following hypothesis: hypothesis_1
Your corrected answer (empty if correct):

This interpretation supports the hypothesis: True
Your corrected answer (empty if correct):

### interpretation_2

This interpretation has the following description/reasoning:
The analysis identified data documentation issues as the strongest predictors of irreproducibility. The authors state that 'problems with documenting the data work are the most important source of irreproducibility' (Page 6). This is based on the logistic regression analysis where problems P15 ('Mismatch between dataset specified and version of it found online') and P18 ('How dataset is partitioned... is not described') were found to be the most significant features predicting failure, and both had a TPR of 1.0, meaning they were only encountered in irreproducible studies (Table 2, Page 4-5).

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

This interpretation is for the outcome of the following experiment: experiment_1
Your corrected answer (empty if correct):

Answer this question about the (possibly **corrected!**) experiment_id.
This interpretation of the experiment outcome is ...
[] Correct
[] Almost correct (few and minor misinterpretations or mistakes)
[] Acceptable (some misinterpretations or mistakes)
[] (Partially) Incorrect (serious misinterpretations or mistakes)
[] Incorrect
[] Hallucinatory, if so explain below:



This interpretation is to support (or not) the following hypothesis: hypothesis_2
Your corrected answer (empty if correct):

This interpretation supports the hypothesis: True
Your corrected answer (empty if correct):

### interpretation_3

This interpretation has the following description/reasoning:
The study's results support this hypothesis. The authors describe it as a 'surprising result' that 'problem types related to code are not indicative of irreproducible research' and that 'Problems related to the quality of the documentation of code... are not important for successful replication as long as code is shared' (Page 6). In the quantitative analysis (Table 2), 'Poor documentation of code' (P3) had a low logistic regression weight (wi=0.12) and a TPR of 0.0, indicating it was not a predictor of failure and was not observed in any of the irreproducible studies.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

This interpretation is for the outcome of the following experiment: experiment_1
Your corrected answer (empty if correct):

Answer this question about the (possibly **corrected!**) experiment_id.
This interpretation of the experiment outcome is ...
[] Correct
[] Almost correct (few and minor misinterpretations or mistakes)
[] Acceptable (some misinterpretations or mistakes)
[] (Partially) Incorrect (serious misinterpretations or mistakes)
[] Incorrect
[] Hallucinatory, if so explain below:



This interpretation is to support (or not) the following hypothesis: hypothesis_3
Your corrected answer (empty if correct):

This interpretation supports the hypothesis: True
Your corrected answer (empty if correct):


