# Automatic Extraction of Hypothesis: Combining Automated Optimisation of Hyperparameters and Reward Shape
*Julian Dierkes, Emma Cramer, Holger H. Hoos, Sebastian Trimpe*


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

The authors hypothesise that the combined, simultaneous optimisation of an RL algorithm's hyperparameters and its reward function parameters will match or outperform the individual optimisation of either component alone, especially in complex environments.

The LLM has provided the following reasoning with this hypothesis:

The hypothesis is implied in the Abstract and Introduction. The Abstract states: "We demonstrate empirically that an RL algorithm's hyperparameter configurations and reward function are often mutually dependent, meaning neither can be fully optimised without appropriate values for the other. We then propose a methodology for the combined optimisation of hyperparameters and the reward function." The expected outcome is also in the Abstract: "Our results show that combined optimisation significantly improves over baseline performance in half of the environments and achieves competitive performance in the others... This suggests that combined optimisation should be best practice." Contribution 1 on page 2 further clarifies this: "We show that combined optimisation can match the performance of individual optimisation with the same compute budget despite the larger search space; furthermore, we show that it can yield significant improvement in challenging environments, such as Humanoid and Wipe."

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


### hypothesis_2

The LLM has found the following **implied** hypothesis:

The authors hypothesise that including a variance penalty in the optimisation objective (multi-objective optimisation) will improve the stability (i.e., reduce the performance variance) of the learned policies, while achieving similar or better expected performance compared to single-objective optimisation.

The LLM has provided the following reasoning with this hypothesis:

This hypothesis is stated in the Abstract: "Furthermore, we include a variance penalty as an optimisation objective to improve the stability of learned policies." It is also listed as the second key contribution on page 2: "We demonstrate that including a variance penalty for multi-objective optimisation can obtain hyperparameter settings and reward shapes that substantially improve performance variance of a trained policy while achieving similar or better expected performance."

Please grade the hypothesis stated from the following options:

The LLM ...

[] captures the hypothesis (nearly) perfectly.

[X] has stated a hypothesis capturing the general spirit of our work.

[] has stated an incomplete hypothesis; the answer is correct but is missing key information.

[] has stated the general hypothesis but has introduced false or incorrect information.

[] has stated a hypothesis similar to ours, but is far too innaccurate to consider correct.

[] has stated a hypothesis that has (nearly) no overlap with our work.

[] has stated a hypothesis of lesser quality than described above: If it is an hallucination, please explain below.



Based on the LLMs answer, would you like to improve the answer to more accurately capture the hypothesis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

The authors hypothesise that including a variance penalty in the optimisation objective (multi-objective optimisation) of the simultaneous optimisation will improve the stability (i.e., reduce the performance variance) of the learned policies, while achieving similar or better expected performance compared to single-objective optimisation.

### General Hypothesis questions

The LLM has provided you with one or more hypothesis from your work. Is this the amount of hypothesis the same as the amount you specified?

Please write the amount of hypothesis you had for the study: [2]

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
The authors compare the performance of combined hyperparameter and reward shape optimisation against several baselines: a default baseline configuration, optimising only hyperparameters, and optimising only reward parameters. This comparison is performed for two RL algorithms (PPO and SAC) across four different environments. The evaluation is conducted for both a single-objective performance metric and a multi-objective metric that includes a variance penalty.

The LLM ...
[] has described the experiment (nearly) perfectly
[X] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.



#### Hypothesis list
This experiment is used for the following hypotheses: hypothesis_1, hypothesis_2
Your corrected list (empty if correct):

#### Metrics list
The measured metrics in this experiment are: Task Performance, Coefficient of Variation
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Median performance and median coefficient of variation. Each experiment consists of five optimisation runs, and the incumbent from each run is evaluated over ten training runs. The final reported value is the median of the five median performances.
Your corrected list (empty if correct):

#### Strategy and Test
The experiment strategy is summarised as: Optimisation is performed using DEHB over a budget of 133 (PPO) or 80 (SAC) full training runs. Each optimisation experiment is conducted with 5 random seeds. The final incumbent configuration from each is evaluated by training with 10 additional random seeds.
Your corrected answer (empty if correct):

The experiment test is summarised as: Linear mixed-effects model analysis (significance level = 0.05)
Your corrected answer (empty if correct): Linear mixed-effects model analysis (significance level = 0.05) between the pooled 50 training runs of each optimisation's seed's incumbent for different optimisation experiments

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

The results of the experiment are as follows:

{
    "Gymnasium LunarLander": {
        "base": {
            "PPO": {
                "Task Performance": 273,
                "Coefficient of Variance": "11%"
            },
            "SAC": {
                "Task Performance": 208,
                "Coefficient of Variance": "27%"
            }
        },
        "base_DEHB": {
            "PPO": {
                "Single Obj.": {
                    "Task Performance": 287,
                    "Coefficient of Variance": "31%"
                },
                "Multi Obj.": {
                    "Task Performance": 223,
                    "Coefficient of Variance": "10%"
                }
            },
            "SAC": {
                "Single Obj.": {
                    "Task Performance": 175,
                    "Coefficient of Variance":  "14%"
                },
                "Multi Obj.": {
                    "Task Performance": 174,
                    "Coefficient of Variance": "13%"
                }
            }
        },
        "DEHB_base": {
            "PPO": {
                "Single Obj.": {
                    "Task Performance": 265,
                    "Coefficient of Variance": "27%"
                },
                "Multi Obj.": {
                    "Task Performance": 277,
                    "Coefficient of Variance": "11%"
                }
            },
            "SAC": {
                "Single Obj.": {
                    "Task Performance": 194,
                    "Coefficient of Variance": "23%"
                },
                "Multi Obj.": {
                    "Task Performance": 186,
                    "Coefficient of Variance": "15%"
                }
            }
        },
        "DEHB_RS": {
            "PPO": {
                "Single Obj.": {
                    "Task Performance": 262,
                    "Coefficient of Variance": "38%"
                },
                "Multi Obj.": {
                    "Task Performance": 252,
                    "Coefficient of Variance": "24%"
                }
            },
            "SAC": {
                "Single Obj.": {
                    "Task Performance": 171,
                    "Coefficient of Variance": "15%"
                },
                "Multi Obj.": {
                    "Task Performance": 193,
                    "Coefficient of Variance": "18%"
                }
            }
        },
        "DEHB (Ours)": {
            "PPO": {
                "Single Obj.": {
                    "Task Performance": 234,
                    "Coefficient of Variance": "25%" 
                },
                "Multi Obj.": {
                    "Task Performance": 227,
                    "Coefficient of Variance": "15%"
                }
            },
            "SAC": {
                "Single Obj.": {
                    "Task Performance": 177,
                    "Coefficient of Variance": "23%" 
                },
                "Multi Obj.": {
                    "Task Performance": 182,
                    "Coefficient of Variance": "21%"
                }
            }
        }           
    },
    "Google Brax Ant": {
        "base": {
            "PPO": {
                "Task Performance": 6785,
                "Coefficient of Variance": "16%"
            },
            "SAC": {
                "Task Performance": 8054,
                "Coefficient of Variance": "28%"
            }
        },
        "base_DEHB": {
            "PPO": {
                "Single Obj.": {
                    "Task Performance": 6706,
                    "Coefficient of Variance": "17%"
                },
                "Multi Obj.": {
                    "Task Performance": 6663,
                    "Coefficient of Variance": "14%"
                }
            },
            "SAC": {
                "Single Obj.": {
                    "Task Performance": 7927,
                    "Coefficient of Variance": "32%"
                },
                "Multi Obj.": {
                    "Task Performance": 7994,
                    "Coefficient of Variance": "29%"
                }
            }
        },
        "DEHB_base": {
            "PPO": {
                "Single Obj.": {
                    "Task Performance": 8111,
                    "Coefficient of Variance": "14%"
                },
                "Multi Obj.": {
                    "Task Performance": 7842,
                    "Coefficient of Variance": "6%"
                }
            },
            "SAC": {
                "Single Obj.": {
                    "Task Performance": 8282,
                    "Coefficient of Variance": "21%"
                },
                "Multi Obj.": {
                    "Task Performance": 8216,
                    "Coefficient of Variance": "13%"
                }
            }
        },
        "DEHB_RS": {
            "PPO": {
                "Single Obj.": {
                    "Task Performance": 8013,
                    "Coefficient of Variance": "16%"
                }
            },
            "SAC": {
                "Single Obj.": {
                    "Task Performance": 8064,
                    "Coefficient of Variance": "21%"
                }
            }
        },
        "DEHB (Ours)": {
            "PPO": {
                "Single Obj.": {
                    "Task Performance": 8049,
                    "Coefficient of Variance": "12%"
                },
                "Multi Obj.": {
                    "Task Performance": 7923,
                    "Coefficient of Variance": "6%"
                }
            },
            "SAC": {
                "Single Obj.": {
                    "Task Performance": 8199,
                    "Coefficient of Variance": "23%"
                },
                "Multi Obj.": {
                    "Task Performance": 8169,
                    "Coefficient of Variance": "18%"
                }
            }
        }           
    },
    "Google Brax Humanoid": {
        "base": {
            "PPO": {
                "Task Performance": 4196,
                "Coefficient of Variance": "<1%"
            },
            "SAC": {
                "Task Performance": 3273,
                "Coefficient of Variance": "11%"
            }
        },
        "base_DEHB": {
            "PPO": {
                "Single Obj.": {
                    "Task Performance": 4464,
                    "Coefficient of Variance": "<1%" 
                },
                "Multi Obj.": {
                    "Task Performance": 4472,
                    "Coefficient of Variance": "<1%"
                }
            },
            "SAC": {
                "Single Obj.": {
                    "Task Performance": 5284,
                    "Coefficient of Variance": "11%"
                },
                "Multi Obj.": {
                    "Task Performance": 5208,
                    "Coefficient of Variance": "8%"
                }
            }
        },
        "DEHB_base": {
            "PPO": {
                "Single Obj.": {
                    "Task Performance": 4826,
                    "Coefficient of Variance": "1%"
                },
                "Multi Obj.": {
                    "Task Performance": 4719,
                    "Coefficient of Variance": "<1%"
                }
            },
            "SAC": {
                "Single Obj.": {
                    "Task Performance": 4881,
                    "Coefficient of Variance": "18%"
                },
                "Multi Obj.": {
                    "Task Performance": 4466,
                    "Coefficient of Variance": "15%"
                }
            }
        },
        "DEHB_RS": {
            "PPO": {
                "Single Obj.": {
                    "Task Performance": 5112,
                    "Coefficient of Variance": "2%"
                }
            },
            "SAC": {
                "Single Obj.": {
                    "Task Performance": 5913,
                    "Coefficient of Variance": "17%"
                }
            }
        },
        "DEHB (Ours)": {
            "PPO": {
                "Single Obj.": {
                    "Task Performance": 5433,
                    "Coefficient of Variance": "7%"
                },
                "Multi Obj.": {
                    "Task Performance": 5485,
                    "Coefficient of Variance": "1%"
                }
            },
            "SAC": {
                "Single Obj.": {
                    "Task Performance": 6033,
                    "Coefficient of Variance": "12%"
                },
                "Multi Obj.": {
                    "Task Performance": 6103,
                    "Coefficient of Variance": "1%"
                }
            }
        }
    },
    "Robosuite Wipe": {
        "base": {
            "SAC": {
                "Task Performance": 101,
                "Coefficient of Variance": "24%"
            }
        },
        "base_DEHB": {
            "SAC": {
                "Single Obj.": {
                    "Task Performance": 108,
                    "Coefficient of Variance": "24%"
                },
                "Multi Obj.": {
                    "Task Performance": 114,
                    "Coefficient of Variance": "20%"
                }
            }
        },
        "DEHB_base": {
            "SAC": {
                "Single Obj.": {
                    "Task Performance": 132,
                    "Coefficient of Variance": "10%"
                },
                "Multi Obj.": {
                    "Task Performance": 131,
                    "Coefficient of Variance": "11%"
                }
            }
        },
        "DEHB_RS": {
            "SAC": {
                "Single Obj.": {
                    "Task Performance": 134,
                    "Coefficient of Variance": "10%"
                }
            }
        },
        "DEHB (Ours)": {
            "SAC": {
                "Single Obj.": {
                    "Task Performance": 136,
                    "Coefficient of Variance": "8%"
                },
                "Multi Obj.": {
                    "Task Performance": 130,
                    "Coefficient of Variance": "10%"
                }
            }
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

Please write the amount of experiments you had for the study: [3]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;
I would seperate the experiment into three parts:
- Landscape analysis
- Single objective optimisation experiments
- Multi objective optimisation experiments


## Interpretation

Experiment outcomes are analysed and interpreted to determine whether the experiment supports the hypothesis or not. 

The LLM has found the following interpretations of the experiment outcomes;

### interpretation_1

This interpretation has the following description/reasoning:
The results in Table 1 support the hypothesis. The authors state in Section 5.2: "Our results show that simultaneously optimising hyperparameters and reward parameters consistently matches or outperforms individual optimisation... Significant performance gains are observed in the complex Humanoid and Wipe environments, while the simpler Ant and LunarLander environments, which are mostly solved using baseline parameter settings, generally show no additional improvements from joint optimisation." For example, in the complex Humanoid environment with PPO, the combined optimisation (5433) significantly outperforms both reward-only (4464) and hyperparameter-only (4826) optimisation. Similarly, for SAC on Wipe, combined optimisation (136) outperforms the individual approaches (108 and 132). The authors conclude that even when performance only matches, "joint optimisation still offers the advantage of not requiring hand-tuning, while addressing the mutual dependencies of hyperparameter and reward parameters."

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
The results in Table 1 support the hypothesis. The authors state in Section 5.3: "From Table 1, we conclude that multi-objective optimisation can improve policy stability by including a penalty for large standard deviation in performance. These improvements come with only marginal performance loss and sometimes even achieve slight gains". For instance, in the Google Brax Ant environment with SAC, the multi-objective hyperparameter-only optimisation achieves a much lower Coefficient of Variation (13%) compared to its single-objective counterpart (21%) while achieving comparable task performance (8216 vs 8282). Similarly, for Humanoid with SAC, the combined multi-objective optimisation achieves a CV of 1% versus 12% for the single-objective version, with a slight performance increase (6103 vs 6033). This demonstrates that the variance penalty successfully improves policy stability.

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



This interpretation is to support (or not) the following hypothesis: hypothesis_2
Your corrected answer (empty if correct):

This interpretation supports the hypothesis: True
Your corrected answer (empty if correct):


