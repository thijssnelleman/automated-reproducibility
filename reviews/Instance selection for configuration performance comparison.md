# Automatic Extraction of Study Representation: Instance selection for configuration performance comparison
*Marie Anastacio, Théo Matricon, Holger H. Hoos*


You will be presented with the output of an LLM which was tasked to extract a representation of your study based on your paper, including research questions, hypotheses, the experiment used to test the hypothesis, the interpretation of the outcome of the experiment and your conclusions.

We ask you to **open your PDF** that was presented to the LLM, to reflect upon the LLM's answer with your paper.

The answer of the LLM is structured into three parts; Hypothesis, experiments and interpretation (of experiment outcome).
- For each experiment the LLM has linked it to one or more hypothesis
- For each interpretation, the LLM has linked it to **one** experiment and **one** hypothesis.

A few notes:
- Research questions are seen as motiviations for the study; they are framed as questions but are often encountered problems as well in the field of computational science.
- The LLM has been tasked to extract a hypothesis **including an expected outcome**. Some studies may have new hypotheses developed during the study instead of before; it should be interpreted as a post-hoc hypothesis.
- The LLM is also tasked to connect the figures, tables and textual results to your experiments. It needs to be verified that these links make sense with its representation.

Please answer the questions in the  following sections.

## Research Questions

### research_question_1

The LLM has found the following **explicit** research question:

How does the selection method perform to compare a new configuration to the incumbent on the subset of instances for which we already collected information throughout the configuration run as seen in phase 1?

The LLM has provided the following reasoning with this research question:

Explicitly stated in Section 4 (Empirical evaluation) as Q1.

Please grade the research question stated from the following options:

The LLM ...
[X] captures the research question (nearly) perfectly.
[] has stated a research question capturing the general spirit of our work.
[] has stated an incomplete research question; the answer is correct but is missing key information.
[] has stated a general research question but has introduced false or incorrect information.
[] has stated a research question similar to ours, but is far too innaccurate to consider correct.
[] has stated a research question that has (nearly) no overlap with our work.
[] has stated a research question of lesser quality than described above: If it is an hallucination, please explain below.


Based on the LLMs answer, would you like to improve the answer to more accurately capture the research question?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.


### research_question_2

The LLM has found the following **explicit** research question:

How does the selection method perform to compare a new configuration to the incumbent on all instances, selecting instances for which we did not collect information throughout the configuration run as seen in phase 2?

The LLM has provided the following reasoning with this research question:

Explicitly stated in Section 4 (Empirical evaluation) as Q2.

Please grade the research question stated from the following options:

The LLM ...
[X] captures the research question (nearly) perfectly.
[] has stated a research question capturing the general spirit of our work.
[] has stated an incomplete research question; the answer is correct but is missing key information.
[] has stated a general research question but has introduced false or incorrect information.
[] has stated a research question similar to ours, but is far too innaccurate to consider correct.
[] has stated a research question that has (nearly) no overlap with our work.
[] has stated a research question of lesser quality than described above: If it is an hallucination, please explain below.


Based on the LLMs answer, would you like to improve the answer to more accurately capture the research question?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.



### General Research Questions questions

The LLM has provided you with one or more research questions from your work. Is this the amount of research questions the same as the amount you specified or implied?

Please write the amount of research questions you had for the study: [2]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Hypotheses

### hypothesis_1

The LLM has found the following **implied** hypothesis:

The authors hypothesise that carefully selecting instances using methods based on performance models (such as discrimination, variance, UDD, or uncertainty) will significantly reduce the time required to accurately decide the better of two given algorithm configurations compared to uniform random sampling.

The LLM has provided the following reasoning with this hypothesis:

Implied in the Abstract and Introduction. The authors state that prior work showed instance selection reduces time for algorithm comparison, and they explore applying a similar process to configuration comparison, expecting a speed-up over random sampling.

The LLM has linked the hypothesis to the following research questions: research_question_1, research_question_2
Your corrected list (empty if correct):

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

The LLM has provided you with zero or more hypothesis from your work. Is this the amount of hypothesis the same as the amount you specified?

Please write the amount of hypothesis you had for the study: [1]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Experiments

The LLM has found one or more experiment that were used for the empirical evaluation of your research questions or hypotheses. 

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
Phase 1 evaluation: Comparing configurations on known instances. A fraction of instances and configurations are randomly selected as known data to train a Random Forest model. A challenger configuration is picked, and instances are iteratively selected using the selection methods to compare it against the incumbent. The process stops when all selected instances are run, and a Wilcoxon test is used to decide if the challenger can be discarded.
> Phase 1 evaluation: Comparing configurations on known instances. A fraction of instances and configurations are randomly selected as known data to train a Random Forest model. A challenger configuration is picked, and instances are iteratively selected using the selection methods to compare it against the incumbent. The process stops when all selected instances are run, **or** when the Wilcoxon test decides that the challenger can be discarded.

The LLM ...
[] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[X] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

The LLM has found the following strategy or protocol for the experiment: Random split of instances (p_I in [0.1, 0.2, 0.3, 0.4, 0.5]) and configurations (p_C in [10, 20, 30, 40, 50]) into known/unknown sets. 10 seeds per pair.
Your corrected answer (empty if correct): Random sampling of instances (p_I in [0.1, 0.2, 0.3, 0.4, 0.5]) and configurations (p_C in [10, 20, 30, 40, 50]) into known/unknown sets. 10 seeds per pair.

The LLM has found the following data (sets) used as input for the experiment: Circuitfuzz (AClib), IBM (AClib), crypto (Nejati and Ganesh 2019), RCW2 (AClib), Regions200 (AClib), MIPverify (König et al. 2021)
Your corrected answer (empty if correct):

This experiment is used to answer the following research questions: research_question_1
Your corrected list (empty if correct):

This experiment is used for the following hypotheses: hypothesis_1
Your corrected list (empty if correct):

### experiment_2

The LLM describes this experiment as follows:
Phase 2 evaluation: Comparing configurations on unknown instances. A Random Forest model is trained on known data. Two configurations that cannot be told apart by a Wilcoxon test are chosen. Up to 10 unknown instances are iteratively selected and run for both configurations until they can be told apart by the test.

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

The LLM has found the following strategy or protocol for the experiment: Random split of instances (p_I in [0.1, 0.2, 0.3, 0.4, 0.5]) and configurations (p_C in [10, 20, 30, 40, 50]) into known/unknown sets. Stopping criterion: maximum of 10 instances selected or configurations told apart.
Your corrected answer (empty if correct): Random sampling of instances (p_I in [0.1, 0.2, 0.3, 0.4, 0.5]) and configurations (p_C in [10, 20, 30, 40, 50]) into known/unknown sets. Stopping criterion: maximum of 10 instances selected or configurations told apart.

The LLM has found the following data (sets) used as input for the experiment: Circuitfuzz (AClib), IBM (AClib), crypto (Nejati and Ganesh 2019), RCW2 (AClib), Regions200 (AClib), MIPverify (König et al. 2021)
Your corrected answer (empty if correct):

This experiment is used to answer the following research questions: research_question_2
Your corrected list (empty if correct):

This experiment is used for the following hypotheses: hypothesis_1
Your corrected list (empty if correct):


### General Experiment Questions

The LLM has provided you with one or more experiments from your work. Is this amount of experiments the same as the amount you specified?

Please write the amount of experiments you had for the study: [2]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Analysis

The LLM has found one or more analyses that were used to investigate the outcomes of your experiment(s).

### analysis_1

This analysis has the following description/reasoning:
Evaluating the accuracy of the selection methods over time in Phase 1 by comparing the outcome of the Wilcoxon test on the selected instances to the ground truth (all known instances).

Based on the LLMs answer, would you like to improve the answer to more accurately capture the analysis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This analysis is based on the following experiment(s) (outcomes): experiment_1
Your corrected answer (empty if correct): 

#### Metrics list
The measured metrics in this analysis are: Accuracy, Percentage of time spent, Area under the curve (AUC)
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Mean accuracy, Area under the curve (AUC)
Your corrected list (empty if correct):

#### Analysis Test

The analysis test is summarised as: Wilcoxon matched-pairs signed-ranks test (p = 0.05)
Your corrected answer (empty if correct):

#### Results

The LLM has found the data of the analysis in the study, which is summarised below. It states either the figures, tables or in text values where it has been found. It describes each with a caption (in case of figure/table), a reason, and subsets of the sets stated before: the metrics used for the analysis, the statistics used, which input data was used, and, which test was applied to reflect upon research questions or confirm/reject hypotheses.

The analysed results were found in the following locations:

- **Tables**:
- **Figures**:
  - **Figure 1**:
    - **caption**:
      - Mean accuracy of the Wilcoxon test (p=0.05) on which among Cch and Cinc performs best along the percentage of time spent on evaluations (100% means that all instances of Iknown have been run)
    - **reason**:
      - Shows the collected accuracy over the time spent to make the comparison for two examples.
    - **metrics**:
      - Accuracy
      - Percentage of time spent
    - **statistics**:
      - Mean accuracy
    - **data**:
      - IBM (AClib)
      - RCW2 (AClib)
    - **test**:
      - Wilcoxon matched-pairs signed-ranks test (p = 0.05)
  - **Figure 2**:
    - **caption**:
      - Area under the curve of the mean accuracy of the Wilcoxon test (p=0.05) on which among Cch and Cinc performs best along the time spent on evaluations
    - **reason**:
      - Synthesizes the curves by computing the AUC for each method across different amounts of prior data.
    - **metrics**:
      - Area under the curve (AUC)
    - **statistics**:
      - Area under the curve (AUC)
    - **data**:
      - Circuitfuzz (AClib)
      - IBM (AClib)
      - crypto (Nejati and Ganesh 2019)
      - RCW2 (AClib)
      - Regions200 (AClib)
      - MIPverify (König et al. 2021)
    - **test**:
      - Wilcoxon matched-pairs signed-ranks test (p = 0.05)
- **Text**:


#### General

The LLM has overall captured the analysis details...

[X] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)

### analysis_2

This analysis has the following description/reasoning:
Evaluating the time used to decide between two configurations on unknown instances in Phase 2.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the analysis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This analysis is based on the following experiment(s) (outcomes): experiment_2
Your corrected answer (empty if correct): 

#### Metrics list
The measured metrics in this analysis are: Time used (seconds)
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Median time
Your corrected list (empty if correct):

#### Analysis Test

The analysis test is summarised as: Wilcoxon matched-pairs signed-ranks test (p = 0.05)
Your corrected answer (empty if correct):

#### Results

The LLM has found the data of the analysis in the study, which is summarised below. It states either the figures, tables or in text values where it has been found. It describes each with a caption (in case of figure/table), a reason, and subsets of the sets stated before: the metrics used for the analysis, the statistics used, which input data was used, and, which test was applied to reflect upon research questions or confirm/reject hypotheses.

The analysed results were found in the following locations:

- **Tables**:
  - **Table 1**:
    - **caption**:
      - Median time in seconds for each method over every tested prior data
    - **reason**:
      - Reports the median time used to run the instances selected by each of the methods for each prior data.
    - **metrics**:
      - Time used (seconds)
    - **statistics**:
      - Median time
    - **data**:
      - Circuitfuzz (AClib)
      - IBM (AClib)
      - crypto (Nejati and Ganesh 2019)
      - RCW2 (AClib)
      - Regions200 (AClib)
      - MIPverify (König et al. 2021)
    - **test**:
      - Wilcoxon matched-pairs signed-ranks test (p = 0.05)
- **Figures**:
  - **Figure 3**:
    - **caption**:
      - Time used (in seconds) before taking a decision based on a Wilcoxon test (p=0.05) or reaching a maximum of 10 instance selected
    - **reason**:
      - Shows the running times obtained for two examples in Phase 2.
    - **metrics**:
      - Time used (seconds)
    - **statistics**:
      - Median time
    - **data**:
      - crypto (Nejati and Ganesh 2019)
      - RCW2 (AClib)
    - **test**:
      - Wilcoxon matched-pairs signed-ranks test (p = 0.05)
- **Text**:


#### General

The LLM has overall captured the analysis details...

[X] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)


### General Analysis Questions

The LLM has provided you with one or more analyses from your work. Is this amount of analyses the same as the amount you specified?

Please write the amount of analyses you had for the study: [2]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Interpretation

Experiment outcomes are analysed and interpreted to determine whether the experiment supports the hypothesis or not. 

The LLM has found the following interpretations of the experiment outcomes;

### interpretation_1

This interpretation has the following description/reasoning:
Randomly sampling instances performs well but in most cases the discrimination and variance approaches do better. UDD and uncertainty have a lower accuracy than random sampling in some cases. There is a clear correlation between the amount of known configuration and the AUC, but adding more instances does not significantly improve performance.

The LLM has provided the following notes on its reasoning:
The authors interpret the AUC and accuracy over time curves in Section 5.1, noting the superiority of discrimination and variance methods and the impact of prior data.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason: Randomly sampling instances performs well but in most cases the discrimination and variance approaches do better. UDD and uncertainty have a lower performance than random sampling in some cases. There is a clear correlation between the amount of known configuration and the AUC, but adding more instances does not significantly improve performance.

This interpretation is based on the following analyses: analysis_1
Your corrected answer (empty if correct):

Answer this question about the (possibly **corrected!**) analyses_id.
This interpretation of the analysis is ...
[] Correct
[X] Almost correct (few and minor misinterpretations or mistakes)
[] Acceptable (some misinterpretations or mistakes)
[] (Partially) Incorrect (serious misinterpretations or mistakes)
[] Incorrect
[] Hallucinatory, if so explain below:

### interpretation_2

This interpretation has the following description/reasoning:
Most cases show that random is outperformed by all methods, with some exceptions. Discrimination and variance outperform the other methods in almost all cases, with variance providing a speedup ranging from a 5.8 up to 3000 times speedup compared to random.

The LLM has provided the following notes on its reasoning:
The authors interpret the median time results from Table 1 and Figure 3 in Section 5.2, highlighting the massive speedup achieved by the variance method.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This interpretation is based on the following analyses: analysis_2
Your corrected answer (empty if correct):

Answer this question about the (possibly **corrected!**) analyses_id.
This interpretation of the analysis is ...
[X] Correct
[] Almost correct (few and minor misinterpretations or mistakes)
[] Acceptable (some misinterpretations or mistakes)
[] (Partially) Incorrect (serious misinterpretations or mistakes)
[] Incorrect
[] Hallucinatory, if so explain below:


### General Interpretation Questions

The LLM has provided you with one or more interpretations from your work. Is this amount of interpretations the same as the amount you specified?

Please write the amount of interpretations you had for the study: [2]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;

## Conclusions

The interpretations are used to draw conclusions, which either reflect upon the previous research questions or hypotheses, or yield new research questions or hypotheses.

The LLM has found the following conclusions on the interpretations;

### conclusion_1

This conclusion has the following description/reasoning:
The authors conclude that selecting instances smartly allows quicker comparison between configurations of an algorithm. They found considerable potential in the use of these methods, in particular the ones based on the variability in running time or on discrimination power, which successfully reduced the time required to accurately decide the better of two given algorithms.

The LLM has provided the following notes on this conclusion:
Summarized from Section 6 (Conclusion and future work), where the authors state that their results show considerable potential in both cases (Phase 1 and Phase 2), especially for variance and discrimination methods.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the conclusion?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This conclusion is based on the following interpretations: interpretation_1, interpretation_2
Your corrected answer (empty if correct):

Answer this question about the (possibly **corrected!**) interpretation_id.
This conclusion based on the interpretation(s) is ...
[X] Correct
[] Almost correct (few and minor misinterpretations or mistakes)
[] Acceptable (some misinterpretations or mistakes)
[] (Partially) Incorrect (serious misinterpretations or mistakes)
[] Incorrect
[] Hallucinatory, if so explain below:

Next, the LLM was asked to link the conclusion to the following elements:

This conclusion is to answer (or reflect) upon the following research questions: research_question_1, research_question_2
Your corrected answer (empty if correct):

This conclusion is to support (or not) the following hypotheses: hypothesis_1
Your corrected answer (empty if correct):

This conclusion supports the hypothesis: [True]
Your corrected answer (empty if correct):


### General Conclusion Questions

The LLM has provided you with one or more conclusions from your work. Is this amount of conclusions the same as the amount you specified?

Please write the amount of conclusions you had for the study: [1]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Future Work

The LLM has also found possible future work directions in terms of research questions or hypotheses yielded from an exploratory angle of your study.

### Suggested Research Questions

#### suggested_research_question_1

The LLM has found the following suggested research question: How can instance selection methods based on running time variability and discrimination power be effectively integrated into a full model-based algorithm configuration procedure?
Please correct the suggestion if wrong (leave empty if correct): How would instance selection methods based on running time variability and discrimination power perform once integretaed into a full model-based algorithm configuration procedure?

The LLM has provided the following note/location on the suggestion: Section 6. Conclusion and future work

The LLM has provided the following reason for the suggestion: Section 6. Conclusion and future work

The LLM has linked the suggestion to the following conclusions: conclusion_1
Please correct the IDs if wrong/missing (leave empty if correct):

Please grade the suggestion below:
[] The LLM has (nearly) perfectly captured a future research direction suggested by our work.
[] The LLM has stated a future research direction that was implied by our work, but not strongly suggested.
[X] The LLM has stated a future research direction from our work that is partially correct.
[] The LLM has stated a future research direction that has some overlap with our work but has introduced incorrect or false information.
[] The LLM has stated a future research direction that was not stated or implied in our work; the LLM has hallucinated this information.


#### Suggested Research Questions General

The LLM has provided you with one or more Suggested Research Questions from your work. Is this amount of Suggested Research Questions the same as the amount you specified?

Please write the amount of Suggested Research Questions you had for the study: [1]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


### Suggested Hypotheses



#### Suggested Hypotheses General

The LLM has provided you with one or more Suggested Hypotheses from your work. Is this amount of Suggested Hypotheses the same as the amount you specified?

Please write the amount of Suggested Hypotheses you had for the study: [0]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;
