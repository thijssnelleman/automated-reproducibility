# Automatic Extraction of Study Representation: Automatic Adjusting Global Similarity Measures in Learning CBR Systems

_Stuart G. Ottersen, Kerstin Bach_

You will be presented with the output of an LLM which was tasked to extract a representation of your study based on your paper, including research questions, hypotheses, the experiment used to test the hypothesis, the interpretation of the outcome of the experiment and your conclusions.

We ask you to **open your PDF** that was presented to the LLM, to reflect upon the LLM's answer with your paper.

The answer of the LLM is structured into three parts; Hypothesis, experiments and interpretation (of experiment outcome).

- For each experiment the LLM has linked it to one or more hypothesis
- For each interpretation, the LLM has linked it to **one** experiment and **one** hypothesis.

A few notes:

- Research questions are seen as motiviations for the study; they are framed as questions but are often encountered problems as well in the field of computational science.
- The LLM has been tasked to extract a hypothesis **including an expected outcome**. Some studies may have new hypotheses developed during the study instead of before; it should be interpreted as a post-hoc hypothesis.
- The LLM is also tasked to connect the figures, tables and textual results to your experiments. It needs to be verified that these links make sense with its representation.

Please answer the questions in the following sections.

## Research Questions

### research_question_1

The LLM has found the following **explicit** research question:

How does adding new cases affect the performance of a learning CBR system?

The LLM has provided the following reasoning with this research question:

Found in the Abstract and Section 5 (Discussion), where the authors explicitly state: '(1) How adding cases affects the performance'.

Please grade the research question stated from the following options:

The LLM ...
[] captures the research question (nearly) perfectly.
[X] has stated a research question capturing the general spirit of our work.
[] has stated an incomplete research question; the answer is correct but is missing key information.
[] has stated a general research question but has introduced false or incorrect information.
[] has stated a research question similar to ours, but is far too innaccurate to consider correct.
[] has stated a research question that has (nearly) no overlap with our work.
[] has stated a research question of lesser quality than described above: If it is an hallucination, please explain below.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the research question?

- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.
  The research question lacks context, as the question discussed in the paper is limited to only a specific context.

### research_question_2

The LLM has found the following **explicit** research question:

In what way can we detect and mitigate performance loss caused by concept drift in a growing case base?

The LLM has provided the following reasoning with this research question:

Found in Section 3.2 and Section 5 (Discussion), where the authors explicitly state: '(2) in what way can we detect and mitigate performance loss'.

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

### research_question_3

The LLM has found the following **explicit** research question:

How can we adjust the global similarity weights to maintain aligned knowledge containers?

The LLM has provided the following reasoning with this research question:

Found in Section 3.2 and Section 5 (Discussion), where the authors explicitly state: '(3) how to adjust the global similarity weights'.

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

Please write the amount of research questions you had for the study: [3]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;

## Hypotheses

### hypothesis_1

The LLM has found the following **implied** hypothesis:

The authors hypothesise that using a rolling window of the CBR system's performance to trigger feature weight updates (the RUGS method) will minimize unnecessary updates while maintaining predictive performance comparable to always updating.

The LLM has provided the following reasoning with this hypothesis:

Implied in Section 3.5 and the Abstract. The authors propose RUGS to avoid unnecessary updates and state their aim is to identify when drift is large enough to suggest an update, expecting it to maintain performance while reducing computational cost.

The LLM has linked the hypothesis to the following research questions: research_question_2, research_question_3
Your corrected list (empty if correct):research_question_1,research_question_2, research_question_3

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
The experiment simulates concept drift by introducing cases to the CBR system in batches sorted by a single feature. It compares three feature weight updating strategies: no update after the first batch, updating after every batch, and updating using the RUGS method. The performance and number of updates are measured to evaluate the effectiveness of RUGS.

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

The LLM has found the following strategy or protocol for the experiment: Leave-one-out cross-validation (LOOCV) after each batch addition. Batch size is set to 3% of the dataset with a minimum threshold of 5. Concept drift is simulated by sorting a single feature in ascending order.
Your corrected answer (empty if correct):

The LLM has found the following data (sets) used as input for the experiment: Banking [13], Glioma [20], Iris [9], Tictactoe [3], Wdbc [23], Wine [2], Zoo [10]
Your corrected answer (empty if correct):

This experiment is used to answer the following research questions: research_question_1, research_question_2, research_question_3
Your corrected list (empty if correct):

This experiment is used for the following hypotheses: hypothesis_1
Your corrected list (empty if correct):

### General Experiment Questions

The LLM has provided you with one or more experiments from your work. Is this amount of experiments the same as the amount you specified?

Please write the amount of experiments you had for the study: [1]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;

## Analysis

The LLM has found one or more analyses that were used to investigate the outcomes of your experiment(s).

### analysis_1

This analysis has the following description/reasoning:
Analysis of the predictive performance (F1-score) and the frequency/computational cost of updates across the three different updating strategies.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the analysis?

- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This analysis is based on the following experiment(s) (outcomes): experiment_1
Your corrected answer (empty if correct):

#### Metrics list

The measured metrics in this analysis are: F1-micro score, Accuracy, Number of updates, Running time (seconds)
Your corrected list (empty if correct):

#### Statistics

The statistics for the metrics used are: Mean, Standard deviation, Median, Quartiles
Your corrected list (empty if correct):

#### Analysis Test

The analysis test is summarised as: Direct comparison (greater than, less than, comparable)
Your corrected answer (empty if correct):

#### Results

The LLM has found the data of the analysis in the study, which is summarised below. It states either the figures, tables or in text values where it has been found. It describes each with a caption (in case of figure/table), a reason, and subsets of the sets stated before: the metrics used for the analysis, the statistics used, which input data was used, and, which test was applied to reflect upon research questions or confirm/reject hypotheses.

The analysed results were found in the following locations:

- **Tables**:
  - **Table 2**:
    - **caption**:
      - Showing results calculated on all features and all batches. Zoo has fewer updates due to the minimum size of 5 for the batch size.
    - **reason**:
      - Provides the quantitative results for F1-score and number of updates across all datasets and strategies.
    - **metrics**:
      - F1-micro score
      - Number of updates
    - **statistics**:
      - Mean
      - Standard deviation
    - **data**:
      - Banking [13]
      - Glioma [20]
      - Iris [9]
      - Tictactoe [3]
      - Wdbc [23]
      - Wine [2]
      - Zoo [10]
    - **test**:
      - Direct comparison (greater than, less than, comparable)
  - **Table 3**:
    - **caption**:
      - Showing the running time in seconds for the time random forest uses to calculate the feature attributions and average running time for RUGS
    - **reason**:
      - Demonstrates the computational efficiency of the RUGS method compared to calculating feature weights.
    - **metrics**:
      - Running time (seconds)
    - **statistics**:
      - Mean
      - Standard deviation
    - **data**:
      - Banking [13]
      - Glioma [20]
      - Iris [9]
      - Tictactoe [3]
      - Wdbc [23]
      - Wine [2]
      - Zoo [10]
    - **test**:
      - Direct comparison (greater than, less than, comparable)
- **Figures**:
  - **Figure 5**:
    - **caption**:
      - Showing boxplot of results for each dataset and each feature weight updating strategy. Calculated over all features and batches.
    - **reason**:
      - Visualizes the variance and median performance of the three strategies across all datasets.
    - **metrics**:
      - F1-micro score
    - **statistics**:
      - Median
      - Quartiles
    - **data**:
      - Banking [13]
      - Glioma [20]
      - Iris [9]
      - Tictactoe [3]
      - Wdbc [23]
      - Wine [2]
      - Zoo [10]
    - **test**:
      - Direct comparison (greater than, less than, comparable)
  - **Figure 6**:
    - **caption**:
      - Showing change in F1 score for each feature over batch number, the red lines represent feature weight updates performed .
    - **reason**:
      - Shows how RUGS detects performance drops and rebounds performance over time for the Iris dataset.
    - **metrics**:
      - F1-micro score
      - Number of updates
    - **statistics**:
      - Mean
    - **data**:
      - Iris [9]
    - **test**:
      - Direct comparison (greater than, less than, comparable)
  - **Figure 7**:
    - **caption**:
      - Showing the effect of rolling window size on predictive performance for iris dataset.
    - **reason**:
      - Analyzes the sensitivity of the RUGS method to its main parameter, the rolling window size.
    - **metrics**:
      - F1-micro score
      - Number of updates
    - **statistics**:
      - Mean
    - **data**:
      - Iris [9]
    - **test**:
      - Direct comparison (greater than, less than, comparable)
- **Text**:
  - **Section 4.3**:
    - **value**:
      - The effectiveness of RUGS is evident in the results of the experiment shown in Table 2. Here we see that the F1-score remains competitive with the continuously updated feature weights while using considerably fewer updates.
    - **reason**:
      - Summarizes the primary finding that RUGS achieves its goal of maintaining performance with fewer updates.
    - **metrics**:
      - F1-micro score
      - Number of updates
    - **statistics**:
      - Mean
      - Standard deviation
    - **data**:
      - Banking [13]
      - Glioma [20]
      - Iris [9]
      - Tictactoe [3]
      - Wdbc [23]
      - Wine [2]
      - Zoo [10]
    - **test**:
      - Direct comparison (greater than, less than, comparable)

For section 4.3 I do not directly mention the metrics or statistics the LLM does, but I refer to the table that does include those metrics.

#### General

The LLM has overall captured the analysis details...

[X] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)

### General Analysis Questions

The LLM has provided you with one or more analyses from your work. Is this amount of analyses the same as the amount you specified?

Please write the amount of analyses you had for the study: [1]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;

## Interpretation

Experiment outcomes are analysed and interpreted to determine whether the experiment supports the hypothesis or not.

The LLM has found the following interpretations of the experiment outcomes;

### interpretation_1

This interpretation has the following description/reasoning:
RUGS can perform similarly to always updating the feature weights. The variance is also very comparable, while for the initial feature weight update, the performance tends to be considerably worse and has a higher variance.

The LLM has provided the following notes on its reasoning:
Found in Section 4.3. The authors interpret the boxplots (Figure 5) to show that RUGS successfully matches the performance of continuous updates.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?

- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:
Include table 2 in reasoning.

This interpretation is based on the following analyses: analysis_1
Your corrected answer (empty if correct):

Answer this question about the (possibly **corrected!**) analyses_id.
This interpretation of the analysis is ...
[X] Correct
[] Almost correct (few and minor misinterpretations or mistakes)
[] Acceptable (some misinterpretations or mistakes)
[] (Partially) Incorrect (serious misinterpretations or mistakes)
[] Incorrect
[] Hallucinatory, if so explain below:

### interpretation_2

This interpretation has the following description/reasoning:
Selecting an excessively small window will cause an exaggerated number of updates, while a large window will allow for periods of poorer predictive performance.

The LLM has provided the following notes on its reasoning:
Found in Section 4.3. The authors interpret Figure 7 to highlight the importance of the window size parameter in balancing update frequency and performance drops.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?

- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:
Not necessarily excessive, but depending on importance of performance the updates can be done less frequently.

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

### interpretation_3

This interpretation has the following description/reasoning:
RUGS takes about one tenth the time to run, making the trade off worth it in all of the tested scenarios.

The LLM has provided the following notes on its reasoning:
Found in Section 4.3. The authors interpret Table 3 to emphasize the computational efficiency and practical value of the RUGS method.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?

- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This interpretation is based on the following analyses: analysis_1
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

Please write the amount of interpretations you had for the study: [3]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;

## Conclusions

The interpretations are used to draw conclusions, which either reflect upon the previous research questions or hypotheses, or yield new research questions or hypotheses.

The LLM has found the following conclusions on the interpretations;

### conclusion_1

This conclusion has the following description/reasoning:
The authors conclude that adding cases affects performance depending on the order of data introduction and distribution changes (RQ1). They conclude that using rolling windows to detect performance decreases effectively mitigates performance loss (RQ2). Finally, they conclude that using random forest feature attributions to update global similarity weights is an effective way to maintain aligned knowledge containers (RQ3). This supports their hypothesis that RUGS allows for less frequent updates while maintaining performance.

The LLM has provided the following notes on this conclusion:
Found in Section 5 (Discussion) and Section 6 (Conclusion), where the authors explicitly summarize their answers to the research questions and confirm the efficacy of their proposed method.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the conclusion?

- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This conclusion is based on the following interpretations: interpretation_1, interpretation_2, interpretation_3
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

This conclusion is to answer (or reflect) upon the following research questions: research_question_1, research_question_2, research_question_3
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

The LLM has found the following suggested research question: Is the RUGS method applicable in a more complex context with more complex real-world datasets?
Please correct the suggestion if wrong (leave empty if correct):

The LLM has provided the following note/location on the suggestion: Section 6 (Conclusion)

The LLM has provided the following reason for the suggestion: Section 6 (Conclusion)

The LLM has linked the suggestion to the following conclusions: conclusion_1
Please correct the IDs if wrong/missing (leave empty if correct):

Please grade the suggestion below:
[X] The LLM has (nearly) perfectly captured a future research direction suggested by our work.
[] The LLM has stated a future research direction that was implied by our work, but not strongly suggested.
[] The LLM has stated a future research direction from our work that is partially correct.
[] The LLM has stated a future research direction that has some overlap with our work but has introduced incorrect or false information.
[] The LLM has stated a future research direction that was not stated or implied in our work; the LLM has hallucinated this information.

#### suggested_research_question_2

The LLM has found the following suggested research question: How does the window size parameter affect performance in more detail, and can it function as a proxy for the sensitivity of the feature weight updates?
Please correct the suggestion if wrong (leave empty if correct):

The LLM has provided the following note/location on the suggestion: Section 6 (Conclusion)

The LLM has provided the following reason for the suggestion: Section 6 (Conclusion)

The LLM has linked the suggestion to the following conclusions: conclusion_1
Please correct the IDs if wrong/missing (leave empty if correct):

Please grade the suggestion below:
[X] The LLM has (nearly) perfectly captured a future research direction suggested by our work.
[] The LLM has stated a future research direction that was implied by our work, but not strongly suggested.
[] The LLM has stated a future research direction from our work that is partially correct.
[] The LLM has stated a future research direction that has some overlap with our work but has introduced incorrect or false information.
[] The LLM has stated a future research direction that was not stated or implied in our work; the LLM has hallucinated this information.

#### suggested_research_question_3

The LLM has found the following suggested research question: How does the RUGS approach compare to more complex baselines?
Please correct the suggestion if wrong (leave empty if correct):

The LLM has provided the following note/location on the suggestion: Section 6 (Conclusion)

The LLM has provided the following reason for the suggestion: Section 6 (Conclusion)

The LLM has linked the suggestion to the following conclusions: conclusion_1
Please correct the IDs if wrong/missing (leave empty if correct):

Please grade the suggestion below:
[X] The LLM has (nearly) perfectly captured a future research direction suggested by our work.
[] The LLM has stated a future research direction that was implied by our work, but not strongly suggested.
[] The LLM has stated a future research direction from our work that is partially correct.
[] The LLM has stated a future research direction that has some overlap with our work but has introduced incorrect or false information.
[] The LLM has stated a future research direction that was not stated or implied in our work; the LLM has hallucinated this information.

#### Suggested Research Questions General

The LLM has provided you with one or more Suggested Research Questions from your work. Is this amount of Suggested Research Questions the same as the amount you specified?

Please write the amount of Suggested Research Questions you had for the study: [3]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;

### Suggested Hypotheses

#### Suggested Hypotheses General

The LLM has provided you with one or more Suggested Hypotheses from your work. Is this amount of Suggested Hypotheses the same as the amount you specified?

Please write the amount of Suggested Hypotheses you had for the study: [0]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;
