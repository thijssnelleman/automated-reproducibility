# Automatic Extraction of Hypothesis: EDC: Equation Discovery for Classification
*Guus Toussaint, Arno Knobbe*


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

The authors hypothesise that their proposed Equation Discovery for Classification (EDC) method can discover concise and interpretable analytical functions for binary classification that (a) achieve performance comparable to state-of-the-art classification algorithms, (b) outperform existing Equation Discovery-based classification methods, and (c) can accurately reconstruct the underlying decision boundaries in both artificial and real-world data.

The LLM has provided the following reasoning with this hypothesis:

This hypothesis is implied from the abstract and the summary of contributions. The abstract states that EDC achieves 'performance comparable to the state of the art in binary classification' and outperforms 'current state-of-the-art ED-based classification methods'. The contributions on page 3 reiterate these claims, stating EDC's performance is 'comparable to the current state-of-the-art' and that it can 'reconstruct a hard-coded decision boundary in artificial data'.

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

The authors hypothesise that their proposed Equation Discovery for Classification (EDC) method can discover concise and interpretable analytical functions for binary classification that (a) achieve performance comparable to state-of-the-art classification algorithms, (b) outperform existing interpretable binary classification methods, and (c) can accurately reconstruct the underlying decision boundaries in both artificial and real-world data.

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
Evaluation of EDC on four sets of artificial data with increasing difficulty: 1) target equation within search space, 2) target within search space with noise, 3) target beyond search space with noise, and 4) data generated from Gaussian clusters without an explicit equation. This tests the algorithm's ability to reconstruct decision boundaries and its performance in a setting without a ground-truth equation.

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
The measured metrics in this experiment are: AUC
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Mean with standard deviation
Your corrected list (empty if correct):

#### Strategy and Test
The experiment strategy is summarised as: For each of the four scenarios, 100 datasets were generated and evaluated.
Your corrected answer (empty if correct):

The experiment test is summarised as: Comparison of mean AUC values. For the noisy datasets, a paired t-test (p < .001) is used to compare EDC's performance against the original decision boundary.
Your corrected answer (empty if correct): Comparison of mean AUC values. For the artificial datasets with a ground truth decision boundary, a paired t-test (p < .001) is used to compare EDC's performance against the original decision boundary. For the Gaussian Clusters dataset a paired t-test (p < .001) is used to compare EDC's performance against the performance of other binary classification algorithms.

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

The results of the experiment are as follows:

{
    "Within search space (This work)": {
        "AUC": "0.999 ± 0.00"
    },
    "Within search space with noise (This work)": {
        "AUC": "0.951 ± 0.03"
    },
    "Beyond search space with noise (This work)": {
        "AUC": "0.962 ± 0.03"
    },
    "Within search space (Original DB)": {
        "AUC": "1.000 ± 0.00"
    },
    "Within search space with noise (Original DB)": {
        "AUC": "0.943 ± 0.03"
    },
    "Beyond search space with noise (Original DB)": {
        "AUC": "0.956 ± 0.03"
    },
    "Gaussian clusters (This work)": {
        "AUC": "0.965 ± 0.043"
    }
    "Gaussian clusters (MLP)": {
        "AUC": "0.972 ± 0.034"
    }
    "Gaussian clusters (SVM)": {
        "AUC": "0.970 ± 0.038"
    }
    "Gaussian clusters (RF)": {
        "AUC": "0.967 ± 0.037"
    }
    "Gaussian clusters (Tree)": {
        "AUC": "0.899 ± 0.079"
    }
    "Gaussian clusters (M4GP)": {
        "AUC": "0.894 ± 0.082"
    }
    "Gaussian clusters (LDA)": {
        "AUC": "0.811 ± 0.139"
    }
    "Gaussian clusters (AMAXSC)": {
        "AUC": "0.802 ± 0.181"
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
Evaluation of EDC and several other classifiers (AMAXSC, M4GP, LDA, Tree, MLP, RF, SVM) on nine real-world binary classification datasets from the UCI repository.

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
The measured metrics in this experiment are: AUC
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Mean with standard deviation
Your corrected list (empty if correct):

#### Strategy and Test
The experiment strategy is summarised as: 10-fold cross-validation
Your corrected answer (empty if correct):

The experiment test is summarised as: Critical distance plot (Demšar, 2006) to compare the average ranks of the classifiers and test for statistical significance.
Your corrected answer (empty if correct):

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

The results of the experiment are as follows:

{
    "ADULT [3]": {
        "AUC": {
            "Ours": 0.889,
            "AMAXSC" : 0.807,            
            "M4GP" : 0.770,
            "LDA" : 0.902,
            "Tree" : 0.730,
            "MLP" : 0.901,
            "RF" : 0.880,
            "SVM" : 0.898,
        }
    },
    "BANKNOTE [18]": {
        "AUC": {
            "Ours": 1.000,
            "AMAXSC" : 0.982,
            "M4GP" : 0.999,
            "LDA" : 1.000,
            "Tree" : 0.979, 
            "MLP" : 1.000,
            "RF" : 1.000,
            "SVM" : 1.000,
        }
    },
    "BREAST [28]": {
        "AUC": {
            "Ours": 0.670,
            "AMAXSC" : 0.617,
            "M4GP" : 0.614,
            "LDA" : 0.636,
            "Tree" : 0.590, 
            "MLP" : 0.701,
            "RF" : 0.683,
            "SVM" : 0.709,
        }
    },
    "CREDIT [22]": {
        "AUC": {
            "Ours": 0.918,
            "AMAXSC" : 0.896,
            "M4GP" : 0.869,
            "LDA" : 0.924,
            "Tree" : 0.812, 
            "MLP" : 0.910,
            "RF" : 0.935,
            "SVM" : 0.920,
        }
    },
    "CYLINDER [9]": {
        "AUC": {
            "Ours": 0.735,
            "AMAXSC" : 0.547,
            "M4GP" : 0.703,
            "LDA" : 0.778,
            "Tree" : 0.594, 
            "MLP" : 0.844,
            "RF" : 0.870,
            "SVM" : 0.759,
        }
    },
    "DIABETES": {
        "AUC": {
            "Ours": 0.830,
            "AMAXSC" : 0.799,
            "M4GP" : 0.724,
            "LDA" : 0.829,
            "Tree" : 0.673, 
            "MLP" : 0.843,
            "RF" : 0.826,
            "SVM" : 0.836,
        }
    },
    "IONOSPHERE [25]": {
        "AUC": {
            "Ours": 0.894,
            "AMAXSC" : 0.888,
            "M4GP" : 0.855,
            "LDA" : 0.901,
            "Tree" : 0.892, 
            "MLP" : 0.985,
            "RF" : 0.979,
            "SVM" : 0.979,
        }
    },
    "OCCUPANCY [6]": {
        "AUC": {
            "Ours": 0.996,
            "AMAXSC" : 0.994,
            "M4GP" : 0.990,
            "LDA" : 0.994,
            "Tree" : 0.989, 
            "MLP" : 0.997,
            "RF" : 0.999,
            "SVM" : 0.993,
        }
    },
    "SONAR [24]": {
        "AUC": {
            "Ours": 0.780,
            "AMAXSC" : 0.762,
            "M4GP" : 0.767,
            "LDA" : 0.803,
            "Tree" : 0.731, 
            "MLP" : 0.927,
            "RF" : 0.917,
            "SVM" : 0.916,
        }
    }
    "Average Score": {
        "Ours": 0.857,
        "AMAXSC" : 0.810,
        "M4GP" : 0.810,
        "LDA" : 0.863,
        "Tree" : 0.777,
        "MLP" : 0.901,
        "RF" : 0.899,
        "SVM" : 0.890,
    }
    "Average Rank": {
        "Ours": 4.00,
        "AMAXSC" : 6.44,
        "M4GP" : 6.78,
        "LDA" : 3.56,
        "Tree" : 7.67, 
        "MLP" : 1.89,
        "RF" : 2.78,
        "SVM" : 2.78,
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

Please write the amount of experiments you had for the study: [2]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Interpretation

Experiment outcomes are analysed and interpreted to determine whether the experiment supports the hypothesis or not. 

The LLM has found the following interpretations of the experiment outcomes;

## interpretation_1

This interpretation has the following description/reasoning:
The results on artificial data support the hypothesis. For data generated from an equation within its search space, EDC achieves a near-perfect AUC of 0.999, demonstrating its ability to reconstruct the correct structure (Page 9). On noisy data, EDC finds decision boundaries that are significantly better than the original ones (p < .001), and it can approximate boundaries from outside its search space (Page 10). On the Gaussian cluster data, EDC's performance (AUC=0.965) is comparable to state-of-the-art methods like MLP (0.972) and RF (0.967), and it outperforms other explainable and ED-based methods (Table 2, Page 11).

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

## interpretation_2

This interpretation has the following description/reasoning:
The results on UCI datasets support the hypothesis. Regarding clause (b), the authors state 'for all datasets, the EDC algorithm achieves a higher AUC. This shows that our approach outperforms the current state-of-the-art ED-based approaches' (Page 12), which is confirmed by the average scores in Table 3 (EDC: 0.857 vs AMAXSC/M4GP: 0.810). Regarding clause (a), the critical distance plot in Figure 4 shows that while state-of-the-art methods like MLP and RF have better average ranks, 'current state-of-the-art classification algorithms do not significantly outperform our proposed EDC algorithms' (Page 12). This supports the claim of comparable performance. The authors do note that for some datasets (IONOSPHERE, SONAR), the performance gap is substantial, suggesting the grammar lacks the necessary building blocks for those problems.

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


