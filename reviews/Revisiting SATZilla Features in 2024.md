# Automatic Extraction of Hypothesis: Revisiting SATZilla Features in 2024
*Hadar Shavit, Holger H. Hoos*


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

The authors hypothesise that their new version of the SATZilla feature extraction tool (SATZilla 2024) is more effective than the previous version (SATZilla 2012), specifically that it can extract features from a broader range of instances and that the extracted features lead to improved performance on the downstream tasks of satisfiability prediction, running time prediction, and algorithm selection.

The LLM has provided the following reasoning with this hypothesis:

The abstract (lines 11-20) introduces the new tool and explicitly states the improvements the authors aim to demonstrate: 'We evaluate the extracted features on three downstream tasks: satisfiability prediction, running time prediction, and algorithm selection. We observe that our new tool is able to extract features from a broader range of instances than before. We show that the new version of the feature extractor produces features that achieve up to 26% lower RMSE for running time prediction, up to 3% higher accuracy for satisfiability prediction, and up to 15 times higher closed gap for algorithm selection...'. This serves as a clear, quantifiable claim that the paper sets out to prove empirically, thus forming an implied hypothesis.

Please grade the hypothesis stated from the following options:

The LLM ...

[X] captures the hypothesis (nearly) perfectly.

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
Compares the percentage of SAT instances for which features can be successfully computed within a given time budget by the new tool (SATZilla 2024) versus the old tool (SATZilla 2012). This experiment tests the claim that the new tool can extract features from a broader range of instances.

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
The measured metrics in this experiment are: Percentage of features computed
Your corrected list (empty if correct): Percentage of features computed

#### Statistics
The statistics for the metrics used are: Cumulative plots showing the percentage of instances completed over time.
Your corrected list (empty if correct):

#### Strategy and Test
The experiment strategy is summarised as: Time limit of 180 seconds per feature group.
Your corrected answer (empty if correct): 

The experiment test is summarised as: Visual comparison of the cumulative completion curves. A higher curve indicates better performance.
Your corrected answer (empty if correct):

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

The results of the experiment are as follows:

{
    "2022 SAT Competition formulas": {
        "Percentage of features computed": "Results are presented visually in Figure 1. For most feature groups, the new tool (blue line) computes features for a higher percentage of instances than the old tool (red line) across the time budget."
    },
    "2023 SAT Competition formulas": {
        "Percentage of features computed": "Results are presented visually in Figure 2. For most feature groups, the new tool (blue line) computes features for a higher percentage of instances. For example, for Preliminary features (Figure 2a), the new tool reaches 100% completion while the old tool plateaus below 80%."
    }
}

#### General

The LLM has overall captured the experiment details...

[X] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)

### experiment_2

The LLM describes this experiment as follows:
A random forest classifier is trained to predict the satisfiability of SAT instances using features extracted by the old and new tools. The prediction accuracy is then compared to evaluate the quality of the features for this task.

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
The measured metrics in this experiment are: Accuracy (%)
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Overall accuracy, and accuracy on satisfiable (sat) and unsatisfiable (unsat) instances.
Your corrected list (empty if correct):

#### Strategy and Test
The experiment strategy is summarised as: 10-fold cross-validation for evaluation, with an inner 10-fold cross-validation for hyperparameter optimization using SMAC3.
Your corrected answer (empty if correct):

The experiment test is summarised as: Direct comparison of accuracy scores. Higher is better.
Your corrected answer (empty if correct):

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

The results of the experiment are as follows:

{
    "2022 SAT Competition instances": {
        "Accuracy (%)": {
            "all": {
                "old_tool": 84.0,
                "new_tool": 86.6
            },
            "sat": {
                "old_tool": 82.3,
                "new_tool": 88.0
            },
            "unsat": {
                "old_tool": 85.9,
                "new_tool": 85.1
            }
        }
    },
    "2023 SAT Competition instances": {
        "Accuracy (%)": {
            "all": {
                "old_tool": 91.2,
                "new_tool": 92.5
            },
            "sat": {
                "old_tool": 86.8,
                "new_tool": 89.4
            },
            "unsat": {
                "old_tool": 94.3,
                "new_tool": 94.7
            }
        }
    }
}

#### General

The LLM has overall captured the experiment details...

[] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[X] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)

### experiment_3

The LLM describes this experiment as follows:
A random forest regressor is trained as an Empirical Performance Model (EPM) to predict the running time of SAT solvers. The EPM is trained using features from the old and new tools, and the prediction error is compared.

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
The measured metrics in this experiment are: Root Mean Square Error (RMSE)
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: RMSE on log10-transformed running times for each solver.
Your corrected list (empty if correct):

#### Strategy and Test
The experiment strategy is summarised as: Inner and outer cross-validation. Hyperparameters of the random forest regressor were optimized for one hour using SMAC3.
Your corrected answer (empty if correct):

The experiment test is summarised as: Direct comparison of RMSE scores. Lower is better.
Your corrected answer (empty if correct):

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

The results of the experiment are as follows:

{
    "2022 SAT Competition solvers' running times": {
        "description": "For all 10 best solvers shown in Figure 4a, the RMSE is lower with the new tool's features. For example, for Kissat_MAB-HyWalk, RMSE decreased from 0.77 to 0.68.",
        "Root Mean Square Error (RMSE)": {
            "Kissat_MAB-HyWalk": {
                "new": 0.68,
                "old": 0.77
            },
            "Kissat_MAB_ESA" : {
                "new": 0.72,
                "old": 0.80
            },
            "Kissat_MAB_MOSS": {
                "new": 0.69,
                "old": 0.79
            },
            "Kissat_MAB_UCB": {
                "new": 0.70,
                "old": 0.78
            },
            "ekissat-mab-db-v1": {
                "new": 0.69,
                "old": 0.78
            },
            "ekissat-mab-db-v2": {
                "new": 0.70,
                "old": 0.78
            },
            "ekissat-mab-gb-db": {
                "new": 0.65,
                "old": 0.76
            },
            "kissat-mab-gb": {
                "new": 0.70,
                "old": 0.78
            },
            "kissat_inc": {
                "new": 0.66,
                "old": 0.76
            },
            "kissat_pre": {
                "new": 0.67,
                "old": 0.76
            }
        }

    },
    "2023 SAT Competition solvers' running times": {
        "description": "For all 10 best solvers shown in Figure 4b, the RMSE is lower with the new tool's features. For example, for Kissat_MAB_prop-no_sym, RMSE decreased from 0.93 to 0.72.",
        "Root Mean Square Error (RMSE)": {
            "Kissat_MAB_prop": {
                "new": 0.71,
                "old": 0.89
            },
            "Kissat_MAB_prop-no_sym": {
                "new": 0.72,
                "old": 0.93
            },
            "Kissat_MAB_prop_pr-no_sym": {
                "new": 0.68,
                "old": 0.83
            },
            "MapleCaDiCaL_LBD-990_275": {
                "new": 0.71,
                "old": 0.81
            },
            "MapleCaDiCaL_LBD-990_500": {
                "new": 0.72,
                "old": 0.84
            },
            "MapleCaDiCaL_PPD-500_500": {
                "new": 0.71,
                "old": 0.82
            },
            "MapleCaDiCaL_PPD-950_950": {
                "new": 0.73,
                "old": 0.84
            },
            "PReLearn-kissat-PReLearn-kissat.sh": {
                "new": 0.54,
                "old": 0.66
            },
            "SBVA-sbva_cadical": {
                "new": 0.55,
                "old": 0.74
            },
            "SBVA-sbva_kissat": {
                "new": 0.65,
                "old": 0.78
            }
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

### experiment_4

The LLM describes this experiment as follows:
An algorithm selector (AutoFolio) is configured using features from the old and new tools to select the best solver for each instance from a portfolio of 10 solvers. The performance of the resulting selectors is compared against baselines.

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
The measured metrics in this experiment are: closed gap
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: The closed gap value, which measures the fraction of the performance gap between the single best solver (SBS) and the virtual best solver (VBS) that is closed by the selector.
Your corrected list (empty if correct):

#### Strategy and Test
The experiment strategy is summarised as: AutoFolio was used as the algorithm selector, trained for 8 hours.
Your corrected answer (empty if correct):

The experiment test is summarised as: Direct comparison of closed gap values. Higher is better.
Your corrected answer (empty if correct):

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

The results of the experiment are as follows:

{
    "2022 SAT Competition": {
        "closed gap": {
            "old_tool": 0.01,
            "new_tool": 0.15
        }
    },
    "2023 SAT Competition": {
        "closed gap": {
            "old_tool": 0.53,
            "new_tool": 0.66
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

Please write the amount of experiments you had for the study: [4]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Interpretation

Experiment outcomes are analysed and interpreted to determine whether the experiment supports the hypothesis or not. 

The LLM has found the following interpretations of the experiment outcomes;

### interpretation_1

This interpretation has the following description/reasoning:
The results in Figures 1 and 2 (pages 5-6) demonstrate that the new tool is able to extract features from a broader range of instances than the old tool for most feature groups. The authors state, 'We first observe that the new tool is able to extract more features than the old one for most feature groups.' (lines 197-198). This directly supports the first part of the hypothesis.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

This interpretation is for the outcome of the following experiment: experiment_1
Your corrected answer (empty if correct):

Answer this question about the (possibly **corrected!**) experiment_id.
This interpretation of the experiment outcome is ...
[X] Correct
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
The results in Figure 3 (page 7) show a consistent improvement in satisfiability prediction accuracy when using features from the new tool. The authors conclude, 'We see that, by using features extracted via the new tool, we achieve better performance across all instances on both SAT competitions.' (lines 222-224). This supports the hypothesis regarding the downstream task of satisfiability prediction.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

This interpretation is for the outcome of the following experiment: experiment_2
Your corrected answer (empty if correct):

Answer this question about the (possibly **corrected!**) experiment_id.
This interpretation of the experiment outcome is ...
[X] Correct
[] Almost correct (few and minor misinterpretations or mistakes)
[] Acceptable (some misinterpretations or mistakes)
[] (Partially) Incorrect (serious misinterpretations or mistakes)
[] Incorrect
[] Hallucinatory, if so explain below:



This interpretation is to support (or not) the following hypothesis: hypothesis_1
Your corrected answer (empty if correct):

This interpretation supports the hypothesis: True
Your corrected answer (empty if correct):

### interpretation_3

This interpretation has the following description/reasoning:
The results in Figure 4 (page 8) and the appendix tables show that features from the new tool lead to lower prediction error (RMSE) for running time prediction across all tested solvers. The paper states, 'We see that using the features extracted by the new tool leads to the lower RMSE for all solvers, compared to using those extracted by the old tool.' (lines 249-251). This supports the hypothesis regarding the downstream task of running time prediction.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

This interpretation is for the outcome of the following experiment: experiment_3
Your corrected answer (empty if correct):

Answer this question about the (possibly **corrected!**) experiment_id.
This interpretation of the experiment outcome is ...
[X] Correct
[] Almost correct (few and minor misinterpretations or mistakes)
[] Acceptable (some misinterpretations or mistakes)
[] (Partially) Incorrect (serious misinterpretations or mistakes)
[] Incorrect
[] Hallucinatory, if so explain below:



This interpretation is to support (or not) the following hypothesis: hypothesis_1
Your corrected answer (empty if correct):

This interpretation supports the hypothesis: True
Your corrected answer (empty if correct):

### interpretation_4

This interpretation has the following description/reasoning:
The results in Figure 6 (page 10) show that using features from the new tool leads to a higher closed gap in the algorithm selection task for both competition datasets. The authors state, 'Importantly, features extracted with the new tool lead to better closed gap values on both scenarios.' (lines 274-275). This supports the hypothesis regarding the downstream task of algorithm selection.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

This interpretation is for the outcome of the following experiment: experiment_4
Your corrected answer (empty if correct):

Answer this question about the (possibly **corrected!**) experiment_id.
This interpretation of the experiment outcome is ...
[X] Correct
[] Almost correct (few and minor misinterpretations or mistakes)
[] Acceptable (some misinterpretations or mistakes)
[] (Partially) Incorrect (serious misinterpretations or mistakes)
[] Incorrect
[] Hallucinatory, if so explain below:



This interpretation is to support (or not) the following hypothesis: hypothesis_1
Your corrected answer (empty if correct):

This interpretation supports the hypothesis: True
Your corrected answer (empty if correct):


