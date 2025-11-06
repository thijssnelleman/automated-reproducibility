# Automatic Extraction of Hypothesis: Instance selection for configuration performance comparison
*Marie Anastacio, Théo Matricon, Holger H. Hoos*


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

The authors hypothesise that using intelligent instance selection methods, adapted from algorithm selection and active learning, can significantly reduce the computational time required to accurately compare the performance of two configurations of the same algorithm, compared to the standard random sampling approach used in configurators.

The LLM has provided the following reasoning with this hypothesis:

The hypothesis is implied from the abstract and introduction. The abstract states: '...by running an algorithm on carefully selected instances, the time required to accurately decide the better of two given algorithms can be significantly reduced. In this work, we explore ways to apply a similar selection process to compare two configurations of the same algorithm.' and concludes '...a decision can be reached 5 to 3000 times faster than with random sampling...'. The introduction further states: '...we argue that carefully selecting instances and avoiding long evaluations that provide only a limited amount of information makes it possible to reach a decision faster.' (Page 2). This sets up the expectation that their proposed methods will be faster and more efficient than the baseline (random sampling).

Please grade the hypothesis stated from the following options:

The LLM ...

[] captures the hypothesis (nearly) perfectly.

[] has stated a hypothesis capturing the general spirit of our work.

[] has stated an incomplete hypothesis; the answer is correct but is missing key information.

[X] has stated the general hypothesis but has introduced false or incorrect information.

[] has stated a hypothesis similar to ours, but is far too innaccurate to consider correct.

[] has stated a hypothesis that has (nearly) no overlap with our work.

[] has stated a hypothesis of lesser quality than described above: If it is an hallucination, please explain below.



Based on the LLMs answer, would you like to improve the answer to more accurately capture the hypothesis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

The authors hypothesise that using intelligent instance selection methods, adapted from active learning, can significantly reduce the computational time required to accurately compare the performance of two configurations of the same algorithm, compared to the standard random sampling approach used in configurators.

### General Hypothesis questions

The LLM has provided you with one or more hypothesis from your work. Is this the amount of hypothesis the same as the amount you specified?

Please write the amount of hypothesis you had for the study: [1]

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
This experiment corresponds to 'phase 1' of algorithm configuration. It evaluates how well different selection methods can compare a new 'challenger' configuration to the current 'incumbent' on a set of instances for which the incumbent's performance is already known. The goal is to measure the speed and accuracy of deciding whether to discard the challenger configuration.

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.



#### Hypothesis list
This experiment is used for the following hypotheses: hypothesis_1
Your corrected list (empty if correct):

#### Metrics list
The measured metrics in this experiment are: Area under the curve (AUC) of mean accuracy vs. time
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: The Area Under the Curve (AUC) is computed from the curve of mean accuracy over 10 seeds versus the percentage of total evaluation time.
Your corrected list (empty if correct):

#### Strategy and Test
The experiment strategy is summarised as: The experiment is run for various amounts of prior data: the number of known configurations is in [10, 20, 30, 40, 50] and the proportion of known instances is in [0.1, 0.2, 0.3, 0.4, 0.5] of the full dataset. Results are averaged over 10 seeds.
Your corrected answer (empty if correct):

The experiment test is summarised as: Wilcoxon matched-pairs signed-ranks test (p < 0.05) is used to decide if the challenger configuration can be discarded.
Your corrected answer (empty if correct):

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

The results of the experiment are as follows:

{
    "Kissat-Circuitfuzz (AClib)": {
        "Area under the curve (AUC) of mean accuracy vs. time": "All methods perform well, achieving 90-100% of the total possible AUC across different amounts of prior data."
    },
    "Kissat-IBM (AClib)": {
        "Area under the curve (AUC) of mean accuracy vs. time": "UDD and Uncertainty methods perform poorly (80-85% AUC), especially with less prior data. Random, discrimination, and variance methods perform better (90-95% AUC)."
    },
    "Kissat-crypto (Nejati and Ganesh, 2019)": {
        "Area under the curve (AUC) of mean accuracy vs. time": "All methods perform well, achieving 90-100% of the total possible AUC across different amounts of prior data."
    },
    "Cplex-Regions200 (AClib)": {
        "Area under the curve (AUC) of mean accuracy vs. time": "All methods perform very well, achieving 95-100% of the total possible AUC across different amounts of prior data."
    },
    "Cplex-RCW2 (AClib)": {
        "Area under the curve (AUC) of mean accuracy vs. time": "All methods perform very well, achieving 85-100% of the total possible AUC across different amounts of prior data."
    },
    "Cplex-MIPverify (König et al., 2021)": {
        "Area under the curve (AUC) of mean accuracy vs. time": "All methods perform very well, achieving 85-100% of the total possible AUC across different amounts of prior data."
    }
}

#### General

The LLM has overall captured the experiment details...

[] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[X] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)

### experiment_2

The LLM describes this experiment as follows:
This experiment corresponds to 'phase 2' of algorithm configuration. It evaluates the time needed to distinguish between two similarly performing configurations by running them on new, previously unseen instances. The experiment measures the total running time required by each selection method to select instances until a statistically significant performance difference is found.

The LLM ...
[] has described the experiment (nearly) perfectly
[X] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.



#### Hypothesis list
This experiment is used for the following hypotheses: hypothesis_1
Your corrected list (empty if correct):

#### Metrics list
The measured metrics in this experiment are: Median time (seconds)
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Median time over all tested prior data settings.
Your corrected list (empty if correct):

#### Strategy and Test
The experiment strategy is summarised as: Up to a maximum of 10 new instances are selected and run until the statistical test can distinguish the two configurations.
Your corrected answer (empty if correct):

The experiment test is summarised as: Wilcoxon test (p < 0.05) is used to determine if the two configurations can be told apart.
Your corrected answer (empty if correct):

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

The results of the experiment are as follows:

{
    "Kissat-IBM (AClib)": {
        "Median time (seconds)": {
            "random": 1557,
            "discrimination": 0.086,
            "variance": 0.776,
            "udd": 880.9,
            "uncertainty": 0.033
        }
    },
    "Kissat-cf (AClib)": {
        "Median time (seconds)": {
            "random": 979.7,
            "discrimination": 143.6,
            "variance": 95.16,
            "udd": 393.2,
            "uncertainty": 330.8
        }
    },
    "Kissat-crypto (Nejati and Ganesh, 2019)": {
        "Median time (seconds)": {
            "random": 21243,
            "discrimination": 419.3,
            "variance": 372.2,
            "udd": 13483,
            "uncertainty": 2361.9
        }
    },
    "Cplex-reg200 (AClib)": {
        "Median time (seconds)": {
            "random": 576.8,
            "discrimination": 96.66,
            "variance": 109.5,
            "udd": 379.7,
            "uncertainty": 152.7
        }
    },
    "Cplex-rcw2 (AClib)": {
        "Median time (seconds)": {
            "random": 4138,
            "discrimination": 364.7,
            "variance": 342.0,
            "udd": 1299,
            "uncertainty": 5974
        }
    },
    "Cplex-MIPverify (König et al., 2021)": {
        "Median time (seconds)": {
            "random": 29470,
            "discrimination": 44390,
            "variance": 41365,
            "udd": 28845,
            "uncertainty": 39801
        }
    }
}

#### General

The LLM has overall captured the experiment details...

[X] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)


### General Experiment Questions

The LLM has provided you with one or more experiments from your work. Is this amount of experiments the same as the amount you specified?

Please write the amount of experiments you had for the study: [2]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Interpretation

Experiment outcomes are analysed and interpreted to determine whether the experiment supports the hypothesis or not. 

The LLM has found the following interpretations of the experiment outcomes;

### interpretation_1

This interpretation has the following description/reasoning:
The results for phase 1 show that intelligent selection methods, particularly 'discrimination' and 'variance', generally outperform random sampling. As stated on page 8, 'randomly sampling instances performs well but in most cases the discrimination and variance approaches do better.' The AUC plots in Figure 2 visually confirm that these methods can reach an accurate decision faster (i.e., with less total evaluation time) than the baseline in most scenarios. This supports the hypothesis that intelligent selection is more efficient.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

This interpretation is for the outcome of the following experiment: experiment_1
Your corrected answer (empty if correct):

Answer this question about the (possibly **corrected!**) experiment_id.
This interpretation of the experiment outcome is ...
[] Correct
[X] Almost correct (few and minor misinterpretations or mistakes)
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
The results for phase 2 provide strong evidence for the hypothesis. Table 1 shows that the median time to reach a decision is substantially lower for the 'discrimination' and 'variance' methods compared to random sampling on most datasets. The paper highlights this, stating that 'variance providing a speedup ranging from a 5.8 up to 3000 times speedup for variance compared to random' (Page 11). This directly demonstrates that intelligent instance selection can drastically reduce the computational cost of comparing configurations, thus supporting the hypothesis.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

This interpretation is for the outcome of the following experiment: experiment_2
Your corrected answer (empty if correct):

Answer this question about the (possibly **corrected!**) experiment_id.
This interpretation of the experiment outcome is ...
[] Correct
[X] Almost correct (few and minor misinterpretations or mistakes)
[] Acceptable (some misinterpretations or mistakes)
[] (Partially) Incorrect (serious misinterpretations or mistakes)
[] Incorrect
[] Hallucinatory, if so explain below:



This interpretation is to support (or not) the following hypothesis: hypothesis_1
Your corrected answer (empty if correct):

This interpretation supports the hypothesis: True
Your corrected answer (empty if correct):


