# Automatic Extraction of Hypothesis: Dynamic Algorithm Termination for Branch-and-Bound-based Neural Network Verification
*Konstantin Kaulen, Matthias König, Holger H. Hoos*


You will be presented with the output of an LLM which was tasked to extract the hypothesis from your paper, including the experiment used to test the hypothesis and the interpretation of the outcome of the experiment.

We ask you to **open your PDF** that was presented to the LLM, to reflect upon the LLM's answer with your paper.

The answer of the LLM is structured into three parts; Hypothesis, experiments and interpretation (of experiment outcome).
- For each experiment the LLM has linked it to one or more hypothesis
- For each interpretation, the LLM has linked it to **one** experiment and **one** hypothesis.

The LLM has been tasked to extract a hypothesis **including an expected outcome**. This may not always be the case for each study; it should be interpreted as a post-hoc hypothesis.

Please answer the following questions:

## Hypotheses

### hypothesis_1

The LLM has found the following **implied** hypothesis:

The authors hypothesise that by using a dynamic prediction model based on static and dynamic instance features to terminate Branch-and-Bound-based neural network verification runs early, it is possible to significantly reduce the total computational running time while maintaining a comparable number of successfully verified instances compared to the standard verification procedure.

The LLM has provided the following reasoning with this hypothesis:

The abstract states, "Overall, using our method, we were able to reduce the total running time by 64% on average compared to the standard verification procedure, while certifying a comparable number of instances." (Page 1, Abstract). The introduction further elaborates on this goal: "...we can reliably terminate verification runs for instances that are unsolvable within a given cutoff time without solving considerably fewer instances overall." (Page 1, Introduction). This implies the hypothesis that their proposed method successfully achieves this trade-off between computational savings and the number of solved instances.

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
The authors evaluate their dynamic termination method against the standard verification procedure on a wide range of benchmarks and three state-of-the-art Branch-and-Bound-based verifiers (αβ-CROWN, VeriNet, Oval). The performance is compared based on the total running time required and the total number of verification instances solved. The performance of the underlying classification model is also evaluated.

The LLM ...
[] has described the experiment (nearly) perfectly
[X] has described the experiment but is lacking information
[] has stated the experiment but has introduced false information or made mistakes
[] has stated the experiment but has nearly no overlap with our work
[] Other. If it has hallucinated, please describe below.



#### Hypothesis list
This experiment is used for the following hypotheses: hypothesis_1
Your corrected list (empty if correct):

#### Metrics list
The measured metrics in this experiment are: Total running time (GPU hours), Number of solved instances, Accuracy, True Positive Rate (TPR), False Positive Rate (FPR)
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Accumulated values over 5 folds for running time and number of solved instances. The difference in solved instances compared to the baseline is also reported. For classification metrics, averages over five folds are reported.
Your corrected list (empty if correct):

#### Strategy and Test
The experiment strategy is summarised as: 5-fold cross-validation. The method is configured with a per-instance timeout (t_cutoff) of 600s, a prediction frequency (t_freq) of 10s, and a confidence threshold (θ) of 0.99.
Your corrected answer (empty if correct):

The experiment test is summarised as: Direct comparison of the total running time and the number of solved instances between the proposed method and the standard verification procedure.
Your corrected answer (empty if correct):

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom.

The results of the experiment are as follows:

{
    "Dynamic Termination Performance": {
        "αβ-CROWN": {
            "5 100": {
                "Total running time (GPU hours)": "21.97 (70%)",
                "Number of solved instances": "868 (±0)"
            },
            "8 100": {
                "Total running time (GPU hours)": "17.86 (43%)",
                "Number of solved instances": "766 (-1)"
            },
            "Conv Big": {
                "Total running time (GPU hours)": "1.01 (68%)",
                "Number of solved instances": "918 (±0)"
            },
            "Conv Small": {
                "Total running time (GPU hours)": "1.00 (80%)",
                "Number of solved instances": "969 (-10)"
            },
            "ResNet 2B": {
                "Total running time (GPU hours)": "4.30 (28%)",
                "Number of solved instances": "619 (±0)"
            },
            "Marabou": {
                "Total running time (GPU hours)": "2.47 (5%)",
                "Number of solved instances": "192 (-1)"
            },
            "Oval21": {
                "Total running time (GPU hours)": "7.57 (15%)",
                "Number of solved instances": "207 (-3)"
            },
            "ViT": {
                "Total running time (GPU hours)": "1.94 (5%)",
                "Number of solved instances": "251 (±0)"
            },
            "SRI ResNet A": {
                "Total running time (GPU hours)": "3.86 (7%)",
                "Number of solved instances": "197 (-1)"
            },
            "CIFAR-100": {
                "Total running time (GPU hours)": "4.91 (20%)",
                "Number of solved instances": "360 (-1)"
            },
            "Tiny ImageNet": {
                "Total running time (GPU hours)": "4.54 (31%)",
                "Number of solved instances": "421 (±0)"
            }
        },
        "VeriNet": {
            "5 100": {
                "Total running time (GPU hours)": "18.81 (28%)",
                "Number of solved instances": "576 (-4)"
            },
            "8 100": {
                "Total running time (GPU hours)": "16.75 (22%)",
                "Number of solved instances": "500 (-1)"
            },
            "Conv Big": {
                "Total running time (GPU hours)": "5.48 (49%)",
                "Number of solved instances": "868 (±0)"
            },
            "Conv Small": {
                "Total running time (GPU hours)": "11.30 (94%)",
                "Number of solved instances": "931 (±0)"
            },
            "ResNet 2B": {
                "Total running time (GPU hours)": "10.45 (46%)",
                "Number of solved instances": "576 (±0)"
            },
            "Marabou": {
                "Total running time (GPU hours)": "6.36 (12%)",
                "Number of solved instances": "168 (-8)"
            },
            "Oval21": {
                "Total running time (GPU hours)": "15.04 (26%)",
                "Number of solved instances": "155 (-3)"
            },
            "SRI ResNet A": {
                "Total running time (GPU hours)": "8.71 (14%)",
                "Number of solved instances": "133 (±0)"
            },
            "CIFAR-100": {
                "Total running time (GPU hours)": "19.52 (49%)",
                "Number of solved instances": "279 (±0)"
            },
            "Tiny ImageNet": {
                "Total running time (GPU hours)": "19.4 (66%)",
                "Number of solved instances": "354 (-2)"
            }
        },
        "Oval": {
            "5 100": {
                "Total running time (GPU hours)": "7.88 (9%)",
                "Number of solved instances": "430 (±0)"
            },
            "8 100": {
                "Total running time (GPU hours)": "3.57 (4%)",
                "Number of solved instances": "386 (-1)"
            },
            "Conv Big": {
                "Total running time (GPU hours)": "6.36 (41%)",
                "Number of solved instances": "841 (-1)"
            },
            "Conv Small": {
                "Total running time (GPU hours)": "6.08 (100%)",
                "Number of solved instances": "958 (±0)"
            },
            "Marabou": {
                "Total running time (GPU hours)": "4.97 (9%)",
                "Number of solved instances": "185 (-2)"
            },
            "Oval21": {
                "Total running time (GPU hours)": "10.02 (19%)",
                "Number of solved instances": "199 (-2)"
            }
        }
    },
    "Classifier Performance": {
        "αβ-CROWN": {
            "5 100": {
                "Accuracy": 0.99,
                "True Positive Rate (TPR)": 0.95,
                "False Positive Rate (FPR)": 0.0
            },
            "8 100": {
                "Accuracy": 0.99,
                "True Positive Rate (TPR)": 0.99,
                "False Positive Rate (FPR)": 0.0
            },
            "Conv Big": {
                "Accuracy": 0.47,
                "True Positive Rate (TPR)": 0.43,
                "False Positive Rate (FPR)": 0.0
            },
            "Conv Small": {
                "Accuracy": 0.82,
                "True Positive Rate (TPR)": 1.0,
                "False Positive Rate (FPR)": 0.2
            },
            "ResNet 2B": {
                "Accuracy": 0.98,
                "True Positive Rate (TPR)": 0.98,
                "False Positive Rate (FPR)": 0.0
            },
            "Marabou": {
                "Accuracy": 0.99,
                "True Positive Rate (TPR)": 0.99,
                "False Positive Rate (FPR)": 0.1
            },
            "Oval21": {
                "Accuracy": 0.97,
                "True Positive Rate (TPR)": 0.98,
                "False Positive Rate (FPR)": 0.05
            },
            "ViT": {
                "Accuracy": 0.99,
                "True Positive Rate (TPR)": 0.98,
                "False Positive Rate (FPR)": 0.0
            },
            "SRI ResNet A": {
                "Accuracy": 0.99,
                "True Positive Rate (TPR)": 1.0,
                "False Positive Rate (FPR)": 0.02
            },
            "CIFAR-100": {
                "Accuracy": 0.99,
                "True Positive Rate (TPR)": 0.99,
                "False Positive Rate (FPR)": 0.02
            },
            "Tiny ImageNet": {
                "Accuracy": 0.99,
                "True Positive Rate (TPR)": 0.99,
                "False Positive Rate (FPR)": 0.0
            }
        },
        "VeriNet": {
            "5 100": {
                "Accuracy": 0.89,
                "True Positive Rate (TPR)": 0.87,
                "False Positive Rate (FPR)": 0.04
            },
            "8 100": {
                "Accuracy": 0.92,
                "True Positive Rate (TPR)": 0.91,
                "False Positive Rate (FPR)": 0.02
            },
            "Conv Big": {
                "Accuracy": 0.88,
                "True Positive Rate (TPR)": 0.74,
                "False Positive Rate (FPR)": 0.0
            },
            "Conv Small": {
                "Accuracy": 0.81,
                "True Positive Rate (TPR)": 0.39,
                "False Positive Rate (FPR)": 0.0
            },
            "ResNet 2B": {
                "Accuracy": 0.77,
                "True Positive Rate (TPR)": 0.71,
                "False Positive Rate (FPR)": 0.0
            },
            "Marabou": {
                "Accuracy": 0.93,
                "True Positive Rate (TPR)": 0.95,
                "False Positive Rate (FPR)": 0.53
            },
            "Oval21": {
                "Accuracy": 0.89,
                "True Positive Rate (TPR)": 0.88,
                "False Positive Rate (FPR)": 0.07
            },
            "SRI ResNet A": {
                "Accuracy": 0.91,
                "True Positive Rate (TPR)": 0.9,
                "False Positive Rate (FPR)": 0.0
            },
            "CIFAR-100": {
                "Accuracy": 0.86,
                "True Positive Rate (TPR)": 0.78,
                "False Positive Rate (FPR)": 0.0
            },
            "Tiny ImageNet": {
                "Accuracy": 0.9,
                "True Positive Rate (TPR)": 0.69,
                "False Positive Rate (FPR)": 0.01
            }
        },
        "Oval": {
            "5 100": {
                "Accuracy": 0.97,
                "True Positive Rate (TPR)": 0.96,
                "False Positive Rate (FPR)": 0.0
            },
            "8 100": {
                "Accuracy": 0.99,
                "True Positive Rate (TPR)": 0.99,
                "False Positive Rate (FPR)": 0.07
            },
            "Conv Big": {
                "Accuracy": 0.78,
                "True Positive Rate (TPR)": 0.75,
                "False Positive Rate (FPR)": 0.05
            },
            "Conv Small": {
                "Accuracy": 0.79,
                "True Positive Rate (TPR)": 0.09,
                "False Positive Rate (FPR)": 0.0
            },
            "Marabou": {
                "Accuracy": 0.96,
                "True Positive Rate (TPR)": 0.96,
                "False Positive Rate (FPR)": 0.13
            },
            "Oval21": {
                "Accuracy": 0.96,
                "True Positive Rate (TPR)": 0.95,
                "False Positive Rate (FPR)": 0.03
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


### General Experiment Questions

The LLM has provided you with one or more experiments from your work. Is this amount of experiments the same as the amount you specified?

Please write the amount of experiments you had for the study: []

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Interpretation

Experiment outcomes are analysed and interpreted to determine whether the experiment supports the hypothesis or not. 

The LLM has found the following interpretations of the experiment outcomes;

## interpretation_1

This interpretation has the following description/reasoning:
The authors conclude that their method successfully accelerates neural network verification. They state in the conclusion: "we showed that our method accelerates the verification procedure by 64% on average compared to the current state-of-the-art approach across a diverse set of benchmarks from the verification literature, while certifying a comparable number of instances." (Page 7, Conclusions and Future Work). The results presented in Table 3 strongly support this claim, showing substantial reductions in running time (e.g., up to 95% saved on the Marabou benchmark for αβ-CROWN) while incurring a minimal loss of solved instances (often 0 or just a few instances lost per benchmark). This directly supports both clauses of the hypothesis. The authors note some cases where performance is weaker (e.g., higher FPR for Marabou on VeriNet), but the overall results are overwhelmingly positive.

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


