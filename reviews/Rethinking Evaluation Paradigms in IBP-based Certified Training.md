# Automatic Extraction of Study Representation: Rethinking Evaluation Paradigms in IBP-based Certified Training
*Konstantin Kaulen, Hadar Shavit, Holger H. Hoos*


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

How does the common practice of reporting a single hyperparameter configuration affect the assessment of the state of the art in certified training, given the inherent trade-off between natural and certified accuracy?

The LLM has provided the following reasoning with this research question:

Implied in the Abstract and Section 1 (Introduction). The authors state that because natural and certified accuracy are inherently conflicting, reporting a single configuration is problematic and can mislead conclusions about overall performance. They motivate their study by addressing this issue via Pareto front comparisons.

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

Which hyperparameters and their interactions most strongly influence the trade-off between certified and natural accuracy in IBP-based certified training?

The LLM has provided the following reasoning with this research question:

Implied in Section 6 (Hyperparameter Importance Analysis). The authors state: 'We analysed which hyperparameters most strongly influence certified and natural accuracy, in order to explain why the discovered configurations outperform previously reported ones, and to derive actionable insights for the certified training community.'

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

The authors hypothesise that evaluating certified training methods via Pareto fronts over the complete natural-certified accuracy trade-off space, discovered through automated multi-objective hyperparameter optimisation, provides a fairer and more accurate assessment of the state of the art than single-configuration comparisons, and will uncover substantial undertuning in previously reported configurations.

The LLM has provided the following reasoning with this hypothesis: 

Implied in the Abstract and Section 4. The authors propose this paradigm change and expect that it will reveal that prior advancements are less pronounced than assumed and that older methods were undertuned.

The LLM has linked the hypothesis to the following research questions: research_question_1
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

The authors hypothesise that evaluating certified training methods via Pareto fronts over the complete natural-certified accuracy trade-off space, discovered through automated multi-objective hyperparameter optimisation, provides a fairer and more accurate assessment of the state of the art than single-configuration comparisons.

### hypothesis_2

The LLM has found the following **implied** hypothesis:

The authors hypothesise that the trade-off between clean and certified performance is governed by complex interactions between multiple hyperparameters that can only be uncovered using state-of-the-art multi-objective Bayesian hyperparameter optimisation methods.

The LLM has provided the following reasoning with this hypothesis:

Implied in Section 1 (Introduction) and Section 7 (Discussion). The authors state that the trade-off is governed by complex interactions that could only be uncovered using their proposed methods, implying this was their expectation when conducting the hyperparameter importance analysis.

The LLM has linked the hypothesis to the following research questions: research_question_2
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

Please write the amount of hypothesis you had for the study: [2]

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
Evaluating IBP, CROWN-IBP, SABR, and MTL-IBP using multi-objective Bayesian hyperparameter optimization to discover Pareto fronts of natural vs. certified accuracy, and comparing these fronts against previously reported single configurations.

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

The LLM has found the following strategy or protocol for the experiment: Multi-objective Bayesian optimization (BoTorch/Optuna) with Gaussian process surrogate and EHVI acquisition function. 100 trials per seed, 3 pseudo-random seeds per benchmark. Complete verification using alpha-beta-CROWN with a 1000s cutoff.
Your corrected answer (empty if correct): Multi-objective Bayesian optimization (BoTorch/Optuna) with Gaussian process surrogate and EHVI acquisition function. 100 trials per seed and 3 pseudo-random seeds per benchmark to determine the pareto front (Not for statistical tests, optimisation budget). Complete verification using alpha-beta-CROWN with a 1000s cutoff.

The LLM has found the following data (sets) used as input for the experiment: CIFAR-10 (Dosovitskiy et al., 2021), Tiny ImageNet (Le & Yang, 2015), MNIST (LeCun, 1998)
Your corrected answer (empty if correct):

This experiment is used to answer the following research questions: research_question_1
Your corrected list (empty if correct):

This experiment is used for the following hypotheses: hypothesis_1
Your corrected list (empty if correct):

### experiment_2

The LLM describes this experiment as follows:
Analyzing the importance of individual hyperparameters on certified and natural accuracy to explain performance improvements and derive actionable insights.

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

The LLM has found the following strategy or protocol for the experiment: fANOVA (functional Analysis of Variance) applied to the optimization procedure results to quantify the fraction of variance in predicted performance attributed to each hyperparameter.
Your corrected answer (empty if correct):

The LLM has found the following data (sets) used as input for the experiment: CIFAR-10 (Dosovitskiy et al., 2021), Tiny ImageNet (Le & Yang, 2015)
Your corrected answer (empty if correct):

This experiment is used to answer the following research questions: research_question_2
Your corrected list (empty if correct):

This experiment is used for the following hypotheses: hypothesis_2
Your corrected list (empty if correct):

### experiment_3

The LLM describes this experiment as follows:
Assessing the impact of tuning directly on the evaluation set by comparing Pareto fronts obtained via validation set tuning versus test set tuning.

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

The LLM has found the following strategy or protocol for the experiment: Rerunning multi-objective hyperparameter optimization on a randomly selected validation set comprising 20% of the train set, and evaluating performance on the test set.
Your corrected answer (empty if correct):

The LLM has found the following data (sets) used as input for the experiment: CIFAR-10 (Dosovitskiy et al., 2021)
Your corrected answer (empty if correct):

This experiment is used to answer the following research questions: research_question_1
Your corrected list (empty if correct):

This experiment is used for the following hypotheses: hypothesis_1
Your corrected list (empty if correct):

### experiment_4

The LLM describes this experiment as follows:
Studying the effect of reduced optimization trials and verification timeouts on the resulting Pareto fronts to analyze computational costs and efficiency.

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

The LLM has found the following strategy or protocol for the experiment: Varying complete verification cutoff times (e.g., 100s, 250s, 500s, 1000s) and varying evaluation budgets (10, 20, 50, 75, 100 trials per seed) to observe the impact on the Pareto front and hypervolume.
Your corrected answer (empty if correct):

The LLM has found the following data (sets) used as input for the experiment: CIFAR-10 (Dosovitskiy et al., 2021), Tiny ImageNet (Le & Yang, 2015)
Your corrected answer (empty if correct):

This experiment is used to answer the following research questions: research_question_1
Your corrected list (empty if correct):

This experiment is used for the following hypotheses: hypothesis_1
Your corrected list (empty if correct):


### General Experiment Questions

The LLM has provided you with one or more experiments from your work. Is this amount of experiments the same as the amount you specified?

Please write the amount of experiments you had for the study: [4]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Analysis

The LLM has found one or more analyses that were used to investigate the outcomes of your experiment(s).

### analysis_1

This analysis has the following description/reasoning:
Comparing the discovered Pareto fronts of different certified training methods against each other and against previously reported single configurations from the literature to assess the true state of the art.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the analysis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This analysis is based on the following experiment(s) (outcomes): experiment_1
Your corrected answer (empty if correct):

#### Metrics list
The measured metrics in this analysis are: Clean accuracy, Certified accuracy
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Pareto fronts (sets of non-dominated configurations)
Your corrected list (empty if correct):

#### Analysis Test

The analysis test is summarised as: Pareto dominance (visual comparison of fronts and tabular comparison of specific points)
Your corrected answer (empty if correct):

#### Results

The LLM has found the data of the analysis in the study, which is summarised below. It states either the figures, tables or in text values where it has been found. It describes each with a caption (in case of figure/table), a reason, and subsets of the sets stated before: the metrics used for the analysis, the statistics used, which input data was used, and, which test was applied to reflect upon research questions or confirm/reject hypotheses.

The analysed results were found in the following locations:

- **Tables**:
  - **Table 1**:
    - **caption**:
      - Comparison of the results reported from the literature to the results achieved by using our novel optimisation procedure. For each result from the literature, we selected a configuration from the Pareto front that achieves similar or better performance. Boldface marks results surpassing prior work; underlined values indicate similar performance (±0.5). Our method typically yields configurations with higher clean accuracy and, in many cases, improved certified accuracy.
    - **reason**:
      - Shows the direct numerical comparison between the literature's single configurations and the Pareto-optimal configurations found in Experiment 1.
    - **metrics**:
      - Clean accuracy
      - Certified accuracy
    - **statistics**:
      - Pareto fronts (sets of non-dominated configurations)
    - **data**:
      - CIFAR-10 (Dosovitskiy et al., 2021)
      - Tiny ImageNet (Le & Yang, 2015)
    - **test**:
      - Pareto dominance (visual comparison of fronts and tabular comparison of specific points)
  - **Table 2**:
    - **caption**:
      - Comparison of the results reported from the literature to the results achieved by using our novel evaluation procedure on MNIST with ϵ = 0.3. For each result from the literature, we selected a configuration from the Pareto front that achieves similar or better performance. Boldface marks results surpassing prior work; underlined values indicate similar performance (±0.5).
    - **reason**:
      - Shows the direct numerical comparison for the MNIST dataset.
    - **metrics**:
      - Clean accuracy
      - Certified accuracy
    - **statistics**:
      - Pareto fronts (sets of non-dominated configurations)
    - **data**:
      - MNIST (LeCun, 1998)
    - **test**:
      - Pareto dominance (visual comparison of fronts and tabular comparison of specific points)
- **Figures**:
  - **Figure 2**:
    - **caption**:
      - Comparison of Pareto fronts from our novel evaluation procedure on CIFAR-10 with (a) ϵ = 2/255, (b) ϵ = 8/255 and Tiny ImageNet with (c) ϵ = 1/255. The fronts enable a nuanced assessment, showing, e.g., that IBP is state of the art in (b) when prioritising natural accuracy and that SABR and MTL-IBP are complementary in (c) and, to a lesser extent, in (a).
    - **reason**:
      - Visually demonstrates the Pareto fronts of all methods to assess the combined state of the art.
    - **metrics**:
      - Clean accuracy
      - Certified accuracy
    - **statistics**:
      - Pareto fronts (sets of non-dominated configurations)
    - **data**:
      - CIFAR-10 (Dosovitskiy et al., 2021)
      - Tiny ImageNet (Le & Yang, 2015)
    - **test**:
      - Pareto dominance (visual comparison of fronts and tabular comparison of specific points)
  - **Figure 3**:
    - **caption**:
      - Results for CIFAR-10 for ϵ = 2/255 are shown in (a)-(d), for ϵ = 8/255 in (e)-(h), and for Tiny ImageNet for ϵ = 1/255 in (i)-(l). We compare Pareto fronts obtained using our evaluation to results given in the original publications and CTBench (Mao et al., 2025).
    - **reason**:
      - Visually demonstrates that the newly discovered Pareto fronts dominate the previously reported single configurations.
    - **metrics**:
      - Clean accuracy
      - Certified accuracy
    - **statistics**:
      - Pareto fronts (sets of non-dominated configurations)
    - **data**:
      - CIFAR-10 (Dosovitskiy et al., 2021)
      - Tiny ImageNet (Le & Yang, 2015)
    - **test**:
      - Pareto dominance (visual comparison of fronts and tabular comparison of specific points)
- **Text**:
  - **Section 5**:
    - **value**:
      - In nearly all scenarios, the results from the literature are Pareto-dominated by the configurations uncovered using our novel evaluation approach. Most notably, on CIFAR-10 with ϵ = 2/255, SABR achieves a gain of more than 1% in terms of clean and certified accuracy, surpassing prior results known for this benchmark.
    - **reason**:
      - Summarizes the findings of the Pareto dominance analysis.
    - **metrics**:
      - Clean accuracy
      - Certified accuracy
    - **statistics**:
      - Pareto fronts (sets of non-dominated configurations)
    - **data**:
      - CIFAR-10 (Dosovitskiy et al., 2021)
    - **test**:
      - Pareto dominance (visual comparison of fronts and tabular comparison of specific points)


#### General

The LLM has overall captured the analysis details...

[X] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)

### analysis_2

This analysis has the following description/reasoning:
Identifying which hyperparameters drive the performance improvements and trade-offs using fANOVA.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the analysis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This analysis is based on the following experiment(s) (outcomes): experiment_2
Your corrected answer (empty if correct): 

#### Metrics list
The measured metrics in this analysis are: Hyperparameter importance score (fraction of variance)
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Importance scores
Your corrected list (empty if correct):

#### Analysis Test

The analysis test is summarised as: fANOVA variance attribution
Your corrected answer (empty if correct):

#### Results

The LLM has found the data of the analysis in the study, which is summarised below. It states either the figures, tables or in text values where it has been found. It describes each with a caption (in case of figure/table), a reason, and subsets of the sets stated before: the metrics used for the analysis, the statistics used, which input data was used, and, which test was applied to reflect upon research questions or confirm/reject hypotheses.

The analysed results were found in the following locations:

- **Tables**:
- **Figures**:
  - **Figure 13**:
    - **caption**:
      - Parallel coordinates plot for the hyperparameter optimisation of IBP on CIFAR-10 ((a)-(d)) and Tiny ImageNet ((e)-(f)). In each plot, we show the five most important parameters with their importance scores for one of the two objectives along with the parameter values of configurations in the Pareto set.
    - **reason**:
      - Shows the fANOVA importance scores and parameter interactions for IBP.
    - **metrics**:
      - Hyperparameter importance score (fraction of variance)
    - **statistics**:
      - Importance scores
    - **data**:
      - CIFAR-10 (Dosovitskiy et al., 2021)
      - Tiny ImageNet (Le & Yang, 2015)
    - **test**:
      - fANOVA variance attribution
- **Text**:
  - **Section 6**:
    - **value**:
      - Our analysis revealed that IBP yields stronger trade-offs when more time is spent on optimising for clean cross-entropy loss than done in related work. This is exemplified in κstart and κend being highly important parameters across all scenarios, often taking larger values and interacting with longer ramp- and warm-up phases than used previously.
    - **reason**:
      - Describes the specific hyperparameter interactions uncovered by the fANOVA analysis.
    - **metrics**:
      - Hyperparameter importance score (fraction of variance)
    - **statistics**:
      - Importance scores
    - **data**:
      - CIFAR-10 (Dosovitskiy et al., 2021)
    - **test**:
      - fANOVA variance attribution

> Also: Figure 14, 15, 16

#### General

The LLM has overall captured the analysis details...

[] Very well (No major mistakes and/or missing information)
[X] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)

### analysis_3

This analysis has the following description/reasoning:
Determining if prior works overestimated generalization performance by tuning on the test set.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the analysis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This analysis is based on the following experiment(s) (outcomes): experiment_3
Your corrected answer (empty if correct): 

#### Metrics list
The measured metrics in this analysis are: Clean accuracy, Certified accuracy
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Pareto fronts (sets of non-dominated configurations)
Your corrected list (empty if correct):

#### Analysis Test

The analysis test is summarised as: Pareto dominance
Your corrected answer (empty if correct):

#### Results

The LLM has found the data of the analysis in the study, which is summarised below. It states either the figures, tables or in text values where it has been found. It describes each with a caption (in case of figure/table), a reason, and subsets of the sets stated before: the metrics used for the analysis, the statistics used, which input data was used, and, which test was applied to reflect upon research questions or confirm/reject hypotheses.

The analysed results were found in the following locations:

- **Tables**:
- **Figures**:
  - **Figure 4**:
    - **caption**:
      - Comparison of Pareto fronts on CIFAR-10 with ϵ = 2/255, obtained using incomplete verification when hyperparameters are tuned on a validation set versus directly on the test set. In all cases, validation-tuned Pareto fronts are strictly dominated by those obtained via test-set tuning, indicating that prior evaluations overestimate generalisation performance.
    - **reason**:
      - Visually demonstrates the performance gap between validation-tuned and test-tuned configurations.
    - **metrics**:
      - Clean accuracy
      - Certified accuracy
    - **statistics**:
      - Pareto fronts (sets of non-dominated configurations)
    - **data**:
      - CIFAR-10 (Dosovitskiy et al., 2021)
    - **test**:
      - Pareto dominance
- **Text**:
  - **Section 5**:
    - **value**:
      - Perhaps unsurprisingly, the Pareto fronts yielded through validation set tuning were always strictly dominated by those obtained when tuning on the test set directly. Interestingly, the fronts exhibited visually similar shapes, indicating that, while absolute performance degrades, relative performance characteristics may remain unchanged.
    - **reason**:
      - Summarizes the findings of the validation vs test set tuning analysis.
    - **metrics**:
      - Clean accuracy
      - Certified accuracy
    - **statistics**:
      - Pareto fronts (sets of non-dominated configurations)
    - **data**:
      - CIFAR-10 (Dosovitskiy et al., 2021)
    - **test**:
      - Pareto dominance

> Also Figure 8 in the appendix

#### General

The LLM has overall captured the analysis details...

[X] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)

### analysis_4

This analysis has the following description/reasoning:
Evaluating if the proposed multi-objective HPO is computationally tractable and how budget reductions affect the quality of the Pareto front.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the analysis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This analysis is based on the following experiment(s) (outcomes): experiment_4
Your corrected answer (empty if correct): 

#### Metrics list
The measured metrics in this analysis are: Hypervolume improvement, Verification time (hours/seconds)
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Total time, Average time, Hypervolume relative improvement
Your corrected list (empty if correct):

#### Analysis Test

The analysis test is summarised as: Comparison of hypervolumes and visual front shifts
Your corrected answer (empty if correct):

#### Results

The LLM has found the data of the analysis in the study, which is summarised below. It states either the figures, tables or in text values where it has been found. It describes each with a caption (in case of figure/table), a reason, and subsets of the sets stated before: the metrics used for the analysis, the statistics used, which input data was used, and, which test was applied to reflect upon research questions or confirm/reject hypotheses.

The analysed results were found in the following locations:

- **Tables**:
  - **Table 8**:
    - **caption**:
      - Hypervolume Improvement with respect to the number of trials used per seed during the multi-objective hyperparameter optimisation. In parentheses, we display the relative improvement to the previous point.
    - **reason**:
      - Quantifies the improvement of the Pareto front as the optimization budget increases.
    - **metrics**:
      - Hypervolume improvement
    - **statistics**:
      - Hypervolume relative improvement
    - **data**:
      - CIFAR-10 (Dosovitskiy et al., 2021)
      - Tiny ImageNet (Le & Yang, 2015)
    - **test**:
      - Comparison of hypervolumes and visual front shifts
- **Figures**:
  - **Figure 11**:
    - **caption**:
      - Evolution of the Pareto fronts of MTL-IBP, SABR, CROWN-IBP and IBP with varying cutoff times for complete verification. It becomes apparent that on CIFAR-10 cutoff times of 100s are sufficient to identify Pareto fronts and on Tiny ImageNet only 250s are required.
    - **reason**:
      - Visually demonstrates that lower verification timeouts do not significantly degrade the discovered Pareto fronts.
    - **metrics**:
      - Verification time (hours/seconds)
    - **statistics**:
      - Total time
      - Average time
    - **data**:
      - CIFAR-10 (Dosovitskiy et al., 2021)
      - Tiny ImageNet (Le & Yang, 2015)
    - **test**:
      - Comparison of hypervolumes and visual front shifts
- **Text**:
  - **Section 5**:
    - **value**:
      - For example, the total verification time of MTL-IBP and SABR on CIFAR-10 with ϵ = 2/255 decreased from 1311 to 208 hours and from 1585 to 227 hours, respectively. On Tiny ImageNet, slightly larger timeouts of 250 s were required to maintain identical fronts.
    - **reason**:
      - Provides concrete numbers on the computational savings achieved by reducing verification timeouts.
    - **metrics**:
      - Verification time (hours/seconds)
    - **statistics**:
      - Total time
    - **data**:
      - CIFAR-10 (Dosovitskiy et al., 2021)
      - Tiny ImageNet (Le & Yang, 2015)
    - **test**:
      - Comparison of hypervolumes and visual front shifts

> Also figure 12, 

#### General

The LLM has overall captured the analysis details...

[] Very well (No major mistakes and/or missing information)
[X] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)


### General Analysis Questions

The LLM has provided you with one or more analyses from your work. Is this amount of analyses the same as the amount you specified?

Please write the amount of analyses you had for the study: [4]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Interpretation

Experiment outcomes are analysed and interpreted to determine whether the experiment supports the hypothesis or not. 

The LLM has found the following interpretations of the experiment outcomes;

### interpretation_1

This interpretation has the following description/reasoning:
In nearly all scenarios, the results from the literature are Pareto-dominated by the configurations uncovered using our novel evaluation approach... Furthermore, we show that there is no single certified training method that uniformly achieves state of the art performance; instead, methods are complementary, with SABR generally excelling at high natural accuracy and MTL-IBP delivering stronger certified guarantees.

The LLM has provided the following notes on its reasoning:
The authors interpret the Pareto fronts as showing that prior methods were undertuned and that different methods excel at different parts of the trade-off space, refuting the idea of a single 'best' method.

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

### interpretation_2

This interpretation has the following description/reasoning:
Our analysis revealed that IBP yields stronger trade-offs when more time is spent on optimising for clean cross-entropy loss than done in related work... the trade-off between clean and certified performance is influenced by a sizeable set of interacting hyperparameters – including, but not limited to, method-specific trade-off parameters.

The LLM has provided the following notes on its reasoning:
The authors interpret the fANOVA results to explain why their configurations beat the literature, highlighting the importance of previously overlooked hyperparameters like the length of warm-up phases and the κ parameter.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason: The trade-off between clean and certified performance is influenced by a sizeable set of interacting hyperparameters – including, but not limited to, method-specific trade-off parameters.

This interpretation is based on the following analyses: analysis_2
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
These results demonstrate that previous evaluations substantially overestimated performance and do not accurately reflect the generalisation capabilities of IBP-based certified training.

The LLM has provided the following notes on its reasoning:
The authors interpret the gap between validation-tuned and test-tuned fronts as evidence of overfitting in prior literature, emphasizing the need for proper validation splits.

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

### interpretation_4

This interpretation has the following description/reasoning:
Overall, these results suggest that verification times can be reduced substantially with little impact on the final Pareto fronts, whereas reducing the optimisation budget is considerably more detrimental to their quality.

The LLM has provided the following notes on its reasoning:
The authors interpret the cost analysis to provide practical recommendations for running their evaluation protocol, showing it can be made more efficient.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This interpretation is based on the following analyses: analysis_4
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

## Conclusions

The interpretations are used to draw conclusions, which either reflect upon the previous research questions or hypotheses, or yield new research questions or hypotheses.

The LLM has found the following conclusions on the interpretations;

### conclusion_1

This conclusion has the following description/reasoning:
Our results demonstrate that the well-known IBP and CROWN-IBP methods perform substantially better than previously reported when properly tuned, indicating that prior comparisons have underestimated their potential... Overall, our work calls for a shift in how certified training methods are evaluated and compared. We advocate for standardised multi-objective evaluation protocols that jointly tune all hyperparameters.

The LLM has provided the following notes on this conclusion:
Concludes that the Pareto-based evaluation is necessary, reveals the true state of the art, and confirms that prior methods were undertuned, fully supporting Hypothesis 1.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the conclusion?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason: Overall, our work calls for a shift in how certified training methods are evaluated and compared. We advocate for standardised multi-objective evaluation protocols that jointly tune all hyperparameters. Evaluations should be done in a standardised multi objective fashion, and thereby we have shown previously unknown performance complementarities.

This conclusion is based on the following interpretations: interpretation_1, interpretation_3
Your corrected answer (empty if correct): interpretation_1

Answer this question about the (possibly **corrected!**) interpretation_id.
This conclusion based on the interpretation(s) is ...
[] Correct
[X] Almost correct (few and minor misinterpretations or mistakes)
[] Acceptable (some misinterpretations or mistakes)
[] (Partially) Incorrect (serious misinterpretations or mistakes)
[] Incorrect
[] Hallucinatory, if so explain below:

Next, the LLM was asked to link the conclusion to the following elements:

This conclusion is to answer (or reflect) upon the following research questions: research_question_1
Your corrected answer (empty if correct):

This conclusion is to support (or not) the following hypotheses: hypothesis_1
Your corrected answer (empty if correct):

This conclusion supports the hypothesis: [True]
Your corrected answer (empty if correct):

### conclusion_2

This conclusion has the following description/reasoning:
Beyond benchmarking, our work provides new insights into the mechanisms that govern certified training. We show that the trade-off between clean and certified performance is influenced by a sizeable set of interacting hyperparameters... These interactions are highly complex and could only be uncovered using a state-of-the-art hyperparameter optimisation method.

The LLM has provided the following notes on this conclusion:
Concludes that complex hyperparameter interactions govern the trade-off and require advanced HPO to be discovered, fully supporting Hypothesis 2.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the conclusion?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This conclusion is based on the following interpretations: interpretation_2
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

This conclusion is to answer (or reflect) upon the following research questions: research_question_2
Your corrected answer (empty if correct):

This conclusion is to support (or not) the following hypotheses: hypothesis_2
Your corrected answer (empty if correct):

This conclusion supports the hypothesis: [True]
Your corrected answer (empty if correct):


### General Conclusion Questions

The LLM has provided you with one or more conclusions from your work. Is this amount of conclusions the same as the amount you specified?

Please write the amount of conclusions you had for the study: [3]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;

> Undertuning: Seperate conclusion 1 into two, where one is on the undertuning and the other on the multi objective evaluation.
> Add conclusion 3: Our results demonstrate that the well-known IBP and CROWN-IBP methods perform substantially better than previously reported when properly tuned, indicating that prior comparisons have underestimated their potential. (Based on interpretation 1)

## Future Work

The LLM has also found possible future work directions in terms of research questions or hypotheses yielded from an exploratory angle of your study.

### Suggested Research Questions

#### suggested_research_question_1

The LLM has found the following suggested research question: How can certified training methods be improved at larger perturbation radii, where progress has currently stalled?
Please correct the suggestion if wrong (leave empty if correct):

The LLM has provided the following note/location on the suggestion: Section 7 (Discussion)

The LLM has provided the following reason for the suggestion: Section 7 (Discussion)

The LLM has linked the suggestion to the following conclusions: conclusion_1
Please correct the IDs if wrong/missing (leave empty if correct):

Please grade the suggestion below:
[X] The LLM has (nearly) perfectly captured a future research direction suggested by our work.
[] The LLM has stated a future research direction that was implied by our work, but not strongly suggested.
[] The LLM has stated a future research direction from our work that is partially correct.
[] The LLM has stated a future research direction that has some overlap with our work but has introduced incorrect or false information.
[] The LLM has stated a future research direction that was not stated or implied in our work; the LLM has hallucinated this information.

#### suggested_research_question_2

The LLM has found the following suggested research question: How do the findings regarding Pareto-optimal configurations and hyperparameter interactions generalize to novel methods, other datasets, or more complex threat models beyond ℓ∞ perturbations?
Please correct the suggestion if wrong (leave empty if correct):

The LLM has provided the following note/location on the suggestion: Section 7 (Discussion)

The LLM has provided the following reason for the suggestion: Section 7 (Discussion)

The LLM has linked the suggestion to the following conclusions: conclusion_1, conclusion_2
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
> We also suggested that people may develop methods based on this pareto front evaluation that may work well on specific areas of the pareto front for complementarity of certified training methods.


### Suggested Hypotheses



#### Suggested Hypotheses General

The LLM has provided you with one or more Suggested Hypotheses from your work. Is this amount of Suggested Hypotheses the same as the amount you specified?

Please write the amount of Suggested Hypotheses you had for the study: [0]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;
