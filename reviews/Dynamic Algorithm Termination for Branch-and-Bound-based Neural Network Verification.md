# Automatic Extraction of Study Representation: Dynamic Algorithm Termination for Branch-and-Bound-based Neural Network Verification
*Konstantin Kaulen, Matthias König, Holger H. Hoos*


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

The LLM has found the following **implied** research question:

How can the computational cost of Branch-and-Bound-based neural network verification be reduced by leveraging running time prediction techniques?

The LLM has provided the following reasoning with this research question:

In the Abstract and Introduction, the authors highlight the immense computational resources required for neural network verification and state: 'In this work, we seek to reduce this cost by leveraging running time prediction techniques, thereby allowing for more efficient resource allocation and use.'

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

The LLM has found the following **implied** research question:

What features of branch-and-bound-based neural network verification instances enable reliable predictions about their solvability within a given time budget?

The LLM has provided the following reasoning with this research question:

In the Introduction, the authors list as a primary contribution: 'We present, for the first time, features of branch-and-bound-based neural network verification instances that enable predictions about their solvability within a given time budget'.

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

The authors hypothesise that by using cheaply computable static and dynamic features to dynamically predict solvability, they can terminate unsolvable verification instances early, leading to a substantial reduction in total running time while certifying a comparable number of instances relative to the standard verification procedure.

The LLM has provided the following reasoning with this hypothesis:

In the Abstract, the authors state: 'Overall, using our method, we were able to reduce the total running time by 64% on average compared to the standard verification procedure, while certifying a comparable number of instances.' The Introduction further explains their operationalization of these predictions to avoid spending compute resources on unsolvable instances.

The LLM has linked the hypothesis to the following research questions: research_question_1, research_question_2
Your corrected list (empty if correct):

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

The authors hypothesise that by using cheaply computable static and dynamic features to one can make meaningfully predictions about the running time of a verification algorithm.

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
Evaluating the proposed dynamic algorithm termination method by simulating it on collected performance data from running verification tools (αβ-CROWN, VeriNet, Oval) on various benchmarks. A random forest classifier is trained to predict timeouts at regular checkpoints.

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

The LLM has found the following strategy or protocol for the experiment: 5-fold cross-validation
Your corrected answer (empty if correct):

The LLM has found the following data (sets) used as input for the experiment: ERAN repository (MNIST 5 100, 8 100, Conv Small, Conv Big) (Müller et al. 2022b; Singh et al. 2019a), CIFAR-10 ResNet 2B (Wang et al. 2021), VNN Competition benchmarks (Marabou, Oval21, ViT, SRI ResNet A, CIFAR-100, Tiny ImageNet) (Brix et al. 2023; Müller et al. 2022a; Bak, Liu, and Johnson 2021)
Your corrected answer (empty if correct):

This experiment is used to answer the following research questions: research_question_1
Your corrected list (empty if correct): research_question_1, research_question_2

This experiment is used for the following hypotheses: hypothesis_1
Your corrected list (empty if correct):

### experiment_2

The LLM describes this experiment as follows:
Conducting a feature importance study using Shapley value analysis and a feature ablation study to assess the relevance of the proposed static and dynamic instance features.

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

The LLM has found the following strategy or protocol for the experiment: Shapley value computation on predictions made by the classifiers; Feature ablation by re-running experiments excluding one feature at a time.
Your corrected answer (empty if correct):

The LLM has found the following data (sets) used as input for the experiment: ERAN repository (MNIST 5 100, 8 100, Conv Small, Conv Big) (Müller et al. 2022b; Singh et al. 2019a), CIFAR-10 ResNet 2B (Wang et al. 2021), VNN Competition benchmarks (Marabou, Oval21, ViT, SRI ResNet A, CIFAR-100, Tiny ImageNet) (Brix et al. 2023; Müller et al. 2022a; Bak, Liu, and Johnson 2021)
Your corrected answer (empty if correct):

This experiment is used to answer the following research questions: research_question_2
Your corrected list (empty if correct):

This experiment is used for the following hypotheses: hypothesis_1
Your corrected list (empty if correct):

### experiment_3

The LLM describes this experiment as follows:
Predicting the exact running times of verification instances at the first checkpoint (after 10 seconds) using a random forest regression model to evaluate if features can model exact running times.

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

The LLM has found the following strategy or protocol for the experiment: 5-fold cross-validation
Your corrected answer (empty if correct):

The LLM has found the following data (sets) used as input for the experiment: ERAN repository (MNIST 5 100, 8 100, Conv Small, Conv Big) (Müller et al. 2022b; Singh et al. 2019a), CIFAR-10 ResNet 2B (Wang et al. 2021), VNN Competition benchmarks (Marabou, Oval21, ViT, SRI ResNet A, CIFAR-100, Tiny ImageNet) (Brix et al. 2023; Müller et al. 2022a; Bak, Liu, and Johnson 2021)
Your corrected answer (empty if correct):

This experiment is used to answer the following research questions: research_question_1, research_question_2
Your corrected list (empty if correct):

This experiment is used for the following hypotheses: 
Your corrected list (empty if correct): hypothesis_1


### General Experiment Questions

The LLM has provided you with one or more experiments from your work. Is this amount of experiments the same as the amount you specified?

Please write the amount of experiments you had for the study: [3]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Analysis

The LLM has found one or more analyses that were used to investigate the outcomes of your experiment(s).

### analysis_1

This analysis has the following description/reasoning:
Analyzing the classification performance of the timeout predictor and the overall impact on verification running time and number of solved instances.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the analysis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This analysis is based on the following experiment(s) (outcomes): experiment_1
Your corrected answer (empty if correct): 

#### Metrics list
The measured metrics in this analysis are: Accuracy, True Positive Rate (TPR), False Positive Rate (FPR), Running Time, Number of Solved Instances
Your corrected list (empty if correct): Running Time, Number of Solved Instances

#### Statistics
The statistics for the metrics used are: Mean (averages over five folds), Sum (accumulated over five folds), Percentage of original running time, Difference in solved instances
Your corrected list (empty if correct):

#### Analysis Test

The analysis test is summarised as: Comparison against the standard verification procedure (baseline without early termination).
Your corrected answer (empty if correct):

#### Results

The LLM has found the data of the analysis in the study, which is summarised below. It states either the figures, tables or in text values where it has been found. It describes each with a caption (in case of figure/table), a reason, and subsets of the sets stated before: the metrics used for the analysis, the statistics used, which input data was used, and, which test was applied to reflect upon research questions or confirm/reject hypotheses.

The analysed results were found in the following locations:

- **Tables**:
  - **Table 2**:
    - **caption**:
      - Results for timeout prediction with continuous feature collection in terms of accuracy, true positive and false positive rate as averages over five folds. We display results for θ = 0.99, i.e., the confidence threshold that must be reached before an instance is terminated.
    - **reason**:
      - Shows the classification metrics of the predictor.
    - **metrics**:
      - Accuracy
      - True Positive Rate (TPR)
      - False Positive Rate (FPR)
    - **statistics**:
      - Mean (averages over five folds)
    - **data**:
      - ERAN repository (MNIST 5 100, 8 100, Conv Small, Conv Big) (Müller et al. 2022b; Singh et al. 2019a)
      - CIFAR-10 ResNet 2B (Wang et al. 2021)
      - VNN Competition benchmarks (Marabou, Oval21, ViT, SRI ResNet A, CIFAR-100, Tiny ImageNet) (Brix et al. 2023; Müller et al. 2022a; Bak, Liu, and Johnson 2021)
    - **test**:
      - None
  - **Table 3**:
    - **caption**:
      - Results for dynamic termination of verification queries with θ = 0.99. We display the running time and the number of solved instances accumulated over five folds. In parentheses, we provide the fraction of running time used and the difference in the number of solved instances compared to the standard verification procedure.
    - **reason**:
      - Shows the main results of the dynamic termination method compared to the baseline.
    - **metrics**:
      - Running Time
      - Number of Solved Instances
    - **statistics**:
      - Sum (accumulated over five folds)
      - Percentage of original running time
      - Difference in solved instances
    - **data**:
      - ERAN repository (MNIST 5 100, 8 100, Conv Small, Conv Big) (Müller et al. 2022b; Singh et al. 2019a)
      - CIFAR-10 ResNet 2B (Wang et al. 2021)
      - VNN Competition benchmarks (Marabou, Oval21, ViT, SRI ResNet A, CIFAR-100, Tiny ImageNet) (Brix et al. 2023; Müller et al. 2022a; Bak, Liu, and Johnson 2021)
    - **test**:
      - Comparison against the standard verification procedure
  - **Table 5**:
    - **caption**:
      - Results for dynamic termination of verification queries with θ ∈ {0.5, 0.9}. We display the running time and the number of solved instances accumulated over five folds...
    - **reason**:
      - Shows the trade-off for different confidence thresholds.
    - **metrics**:
      - Running Time
      - Number of Solved Instances
    - **statistics**:
      - Sum (accumulated over five folds)
      - Percentage of original running time
      - Difference in solved instances
    - **data**:
      - ERAN repository (MNIST 5 100, 8 100, Conv Small, Conv Big) (Müller et al. 2022b; Singh et al. 2019a)
      - CIFAR-10 ResNet 2B (Wang et al. 2021)
      - VNN Competition benchmarks (Marabou, Oval21, ViT, SRI ResNet A, CIFAR-100, Tiny ImageNet) (Brix et al. 2023; Müller et al. 2022a; Bak, Liu, and Johnson 2021)
    - **test**:
      - Comparison against the standard verification procedure
- **Figures**:
  - **Figure 2**:
    - **caption**:
      - We display the results of our method to dynamically terminate presumably unsolvable verification instances in terms of running time and the number of solved instances for all choices of the confidence threshold parameter θ between 0.5 and 0.99 with step size 0.01...
    - **reason**:
      - Visualizes the trade-off between running time and solved instances across different thresholds.
    - **metrics**:
      - Running Time
      - Number of Solved Instances
    - **statistics**:
      - Mean (average results over all benchmarks)
    - **data**:
      - ERAN repository (MNIST 5 100, 8 100, Conv Small, Conv Big) (Müller et al. 2022b; Singh et al. 2019a)
      - CIFAR-10 ResNet 2B (Wang et al. 2021)
      - VNN Competition benchmarks (Marabou, Oval21, ViT, SRI ResNet A, CIFAR-100, Tiny ImageNet) (Brix et al. 2023; Müller et al. 2022a; Bak, Liu, and Johnson 2021)
    - **test**:
      - None
- **Text**:
  - **Section Results and Discussion**:
    - **value**:
      - On average, our classifier correctly identified 84% of timeouts while incorrectly classifying 5% of solvable instances... On average, our approach solved comparably many instances in 36% of the original running time.
    - **reason**:
      - Summarizes the main findings of the classification and termination performance.
    - **metrics**:
      - True Positive Rate (TPR)
      - False Positive Rate (FPR)
      - Running Time
    - **statistics**:
      - Mean
    - **data**:
      - ERAN repository (MNIST 5 100, 8 100, Conv Small, Conv Big) (Müller et al. 2022b; Singh et al. 2019a)
      - CIFAR-10 ResNet 2B (Wang et al. 2021)
      - VNN Competition benchmarks (Marabou, Oval21, ViT, SRI ResNet A, CIFAR-100, Tiny ImageNet) (Brix et al. 2023; Müller et al. 2022a; Bak, Liu, and Johnson 2021)
    - **test**:
      - Comparison against the standard verification procedure

> NOT table 2
> NOT table 5
> NOT figure 2


#### General

The LLM has overall captured the analysis details...

[] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[X] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)

### analysis_2

This analysis has the following description/reasoning:
Analyzing the Shapley values to determine which features contribute most to the predictions.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the analysis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason: Analyzing the Shapley values to determine which features contribute most to the predictions at which point time.

This analysis is based on the following experiment(s) (outcomes): experiment_2
Your corrected answer (empty if correct): 

#### Metrics list
The measured metrics in this analysis are: Shapley value (impact on model output)
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Distribution (boxplots)
Your corrected list (empty if correct):

#### Analysis Test

The analysis test is summarised as: Comparison of feature importance (larger Shapley values indicate higher importance).
Your corrected answer (empty if correct):

#### Results

The LLM has found the data of the analysis in the study, which is summarised below. It states either the figures, tables or in text values where it has been found. It describes each with a caption (in case of figure/table), a reason, and subsets of the sets stated before: the metrics used for the analysis, the statistics used, which input data was used, and, which test was applied to reflect upon research questions or confirm/reject hypotheses.

The analysed results were found in the following locations:

- **Tables**:
- **Figures**:
  - **Figure 3**:
    - **caption**:
      - Shapley Values of all features our method employs to predict whether problem instances verified by αβ-CROWN will be solved within the remaining compute budget...
    - **reason**:
      - Shows feature importance for αβ-CROWN.
    - **metrics**:
      - Shapley value (impact on model output)
    - **statistics**:
      - Distribution (boxplots)
    - **data**:
      - ERAN repository (MNIST 5 100, 8 100, Conv Small, Conv Big) (Müller et al. 2022b; Singh et al. 2019a)
      - CIFAR-10 ResNet 2B (Wang et al. 2021)
      - VNN Competition benchmarks (Marabou, Oval21, ViT, SRI ResNet A, CIFAR-100, Tiny ImageNet) (Brix et al. 2023; Müller et al. 2022a; Bak, Liu, and Johnson 2021)
    - **test**:
      - Comparison of feature importance
  - **Figure 4**:
    - **caption**:
      - Shapley Values of all features our method employs to predict whether problem instances verified by VeriNet will be solved within the remaining compute budget...
    - **reason**:
      - Shows feature importance for VeriNet.
    - **metrics**:
      - Shapley value (impact on model output)
    - **statistics**:
      - Distribution (boxplots)
    - **data**:
      - ERAN repository (MNIST 5 100, 8 100, Conv Small, Conv Big) (Müller et al. 2022b; Singh et al. 2019a)
      - CIFAR-10 ResNet 2B (Wang et al. 2021)
      - VNN Competition benchmarks (Marabou, Oval21, ViT, SRI ResNet A, CIFAR-100, Tiny ImageNet) (Brix et al. 2023; Müller et al. 2022a; Bak, Liu, and Johnson 2021)
    - **test**:
      - Comparison of feature importance
  - **Figure 5**:
    - **caption**:
      - Shapley Values of all features our method employs to predict whether problem instances verified by Oval will be solved within the remaining compute budget...
    - **reason**:
      - Shows feature importance for Oval.
    - **metrics**:
      - Shapley value (impact on model output)
    - **statistics**:
      - Distribution (boxplots)
    - **data**:
      - ERAN repository (MNIST 5 100, 8 100, Conv Small, Conv Big) (Müller et al. 2022b; Singh et al. 2019a)
      - CIFAR-10 ResNet 2B (Wang et al. 2021)
      - VNN Competition benchmarks (Marabou, Oval21, ViT, SRI ResNet A, CIFAR-100, Tiny ImageNet) (Brix et al. 2023; Müller et al. 2022a; Bak, Liu, and Johnson 2021)
    - **test**:
      - Comparison of feature importance
- **Text**:
  - **Section Results**:
    - **value**:
      - Overall, our analysis revealed that all of our novel features impacted the predictions of our classification models. Primarily, BaB tree characteristics were the most important features across all considered verification systems and benchmarks.
    - **reason**:
      - Summarizes the findings of the feature importance study.
    - **metrics**:
      - Shapley value (impact on model output)
    - **statistics**:
    - **data**:
      - ERAN repository (MNIST 5 100, 8 100, Conv Small, Conv Big) (Müller et al. 2022b; Singh et al. 2019a)
      - CIFAR-10 ResNet 2B (Wang et al. 2021)
      - VNN Competition benchmarks (Marabou, Oval21, ViT, SRI ResNet A, CIFAR-100, Tiny ImageNet) (Brix et al. 2023; Müller et al. 2022a; Bak, Liu, and Johnson 2021)
    - **test**:
      - Comparison of feature importance


#### General

The LLM has overall captured the analysis details...

[] Very well (No major mistakes and/or missing information)
[X] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)

### analysis_3

This analysis has the following description/reasoning:
Analyzing the performance of the running time regression model.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the analysis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This analysis is based on the following experiment(s) (outcomes): experiment_3
Your corrected answer (empty if correct): 

#### Metrics list
The measured metrics in this analysis are: Root Mean Squared Error (RMSE), R2 score (R2), Spearman Rank Correlation (ρ)
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Mean (averages over five folds)
Your corrected list (empty if correct):

#### Analysis Test

The analysis test is summarised as: Comparison of predicted vs true running times.
Your corrected answer (empty if correct):

#### Results

The LLM has found the data of the analysis in the study, which is summarised below. It states either the figures, tables or in text values where it has been found. It describes each with a caption (in case of figure/table), a reason, and subsets of the sets stated before: the metrics used for the analysis, the statistics used, which input data was used, and, which test was applied to reflect upon research questions or confirm/reject hypotheses.

The analysed results were found in the following locations:

- **Tables**:
  - **Table 6**:
    - **caption**:
      - Results for the running time regression task as averages over five folds in terms of root mean squared error (RMSE), R2 score (R2) and Spearman Rank Correlation (ρ)...
    - **reason**:
      - Shows the regression metrics.
    - **metrics**:
      - Root Mean Squared Error (RMSE)
      - R2 score (R2)
      - Spearman Rank Correlation (ρ)
    - **statistics**:
      - Mean (averages over five folds)
    - **data**:
      - ERAN repository (MNIST 5 100, 8 100, Conv Small, Conv Big) (Müller et al. 2022b; Singh et al. 2019a)
      - CIFAR-10 ResNet 2B (Wang et al. 2021)
      - VNN Competition benchmarks (Marabou, Oval21, ViT, SRI ResNet A, CIFAR-100, Tiny ImageNet) (Brix et al. 2023; Müller et al. 2022a; Bak, Liu, and Johnson 2021)
    - **test**:
      - None
- **Figures**:
  - **Figure 6**:
    - **caption**:
      - Scatter plots of the predictions yielded by our running time regression approach (see Appendix ) against true running times.
    - **reason**:
      - Visualizes the correlation between predicted and true running times.
    - **metrics**:
      - Predicted running time
      - True running time
    - **statistics**:
    - **data**:
      - ERAN repository (MNIST 5 100, 8 100, Conv Small, Conv Big) (Müller et al. 2022b; Singh et al. 2019a)
      - CIFAR-10 ResNet 2B (Wang et al. 2021)
      - VNN Competition benchmarks (Marabou, Oval21, ViT, SRI ResNet A, CIFAR-100, Tiny ImageNet) (Brix et al. 2023; Müller et al. 2022a; Bak, Liu, and Johnson 2021)
    - **test**:
      - Comparison of predicted vs true running times
- **Text**:
  - **Section Running Time Regression**:
    - **value**:
      - Overall, we found that the best results across all experiments and verifiers were achieved on the 5 100 and 8 100 benchmarks for αβ-CROWN... While these results are promising, they did not generalise well enough for meaningful application.
    - **reason**:
      - Summarizes the regression performance.
    - **metrics**:
      - Root Mean Squared Error (RMSE)
      - R2 score (R2)
      - Spearman Rank Correlation (ρ)
    - **statistics**:
      - Mean
    - **data**:
      - ERAN repository (MNIST 5 100, 8 100, Conv Small, Conv Big) (Müller et al. 2022b; Singh et al. 2019a)
      - CIFAR-10 ResNet 2B (Wang et al. 2021)
      - VNN Competition benchmarks (Marabou, Oval21, ViT, SRI ResNet A, CIFAR-100, Tiny ImageNet) (Brix et al. 2023; Müller et al. 2022a; Bak, Liu, and Johnson 2021)
    - **test**:
      - None


#### General

The LLM has overall captured the analysis details...

[X] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)


### General Analysis Questions

The LLM has provided you with one or more analyses from your work. Is this amount of analyses the same as the amount you specified?

Please write the amount of analyses you had for the study: [6]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;
- A4: The sensitivity study table 5, figure 2 for different theta values
- A5: Classifier preformance analysis in table 2
- A6: Classifier training time analysis figure 1


## Interpretation

Experiment outcomes are analysed and interpreted to determine whether the experiment supports the hypothesis or not. 

The LLM has found the following interpretations of the experiment outcomes;

### interpretation_1

This interpretation has the following description/reasoning:
The authors interpret that their method obtains very high TPR scores while maintaining a FPR close to 0 for most verifiers and benchmarks, leading to substantial speed-ups (saving 64% of running time on average) with only a small amount of solvable instances terminated prematurely.

The LLM has provided the following notes on its reasoning:
Based on the Results and Discussion section, where they state 'We obtained very high TPR scores while maintaining a FPR close to 0... we obtained substantial speed-ups, while only a small amount of solvable instances was terminated prematurely.'

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This interpretation is based on the following analyses: analysis_1
Your corrected answer (empty if correct): analysis_1, analysis_5

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
The authors interpret that dynamic features capturing BaB tree characteristics are the most important features across all verification systems, while static features from incomplete methods are mainly important during the early stages of verification.

The LLM has provided the following notes on its reasoning:
Based on the Results section for the feature importance study: 'Primarily, BaB tree characteristics were the most important features across all considered verification systems and benchmarks... the features that capture the results of the incomplete verification methods were important only during the beginning of the verification procedure'.

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

### interpretation_3

This interpretation has the following description/reasoning:
The authors interpret that while running time regression shows promising results on specific benchmarks (e.g., fully-connected networks for αβ-CROWN), it does not generalize well enough across all benchmarks for meaningful application.

The LLM has provided the following notes on its reasoning:
Based on the Running Time Regression section: 'While these results are promising, they did not generalise well enough for meaningful application.'

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This interpretation is based on the following analyses: analysis_3
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

Please write the amount of interpretations you had for the study: [4]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;
- Theta as a trade off parameter between number of solved instances and saved running time (Appendix, interpret of fig 2)

## Conclusions

The interpretations are used to draw conclusions, which either reflect upon the previous research questions or hypotheses, or yield new research questions or hypotheses.

The LLM has found the following conclusions on the interpretations;

### conclusion_1

This conclusion has the following description/reasoning:
The authors conclude that their dynamic algorithm termination method successfully reduces the computational resources demanded by neural network robustness verification. By identifying and terminating unsolvable instances early using the proposed features, the method accelerates the verification procedure by 64% on average while certifying a comparable number of instances.

The LLM has provided the following notes on this conclusion:
Based on the Conclusions and Future Work section: 'In this study, we have, for the first time, shown that the computational resources demanded by neural network robustness verification can be greatly reduced... we showed that our method accelerates the verification procedure by 64% on average compared to the current state-of-the-art approach...'

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

The LLM has found the following suggested research question: Can the proposed features and dynamic termination approach be applied in other contexts, such as algorithm selection or satisfiability prediction?
Please correct the suggestion if wrong (leave empty if correct):

The LLM has provided the following note/location on the suggestion: Conclusions and Future Work section

The LLM has provided the following reason for the suggestion: Conclusions and Future Work section

The LLM has linked the suggestion to the following conclusions: conclusion_1
Please correct the IDs if wrong/missing (leave empty if correct):

Please grade the suggestion below:
[X] The LLM has (nearly) perfectly captured a future research direction suggested by our work.
[] The LLM has stated a future research direction that was implied by our work, but not strongly suggested.
[] The LLM has stated a future research direction from our work that is partially correct.
[] The LLM has stated a future research direction that has some overlap with our work but has introduced incorrect or false information.
[] The LLM has stated a future research direction that was not stated or implied in our work; the LLM has hallucinated this information.

#### suggested_research_question_2

The LLM has found the following suggested research question: Can the running time prediction capabilities of the proposed features enable empirical scaling models of BaB-based verification?
Please correct the suggestion if wrong (leave empty if correct):

The LLM has provided the following note/location on the suggestion: Conclusions and Future Work section

The LLM has provided the following reason for the suggestion: Conclusions and Future Work section

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

Please write the amount of Suggested Research Questions you had for the study: [2]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


### Suggested Hypotheses

#### suggested_hypothesis_1

The LLM has found the following suggested hypothesis: The authors hypothesise that their dynamic termination approach can be successfully extended to further BaB-based verification approaches, such as MN-BaB.
Please correct the suggestion if wrong (leave empty if correct):

The LLM has provided the following note/location on the suggestion: Conclusions and Future Work section

The LLM has provided the following reason for the suggestion: The authors state: 'In future work, we seek to extend our approach to further BaB-based verification approaches (e.g., MN-BaB).'

The LLM has linked the suggestion to the following conclusions: conclusion_1
Please correct the IDs if wrong/missing (leave empty if correct):

Please grade the suggestion below:
[X] The LLM has (nearly) perfectly captured a future research direction suggested by our work.
[] The LLM has stated a future research direction that was implied by our work, but not strongly suggested.
[] The LLM has stated a future research direction from our work that is partially correct.
[] The LLM has stated a future research direction that has some overlap with our work but has introduced incorrect or false information.
[] The LLM has stated a future research direction that was not stated or implied in our work; the LLM has hallucinated this information.


#### Suggested Hypotheses General

The LLM has provided you with one or more Suggested Hypotheses from your work. Is this amount of Suggested Hypotheses the same as the amount you specified?

Please write the amount of Suggested Hypotheses you had for the study: [1]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;
