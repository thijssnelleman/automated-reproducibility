# Automatic Extraction of Hypothesis: Trajectory-based Algorithm Selection with Warm-starting
*Anja Jankovic, Diederick Vermetten, Ana Kostovska, Jacob de Nobel, Tome Eftimov, Carola Doerr*


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

The authors hypothesise that a trajectory-based algorithm selector, which uses landscape features computed from an initial optimization run to select and warm-start a subsequent algorithm, can outperform any single algorithm from the portfolio in a dynamic, per-run switching context.

The LLM has provided the following reasoning with this hypothesis:

The hypothesis is implied from the Abstract and Introduction. The abstract states the problem of costly feature extraction in traditional landscape-aware algorithm selection and proposes a trajectory-based approach to circumvent this. The authors state: 'In this new context, we show promising performance of the trajectory-based per-run algorithm selection with warm-starting.' (Abstract, p.1). The introduction further elaborates on this, extending a previous approach '[...] to a portfolio of five widely used black-box optimization algorithms, and we consider that we can switch between the algorithms once during the optimization process.' (p.1). The expected outcome is that this selector will be effective, which in the context of algorithm selection means outperforming the single best solver.

Please grade the hypothesis stated from the following options:

The LLM ...

[] captures the hypothesis (nearly) perfectly.

[] has stated a hypothesis capturing the general spirit of our work.

[X] has stated an incomplete hypothesis; the answer is correct but is missing key information.

[] has stated the general hypothesis but has introduced false or incorrect information.

[] has stated a hypothesis similar to ours, but is far too innaccurate to consider correct.

[] has stated a hypothesis that has (nearly) no overlap with our work.

[] has stated a hypothesis of lesser quality than described above: If it is an hallucination, please explain below.



Based on the LLMs answer, would you like to improve the answer to more accurately capture the hypothesis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

The authors hypothesise that a trajectory-based algorithm selector, which uses landscape features computed from an initial optimization run to select and warm-start a subsequent algorithm, can outperform static selection (not only any single algorithm from the portfolio, but even simple selection on top) in a dynamic, per-run switching context.


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
The experiment evaluates a trajectory-based algorithm selection model on a portfolio of five optimization algorithms (BFGS, CMA-ES, DE, MLSL, PSO). An initial algorithm (CMA-ES) runs for 154 function evaluations, during which landscape features are collected. Based on these features, a Random Forest regression model predicts the performance of each of the five algorithms for a subsequent run with a given budget. The algorithm with the best predicted performance is selected and warm-started to continue the optimization. The performance of this algorithm selector is then compared to the performance of each individual algorithm in the portfolio across various budgets for the second part of the search. The evaluation is performed in two scenarios: with the full portfolio, and with a portfolio where the dominant BFGS algorithm is excluded.

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
The measured metrics in this experiment are: R-squared score, Loss (log-performance difference)
Your corrected list (empty if correct): R-squared score, Log distance to the Optimum

#### Statistics
The statistics for the metrics used are: Mean, Distribution (via boxplots showing median and quartiles)
Your corrected list (empty if correct):

#### Strategy and Test
The experiment strategy is summarised as: Leave-one-group-out cross-validation (groups are problem instance IDs 1-5) for training regression models. The optimization runs have a fixed budget, split into an initial 154 evaluations for feature extraction and a subsequent budget for the selected algorithm (tested budgets: {100, 200, 300, 500, 700, 900}).
Your corrected answer (empty if correct): Leave-one-group-out cross-validation (groups are problem instance IDs 1-5) for training regression models. The optimization runs have a fixed budget, split into an initial 150 evaluations for feature extraction and a subsequent budget for the selected algorithm (tested budgets: {100, 200, 300, 500, 700, 900}).

The experiment test is summarised as: Direct comparison of the mean and distribution of the 'Loss' metric between the proposed algorithm selector and the individual algorithms in the portfolio.
Your corrected answer (empty if correct):

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

The results of the experiment are as follows:

{ TODO:
    "BBOB noiseless testbed (COCO environment) Actual Target Precision": {
        "R-squared score": {
            "A2 budget 100": {
                "BFGS": 0.0637,
                "CMAES": 0.5030,
                "DE": 0.1700,
                "MLSL": 0.2410,
                "PSO": 0.5361
            },
            "A2 budget 200": {
                "BFGS": 0.3059,
                "CMAES": 0.1473,
                "DE": 0.2699,
                "MLSL": 0.2066,
                "PSO": 0.5694
            },
            "A2 budget 300": {
                "BFGS": 0.4764,
                "CMAES": 0.0993,
                "DE": 0.1571,
                "MLSL": 0.3142,
                "PSO": 0.5884
            },
            "A2 budget 500": {
                "BFGS": 0.4854,
                "CMAES": 0.2514,
                "DE": 0.1322,
                "MLSL": -0.1059,
                "PSO": 0.3919
            },
            "A2 budget 700": {
                "BFGS": 0.4869,
                "CMAES": 0.2353,
                "DE": 0.0333,
                "MLSL": -0.0641,
                "PSO": 0.1398
            },
            "A2 budget 900": {
                "BFGS": 0.4860,
                "CMAES": 0.1152,
                "DE": -0.0321,
                "MLSL": -0.0279,
                "PSO": -0.8812
            }
    },
    "BBOB noiseless testbed (COCO environment) log-target precision": {
        "R-squared score": {
            "A2 budget 100": {
                "BFGS": 0.7016,
                "CMAES": 0.6708,
                "DE": 0.6721,
                "MLSL": 0.7296,
                "PSO": 0.7205
            },
            "A2 budget 200": {
                "BFGS": 0.6691,
                "CMAES": 0.7006,
                "DE": 0.6549,
                "MLSL": 0.7277,
                "PSO": 0.7017
            },
            "A2 budget 300": {
                "BFGS": 0.7073,
                "CMAES": 0.7695,
                "DE": 0.6324,
                "MLSL": 0.8722,
                "PSO": 0.7980
            },
            "A2 budget 500": {
                "BFGS": 0.7425,
                "CMAES": 0.8423,
                "DE": 0.6109,
                "MLSL": 0.8687,
                "PSO": 0.9128
            },
            "A2 budget 700": {
                "BFGS": 0.7492,
                "CMAES": 0.8053,
                "DE": 0.6194,
                "MLSL": 0.8678,
                "PSO": 0.9137
            },
            "A2 budget 900": {
                "BFGS": 0.7570,
                "CMAES": 0.7894,
                "DE": 0.6669,
                "MLSL": 0.8688,
                "PSO": 0.8745
            }
        },
        "Loss (log-performance difference)": [ TODO: Attempt reading figure 5?
            {
                "comment": "Mean loss for the portfolio excluding BFGS, with an A2 budget of 200 (from text on p.6).",
                "Selector": 0.14,
                "CMA-ES": 0.17
            },
            {
                "comment": "Mean loss for the portfolio excluding BFGS, with an A2 budget of 900 (from text on p.6).",
                "Selector": 0.21,
                "CMA-ES": 0.45
            },
            {
                "comment": "For the full portfolio with A2 budget 100, the selector performs slightly worse than the single best solver, BFGS (from text on p.5)."
            }
        ]
    }
    "Figure 2": {
        "Best-switch": {
            "A2 budget 100": {
                "BFGS": 882,
                "CMAES": 185,
                "DE": 93,
                "PSO": 54,
                "MLSL": 82
            },
            "A2 budget 200": {
                "BFGS": 830,
                "CMAES": 247,
                "DE": 83,
                "PSO": 51,
                "MLSL": 91
            },
            "A2 budget 300": {
                "BFGS": 747,
                "CMAES": 298,
                "DE": 84,
                "PSO": 152,
                "MLSL": 87
            },
            "A2 budget 500": {
                "BFGS": 681,
                "CMAES": 384,
                "DE": 62,
                "PSO": 245,
                "MLSL": 101
            },
            "A2 budget 700": {
                "BFGS": 653,
                "CMAES": 374,
                "DE": 65,
                "PSO": 244,
                "MLSL": 138
            },
            "A2 budget 900": {
                "BFGS": 648,
                "CMAES": 376,
                "DE": 96,
                "PSO": 237,
                "MLSL": 160
            }
        },
        "Select counts": {
            "A2 budget 100": {
                "BFGS": 978,
                "CMAES": 128,
                "DE": 69,
                "PSO": 7,
                "MLSL": 18
            },
            "A2 budget 200": {
                "BFGS": 997,
                "CMAES": 154,
                "DE": 35,
                "PSO": 3,
                "MLSL": 11,
            },
            "A2 budget 300": {
                "BFGS": 878,
                "CMAES": 228,
                "DE": 16,
                "PSO": 68,
                "MLSL": 10
            },
            "A2 budget 500": {
                "BFGS": 765,
                "CMAES": 310,
                "DE": 19,
                "PSO": 67,
                "MLSL": 39
            },
            "A2 budget 700": {
                "BFGS": 699,
                "CMAES": 387,
                "DE": 23,
                "PSO": 45,
                "MLSL": 48
            },
            "A2 budget 900": {
                "BFGS": 667,
                "CMAES": 441,
                "DE": 12,
                "PSO": 44,
                "MLSL": 36
            }
        }
    },
    "Confusion Matrix Table 4": {
        "BFGS": {
            "BFGS": 487,
            "CMA-ES": 44,
            "DE": 1,
            "MLSL": 1,
            "PSO": 2
        },
        "CMA-ES": {
            "BFGS": 48,
            "CMA-ES": 252,
            "DE": 3,
            "MLSL": 4,
            "PSO": 8
        },
        "DE": {
            "BFGS": 11,
            "CMA-ES": 18,
            "DE": 1,
            "MLSL": 3,
            "PSO": 1
        },
        "MLSL": {
            "BFGS": 82,
            "CMA-ES": 66,
            "DE": 2,
            "MLSL": 33,
            "PSO": 4
        },
        "PSO": {
            "BFGS": 33,
            "CMA-ES": 61,
            "DE": 3,
            "MLSL": 0,
            "PSO": 20
        }
    },
    "Select counts w/o BFGS": {
        "A2 budget 100": {
            "CMAES": 577,
            "DE": 435,
            "PSO": 19,
            "MLSL": 169
        },
        "A2 budget 200": {
            "CMAES": 699,
            "DE": 394,
            "PSO": 9,
            "MLSL": 98,
        },
        "A2 budget 300": {
            "CMAES": 754,
            "DE": 295,
            "PSO": 94,
            "MLSL": 57
        },
        "A2 budget 500": {
            "CMAES": 763,
            "DE": 179,
            "PSO": 194,
            "MLSL": 64
        },
        "A2 budget 700": {
            "CMAES": 797,
            "DE": 179,
            "PSO": 146,
            "MLSL": 80
        },
        "A2 budget 900": {
            "CMAES": 864,
            "DE": 137,
            "PSO": 120,
            "MLSL": 79
        }
    },
    "best switch w/o BGFS": {
        "A2 budget 100": {
            "CMAES": 486,
            "DE": 538,
            "PSO": 107,
            "MLSL": 271
        },
        "A2 budget 200": {
            "CMAES": 606,
            "DE": 468,
            "PSO": 74,
            "MLSL": 178,
        },
        "A2 budget 300": {
            "CMAES": 590,
            "DE": 393,
            "PSO": 185,
            "MLSL": 152
        },
        "A2 budget 500": {
            "CMAES": 614,
            "DE": 260,
            "PSO": 345,
            "MLSL": 143
        },
        "A2 budget 700": {
            "CMAES": 629,
            "DE": 240,
            "PSO": 328,
            "MLSL": 172
        },
        "A2 budget 900": {
            "CMAES": 653,
            "DE": 235,
            "PSO": 317,
            "MLSL": 197
        }
    }
}

#### General

The LLM has overall captured the experiment details...

[] Very well (No major mistakes and/or missing information)
[X] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)


### General Experiment Questions

The LLM has provided you with one or more experiments from your work. Is this amount of experiments the same as the amount you specified?

Please write the amount of experiments you had for the study: [1]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Interpretation

Experiment outcomes are analysed and interpreted to determine whether the experiment supports the hypothesis or not. 

The LLM has found the following interpretations of the experiment outcomes;

### interpretation_1

This interpretation has the following description/reasoning:
The authors conclude that the hypothesis is supported, but with the important condition that there must be sufficient performance complementarity among the algorithms in the portfolio. When one algorithm (BFGS) dominates the portfolio, the selector does not provide a benefit and can perform slightly worse (p.5). However, when this dominant algorithm is removed, the performance complementarity increases, and the selector clearly outperforms the remaining individual algorithms. The conclusion states: 'We have shown that the trajectory-based selection is able to outperform all of the individual algorithms in this portfolio, given that there is sufficient complementarity in their performance.' (p.7, Section VI). This is quantitatively supported by the mean loss comparison for the portfolio excluding BFGS, where the selector's mean loss is lower than that of the best single solver in that subset (e.g., 0.21 vs. 0.45 for budget 900, p.6).

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


