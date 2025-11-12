# Automatic Extraction of Hypothesis: AutoMergeNet: AutoML-Based M-Source Satellite Data Fusion Evaluated With Atmospheric Case Studies
*Julia Wąsala, Joannes D. Maasakkers, Berend J. Schuit, Gijs Leguijt, Ilse Aben, Rochelle Schneider, Holger Hoos, Mitra Baratchi*


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

The authors hypothesise that transforming conventional, single-branch image classification networks into multibranch networks improves the performance of multimodal image data fusion for satellite image classification compared to early fusion approaches.

The LLM has provided the following reasoning with this hypothesis:

This hypothesis is derived from the first research question in Section IV (page 5): '1) Does transforming conventional, single-branch image classification networks into multibranch networks improve the results of multimodal image data fusion for satellite image classification?'. The authors' proposed method, AutoMergeNet, is based on this transformation, and they expect it to outperform early fusion baselines, as stated in the abstract: 'AutoMergeNet performs strongly and consistently on these two multimodal classification problems, outperforming six baseline methods'.

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

The authors hypothesise that transforming conventional, single-branch image classification networks into multibranch networks improves the performance of multimodal image data fusion for satellite image classification compared to early fusion approaches, as they struggle to converge.

### hypothesis_2

The LLM has found the following **implied** hypothesis:

The authors hypothesise that using a unimodal auxiliary classifier to enforce an implicit focus on the primary data modality improves the performance of multimodal image data fusion for satellite image classification.

The LLM has provided the following reasoning with this hypothesis:

This hypothesis is derived from the second research question in Section IV (page 5): '2) Does enforcing implicit focus on the primary modality (using a unimodal auxiliary classifier) improve the results of multimodal image data fusion for satellite image classification?'. The authors propose this auxiliary classifier as a key component of their pipeline to 'reduce false positives' (Section III-B, page 5).

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


### hypothesis_3

The LLM has found the following **implied** hypothesis:

The authors hypothesise that models created by their automated AutoMergeNet framework can achieve performance competitive with domain-specific, manually-designed methods when applied in an operational scenario.

The LLM has provided the following reasoning with this hypothesis:

This hypothesis is derived from the third research question in Section IV (page 5): '3) How do AutoMergeNet-created models compare to domain-specific methods when applied in an operational scenario?'. The abstract also states they 'demonstrate the usability of our framework with a realistic methane plume detection use case, which shows that AutoMergeNet can be used as a highly specialized, state-of-the-art approach'.

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

Please write the amount of hypothesis you had for the study: [4]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;
hypothesis_4: We hypothesise that NAS is capable of finding architectures that perform better at Multi-Modal Data Fusion tasks, as neural architectures may be different between tasks.

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
The performance of AutoMergeNet is compared against six state-of-the-art image classification models configured for early fusion. The evaluation is conducted on two distinct atmospheric plume detection datasets. The entire comparison is performed twice: once using the full proposed pipeline including an auxiliary classifier, and once without it to assess its impact.

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.



#### Hypothesis list
This experiment is used for the following hypotheses: hypothesis_1, hypothesis_2
Your corrected list (empty if correct):

#### Metrics list
The measured metrics in this experiment are: Accuracy, Precision, Recall, F1
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Mean with standard deviation
Your corrected list (empty if correct):

#### Strategy and Test
The experiment strategy is summarised as: For each model, multiple independent optimization runs are performed (5 HPO runs for baselines, 30 NAS runs for AutoMergeNet). The best configuration from each run is then trained 5 times. The final reported score is a bootstrapped mean and standard deviation of the test scores from the best models found across all runs. Data splits are: Methane (Random split (train=0.64, validation=0.16, test=0.20)), Carbon Monoxide (Location-based split (train=0.64, validation=0.16, test=0.20)).
Your corrected answer (empty if correct):

The experiment test is summarised as: Wilcoxon signed rank test (p < 0.05)
Your corrected answer (empty if correct):

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

The results of the experiment are as follows:

{
    "Methane Plume Detection Dataset (Schuit et al. 2023)": { TABLE IV TODO CHECK
        "With auxiliary classifier": {
            "Accuracy": {
                "BANet [9]": "0.88±0.02",
                "CNN [16]": "0.89±0.01",
                "CvT [11]": "0.88±0.03",
                "EpsaNet [44]": "0.87±0.04",
                "ResNet [8]": "0.88±0.03",
                "MobileNetV2 [10]": "0.89±0.00",
                "AutoMergeNet": "0.94±0.01"
            },
            "Precision": {
                "BANet [9]": "0.85±0.02",
                "CNN [16]": "0.86±0.02",
                "CvT [11]": "0.85±0.04",
                "EpsaNet [44]": "0.84±0.03",
                "ResNet [8]": "0.84±0.03",
                "MobileNetV2 [10]": "0.84±0.02",
                "AutoMergeNet": "0.91±0.03"
            },
            "Recall": {
                "BANet [9]": "0.79±0.06",
                "CNN [16]": "0.80±0.04",
                "CvT [11]": "0.78±0.12",
                "EpsaNet [44]": "0.77±0.18",
                "ResNet [8]": "0.80±0.12",
                "MobileNetV2 [10]": "0.81±0.02",
                "AutoMergeNet": "0.91±0.02"
            },
            "F1": {
                "BANet [9]": "0.81±0.03",
                "CNN [16]": "0.82±0.02",
                "CvT [11]": "0.81±0.07",
                "EpsaNet [44]": "0.78±0.14",
                "ResNet [8]": "0.81±0.09",
                "MobileNetV2 [10]": "0.83±0.01",
                "AutoMergeNet": "0.88±0.09"
            }
        },
        "Without auxiliary classifier": {
            "Accuracy": {
                "BANet [9]": "0.58±0.05",
                "CNN [16]": "0.62±0.04",
                "CvT [11]": "0.56±0.08",
                "EpsaNet [44]": "0.55±0.06",
                "ResNet [8]": "0.55±0.06",
                "MobileNetV2 [10]": "0.57±0.03",
                "AutoMergeNet": "0.90±0.13"
            },
            "Precision": {
                "BANet [9]": "0.43±0.03",
                "CNN [16]": "0.46±0.03",
                "CvT [11]": "0.42±0.05",
                "EpsaNet [44]": "0.42±0.06",
                "ResNet [8]": "0.42±0.06",
                "MobileNetV2 [10]": "0.43±0.02",
                "AutoMergeNet": "0.83±0.13"
            },
            "Recall": {
                "BANet [9]": "0.82±0.07",
                "CNN [16]": "0.83±0.05",
                "CvT [11]": "0.81±0.012",
                "EpsaNet [44]": "0.80±0.18",
                "ResNet [8]": "0.80±0.18",
                "MobileNetV2 [10]": "0.84±0.03",
                "AutoMergeNet": "0.94±0.04"
            },
            "F1": {
                "BANet [9]": "0.57±0.02",
                "CNN [16]": "0.59±0.01",
                "CvT [11]": "0.55±0.04",
                "EpsaNet [44]": "0.53±0.08",
                "ResNet [8]": "0.53±0.08",
                "MobileNetV2 [10]": "0.57±0.01",
                "AutoMergeNet": "0.91±0.04"
            }
        }
    },
    "Carbon Monoxide Plume Detection Dataset (This work)": { TABLE V, TODO CHECK
        "With auxiliary classifier": {
            "Accuracy": {
                "BANet [9]": "0.87±0.02",
                "CNN [16]": "0.91±0.02",
                "CvT [11]": "0.83±0.02",
                "EpsaNet [44]": "0.86±0.02",
                "ResNet [8]": "0.86±0.02",
                "MobileNetV2 [10]": "0.86±0.02",
                "AutoMergeNet": "0.91±0.04"
            },
            "Precision": {
                "BANet [9]": "0.91±0.02",
                "CNN [16]": "0.91±0.02",
                "CvT [11]": "0.92±0.04",
                "EpsaNet [44]": "0.91±0.02",
                "ResNet [8]": "0.93±0.03",
                "MobileNetV2 [10]": "0.92±0.03",
                "AutoMergeNet": "0.93±0.01"
            },
            "Recall": {
                "BANet [9]": "0.54±0.09",
                "CNN [16]": "0.71±0.07",
                "CvT [11]": "0.36±0.09",
                "EpsaNet [44]": "0.50±0.09",
                "ResNet [8]": "0.48±0.11",
                "MobileNetV2 [10]": "0.50±0.10",
                "AutoMergeNet": "0.89±0.02"
            },
            "F1": {
                "BANet [9]": "0.67±0.07",
                "CNN [16]": "0.80±0.05",
                "CvT [11]": "0.51±0.09",
                "EpsaNet [44]": "0.64±0.08",
                "ResNet [8]": "0.62±0.09",
                "MobileNetV2 [10]": "0.64±0.08",
                "AutoMergeNet": "0.85±0.03"
            }
        },
        "Without auxiliary classifier": {
            "Accuracy": {
                "BANet [9]": "0.81±0.04",
                "CNN [16]": "0.87±0.02",
                "CvT [11]": "0.74±0.01",
                "EpsaNet [44]": "0.81±0.03",
                "ResNet [8]": "0.81±0.03",
                "MobileNetV2 [10]": "0.82±0.02",
                "AutoMergeNet": "0.90±0.02"
            },
            "Precision": {
                "BANet [9]": "0.64±0.07",
                "CNN [16]": "0.71±0.05",
                "CvT [11]": "0.54±0.12",
                "EpsaNet [44]": "0.65±0.07",
                "ResNet [8]": "0.64±0.07",
                "MobileNetV2 [10]": "0.66±0.05",
                "AutoMergeNet": "0.78±0.06"
            },
            "Recall": {
                "BANet [9]": "0.64±0.09",
                "CNN [16]": "0.83±0.08",
                "CvT [11]": "0.44±0.11",
                "EpsaNet [44]": "0.61±0.10",
                "ResNet [8]": "0.57±0.13",
                "MobileNetV2 [10]": "0.60±0.11",
                "AutoMergeNet": "0.89±0.08"
            },
            "F1": {
                "BANet [9]": "0.64±0.07",
                "CNN [16]": "0.76±0.05",
                "CvT [11]": "0.46±0.08",
                "EpsaNet [44]": "0.62±0.07",
                "ResNet [8]": "0.6±0.08",
                "MobileNetV2 [10]": "0.62±0.07",
                "AutoMergeNet": "0.82±0.04"
            }
        }
    }
    TODO: Figure 5
    TODO: Figure 6
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
The single best methane detection model generated by AutoMergeNet is applied to a previously unseen, week-long set of TROPOMI satellite data. The resulting detections are manually labeled by experts and compared to the detections from a highly specialized, operational model by Schuit et al. [1] on the same data.

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.



#### Hypothesis list
This experiment is used for the following hypotheses: hypothesis_3
Your corrected list (empty if correct):

#### Metrics list
The measured metrics in this experiment are: Number of detected plumes, Number of false positives, Number of inconclusive cases
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Raw counts of detections
Your corrected list (empty if correct):

#### Strategy and Test
The experiment strategy is summarised as: The pre-trained model is applied to a new dataset of 17,760 images generated by applying a sliding window over the raw satellite data.
Your corrected answer (empty if correct): The pre-trained model is applied to a new dataset of 17,760 images generated by applying a sliding window over the raw satellite data, duplicates were partially automatically and partially corrected by hand. The labelling of the data was conducted by three experts unanimously. 

The experiment test is summarised as: Direct comparison of detection counts between the two models.
Your corrected answer (empty if correct):

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

The results of the experiment are as follows:

{  # TODO Check text Section V subsection C.
    "TROPOMI methane data (25-31 October 2021)": {
        "Number of detected plumes": {
            "AutoMergeNet": 73,
            "Schuit et al. [1]": 85
        },
        "Number of false positives": {
            "AutoMergeNet": 67,
            "Schuit et al. [1]": 20
        },
        "Number of inconclusive cases": {
            "AutoMergeNet": 46,
            "Schuit et al. [1]": 48
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

Please write the amount of experiments you had for the study: [2]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Interpretation

Experiment outcomes are analysed and interpreted to determine whether the experiment supports the hypothesis or not. 

The LLM has found the following interpretations of the experiment outcomes;

### interpretation_1

This interpretation has the following description/reasoning:
The results support the hypothesis. As stated in Section V-A (page 8), 'on both datasets, AutoMergeNet outperformed all baselines by significant margins in terms of accuracy, precision, and recall'. The authors also note that 'AutoMergeNet never selected models with fusion depth 0. These results suggest that multibranch networks of any depth achieve higher performance for methane and carbon monoxide plume detection than early fusion networks.' Tables IV and V show that AutoMergeNet achieves the highest scores across all metrics, with the improvements being statistically significant.

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
The results support the hypothesis. Section V-B (page 9) states, 'The auxiliary classifier substantially increased the precision and accuracy of all approaches, especially the baselines.' A direct comparison of the 'With auxiliary classifier' and 'Without auxiliary classifier' sections in Tables IV and V confirms this. For instance, on the methane dataset (Table IV), the baselines' precision improves from ~0.42-0.46 to ~0.84-0.86, and accuracy improves from ~0.55-0.62 to ~0.87-0.89, demonstrating the significant positive impact of the auxiliary classifier.

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

### interpretation_3

This interpretation has the following description/reasoning:
The results support the hypothesis, with a caveat. The authors conclude that their model is 'competitive with the expert-designed pipeline in terms of detecting plumes' (Section V-C, page 10), finding a comparable number of plumes (73 vs. 85). This demonstrates that an automatically generated model can perform a complex, real-world task at a level similar to a highly specialized, manually engineered one. However, the authors also acknowledge a key weakness: their model 'does produce relatively more false positives (67 for AutoMergeNet, 20 for the model by Schuit et al. [1])', indicating a trade-off between automation and precision that requires further investigation.

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



This interpretation is to support (or not) the following hypothesis: hypothesis_3
Your corrected answer (empty if correct):

This interpretation supports the hypothesis: True
Your corrected answer (empty if correct):

## General Interpretation notes

We are missing one interpretation of experiment_1: Namely we find that smaller or simpler networks perform better on this problem than deeper or more complex methods.
