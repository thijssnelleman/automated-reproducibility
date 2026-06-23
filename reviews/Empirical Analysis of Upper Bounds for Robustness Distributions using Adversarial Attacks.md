# Automatic Extraction of Study Representation: Empirical Analysis of Upper Bounds for Robustness Distributions using Adversarial Attacks
*Aaron Berger, Nils Eberhardt, Annelot W. Bosman, Henning Duwe, Holger H. Hoos, Jan N. van Rijn*


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

How effective are adversarial attacks in determining computationally efficient and tight upper bounds for robustness distributions of neural networks compared to complete verification techniques?

The LLM has provided the following reasoning with this research question:

Implied from the abstract and introduction, where the authors state: 'This study examines the effectiveness of adversarial attacks in determining upper bounds for robustness distributions for neural networks. While complete neural network verification techniques can provide exact safety margins, their computational cost limits scalability.'

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

Does the monotonicity assumption for perturbation radii of adversarial examples hold, enabling the use of binary search for finding critical epsilons?

The LLM has provided the following reasoning with this research question:

Explicitly stated as a contribution in Section 1: 'We investigate the monotonicity assumption for perturbation radii of adversarial examples on MNIST...'

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

Does the monotonicity assumption for perturbation radii of adversarial attacks hold, enabling the use of binary search for finding critical epsilons?

### research_question_3

The LLM has found the following **explicit** research question:

Can robustness distributions approximated on a small subset of data accurately reflect the distribution of the entire test dataset?

The LLM has provided the following reasoning with this research question:

Explicitly stated as a contribution in Section 1: 'We use the Kolmogorov-Smirnov test to show that approximating the robustness distributions on a subset of the data results in a distribution similar to that for the entire test dataset.'

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


### research_question_4

The LLM has found the following **explicit** research question:

Is there performance complementarity between different state-of-the-art adversarial attacks and complete verifiers in terms of running time and the size of adversarial perturbations?

The LLM has provided the following reasoning with this research question:

Explicitly stated as a contribution in Section 1: 'We show performance complementarity between different state-of-the-art adversarial attacks and verifiers in terms of running time and the size of the adversarial perturbations obtained from them.'

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

Please write the amount of research questions you had for the study: [4]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Hypotheses

### hypothesis_1

The LLM has found the following **implied** hypothesis:

The authors hypothesise that adversarial attack methods can provide tight upper bounds for robustness distributions at a significantly reduced computational cost compared to complete verification methods.

The LLM has provided the following reasoning with this hypothesis:

Implied from the abstract and introduction where they propose using adversarial attacks as a 'cheap alternative' to complete verification to overcome computational cost limitations.

The LLM has linked the hypothesis to the following research questions: research_question_1, research_question_4
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


### hypothesis_2

The LLM has found the following **implied** hypothesis:

The authors hypothesise that the monotonicity assumption for perturbation radii holds in most cases, making binary search a valid approach for computing robustness values.

The LLM has provided the following reasoning with this hypothesis:

Implied from Section 3 where they state: 'Mathematically, the binary search assumes that the robustness result is monotonic concerning the perturbation size. If the monotonicity assumption holds, binary search will find the epsilon* being the closest to the true epsilon*.'

The LLM has linked the hypothesis to the following research questions: research_question_2
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

The authors hypothesise that the monotonicity assumption for perturbation radii of adversarial attacks holds in most cases, making binary search a valid approach for computing robustness values.


### hypothesis_3

The LLM has found the following **implied** hypothesis:

The authors hypothesise that the robustness distributions constructed using adversarial attack methods tend to follow log-normal distributions.

The LLM has provided the following reasoning with this hypothesis:

Implied from Section 5.2 where they test this hypothesis based on recent findings in the literature (Bosman et al.).

The LLM has linked the hypothesis to the following research questions: research_question_1, research_question_3
Your corrected list (empty if correct): research_question_3

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


### hypothesis_4

The LLM has found the following **implied** hypothesis:

The authors hypothesise that approximating robustness distributions on a subset of the data results in a distribution statistically similar to that for the entire test dataset.

The LLM has provided the following reasoning with this hypothesis:

Implied from the introduction where they list this as a contribution to show that a subset is sufficient.

The LLM has linked the hypothesis to the following research questions: research_question_3
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

Please write the amount of hypothesis you had for the study: [4]

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
Iteratively checking local robustness for each epsilon value in the search space to find counterexamples to the monotonicity assumption.

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

The LLM has found the following strategy or protocol for the experiment: Iterative search over discretised search space S := {i/255 | i in N} intersect [0, 0.4]
Your corrected answer (empty if correct):

The LLM has found the following data (sets) used as input for the experiment: MNIST (LeCun et al. 1998), mnist_relu_3_50 (König et al. 2024), mnist-net_256x2 (König et al. 2024), mnist_relu_9_100 (König et al. 2024), mnist_relu_4_1024 (König et al. 2024)
Your corrected answer (empty if correct): MNIST as a dataset and the rest are neural networks

This experiment is used to answer the following research questions: research_question_2
Your corrected list (empty if correct):

This experiment is used for the following hypotheses: hypothesis_2
Your corrected list (empty if correct):

### experiment_2

The LLM describes this experiment as follows:
Computing robustness distributions using binary search with various adversarial attacks (FGSM, PGD, AutoAttack, FAB) and comparing them to the baseline complete verifier (alpha, beta-CROWN) on a subset of 100 MNIST test images.

The LLM ...
[] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[X] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

The LLM has found the following strategy or protocol for the experiment: Binary search with k=40 iterations (for PGD/AutoAttack/CROWN) or specific restarts (FAB)
Your corrected answer (empty if correct): binary search with S := {i/255 | i ∈ N} ∩ [0, 0.4] as the search space for the attacks and the verifier.

The LLM has found the following data (sets) used as input for the experiment: MNIST (LeCun et al. 1998) subset of 100 images, mnist_relu_3_50 (König et al. 2024), mnist-net_256x2 (König et al. 2024), mnist_relu_9_100 (König et al. 2024), mnist_relu_4_1024 (König et al. 2024)
Your corrected answer (empty if correct): MNIST as a dataset and the rest are neural networks

This experiment is used to answer the following research questions: research_question_1, research_question_4
Your corrected list (empty if correct):

This experiment is used for the following hypotheses: hypothesis_1, hypothesis_3
Your corrected list (empty if correct):

### experiment_3

The LLM describes this experiment as follows:
Computing robustness distributions using adversarial attacks on the complete MNIST test set (10000 images) and comparing them to the distributions from the 100-image subset.

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

The LLM has found the following strategy or protocol for the experiment: Binary search
Your corrected answer (empty if correct):

The LLM has found the following data (sets) used as input for the experiment: MNIST (LeCun et al. 1998) complete test set, mnist_relu_3_50 (König et al. 2024), mnist-net_256x2 (König et al. 2024), mnist_relu_9_100 (König et al. 2024), mnist_relu_4_1024 (König et al. 2024)
Your corrected answer (empty if correct): MNIST as a dataset and the rest are neural networks

This experiment is used to answer the following research questions: research_question_1, research_question_3
Your corrected list (empty if correct): research_question_3

This experiment is used for the following hypotheses: hypothesis_1, hypothesis_3, hypothesis_4
Your corrected list (empty if correct): hypothesis_3, hypothesis_4


### General Experiment Questions

The LLM has provided you with one or more experiments from your work. Is this amount of experiments the same as the amount you specified?

Please write the amount of experiments you had for the study: [3]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Analysis

The LLM has found one or more analyses that were used to investigate the outcomes of your experiment(s).

### analysis_1

This analysis has the following description/reasoning:
To determine if the monotonicity assumption holds by counting counterexamples.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the analysis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This analysis is based on the following experiment(s) (outcomes): experiment_1
Your corrected answer (empty if correct): 

#### Metrics list
The measured metrics in this analysis are: Number of counterexamples, Distance between minimum adversarial example and largest robust epsilon
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Count, Mean step distance
Your corrected list (empty if correct):

#### Analysis Test

The analysis test is summarised as: Simple comparison (existence of robust result for epsilon > p*)
Your corrected answer (empty if correct):

#### Results

The LLM has found the data of the analysis in the study, which is summarised below. It states either the figures, tables or in text values where it has been found. It describes each with a caption (in case of figure/table), a reason, and subsets of the sets stated before: the metrics used for the analysis, the statistics used, which input data was used, and, which test was applied to reflect upon research questions or confirm/reject hypotheses.

The analysed results were found in the following locations:

- **Tables**:
  - **Table 4**:
    - **caption**:
      - Results of the monotonicity experiment. The experiment was executed on the first 100 images of the MNIST test set. We show for each algorithm-verifier combination, for how many images the monotonicity assumption was violated...
    - **reason**:
      - Shows the number of counterexamples found for the monotonicity assumption.
    - **metrics**:
      - Number of counterexamples
      - Distance between minimum adversarial example and largest robust epsilon
    - **statistics**:
      - Count
      - Mean step distance
    - **data**:
      - MNIST (LeCun et al. 1998)
      - mnist_relu_3_50 (König et al. 2024)
      - mnist-net_256x2 (König et al. 2024)
      - mnist_relu_9_100 (König et al. 2024)
      - mnist_relu_4_1024 (König et al. 2024)
    - **test**:
      - Simple comparison (existence of robust result for epsilon > p*)
- **Figures**:
- **Text**:
  - **Section 5.1**:
    - **value**:
      - Out of the 1572 queries to find the epsilon* with an iterative search procedure, the monotonicity assumption did not hold for just 17 queries.
    - **reason**:
      - Summarises the findings of the monotonicity experiment.
    - **metrics**:
      - Number of counterexamples
    - **statistics**:
      - Count
    - **data**:
      - MNIST (LeCun et al. 1998)
    - **test**:
      - Simple comparison (existence of robust result for epsilon > p*)


#### General

The LLM has overall captured the analysis details...

[X] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)

### analysis_2

This analysis has the following description/reasoning:
To compare the upper bounds (p*) and running times of attacks vs complete verification.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the analysis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This analysis is based on the following experiment(s) (outcomes): experiment_2
Your corrected answer (empty if correct): 

#### Metrics list
The measured metrics in this analysis are: Average running time, Average minimal adversarial perturbation size (p*), Ratio to the best p* (RB-p*), Relative marginal contribution (RMC)
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Mean, Standard deviation, Minimum, Maximum
Your corrected list (empty if correct):

#### Analysis Test

The analysis test is summarised as: Simple comparison (smaller is better)
Your corrected answer (empty if correct):

#### Results

The LLM has found the data of the analysis in the study, which is summarised below. It states either the figures, tables or in text values where it has been found. It describes each with a caption (in case of figure/table), a reason, and subsets of the sets stated before: the metrics used for the analysis, the statistics used, which input data was used, and, which test was applied to reflect upon research questions or confirm/reject hypotheses.

The analysed results were found in the following locations:

- **Tables**:
  - **Table 1**:
    - **caption**:
      - Performance comparison of complete verification method alpha, beta-CROWN and the considered adversarial attack methods in terms of running time in seconds averaged per image, the average minimum adversarial example, the relative marginal contribution (RMC) and the ratio of the average minimum adversarial perturbation p* over compared to the virtual best algorithm (VBA).
    - **reason**:
      - Provides the main performance metrics comparing attacks to the verifier.
    - **metrics**:
      - Average running time
      - Average minimal adversarial perturbation size (p*)
      - Ratio to the best p* (RB-p*)
      - Relative marginal contribution (RMC)
    - **statistics**:
      - Mean
    - **data**:
      - MNIST (LeCun et al. 1998) subset of 100 images
    - **test**:
      - Simple comparison (smaller is better)
  - **Table 2**:
    - **caption**:
      - Statistics on the 158 test images for which the epsilon* computation of alpha, beta-CROWN is as tight as possible and it holds that p* - epsilon* = 1/255.
    - **reason**:
      - Shows performance on instances where the verifier found the tightest possible bounds.
    - **metrics**:
      - Average running time
      - Average minimal adversarial perturbation size (p*)
      - Ratio to the best p* (RB-p*)
    - **statistics**:
      - Mean
    - **data**:
      - MNIST (LeCun et al. 1998) subset of 100 images
    - **test**:
      - Simple comparison (smaller is better)
  - **Table 6**:
    - **caption**:
      - Execution time in seconds and minimal adversarial perturbation on the first 100 MNIST test images.
    - **reason**:
      - Provides detailed statistics on execution time and p* values.
    - **metrics**:
      - Average running time
      - Average minimal adversarial perturbation size (p*)
    - **statistics**:
      - Mean
      - Standard deviation
      - Minimum
      - Maximum
    - **data**:
      - MNIST (LeCun et al. 1998) subset of 100 images
    - **test**:
      - Simple comparison (smaller is better)
- **Figures**:
  - **Figure 1**:
    - **caption**:
      - Approximation techniques and complete verification on first 100 MNIST test images. The lines display the CDFs of the p*-values for the different methods.
    - **reason**:
      - Visualises the robustness distributions (CDFs) for comparison.
    - **metrics**:
      - Average minimal adversarial perturbation size (p*)
    - **statistics**:
    - **data**:
      - MNIST (LeCun et al. 1998) subset of 100 images
    - **test**:
  - **Figure 2**:
    - **caption**:
      - Scatterplots of the minimum adversarial examples found with alpha, beta-CROWN (x-axis) and AutoAttack (y-axis) for two networks.
    - **reason**:
      - Visualises the per-instance correlation between the verifier and the best attack.
    - **metrics**:
      - Average minimal adversarial perturbation size (p*)
    - **statistics**:
    - **data**:
      - MNIST (LeCun et al. 1998) subset of 100 images
    - **test**:
  - **Figure 4**:
    - **caption**:
      - Fraction of instances where two algorithms found a minimal adverarial perturbation of equal size.
    - **reason**:
      - Shows complementarity and agreement between methods.
    - **metrics**:
      - Average minimal adversarial perturbation size (p*)
    - **statistics**:
    - **data**:
      - MNIST (LeCun et al. 1998) subset of 100 images
    - **test**:
  - **Figure 5**:
    - **caption**:
      - Fraction of instances where the method on th y-axis found a smaller minimal adverarial perturbation than the method on the x-axis.
    - **reason**:
      - Shows pairwise superiority between methods.
    - **metrics**:
      - Average minimal adversarial perturbation size (p*)
    - **statistics**:
    - **data**:
      - MNIST (LeCun et al. 1998) subset of 100 images
    - **test**:
      - Simple comparison (smaller is better)
- **Text**:
  - **Section 5.2**:
    - **value**:
      - Using the adversarial attack methods, we observed running times two to four magnitudes smaller than those for complete verification.
    - **reason**:
      - Highlights the main finding regarding computational efficiency.
    - **metrics**:
      - Average running time
    - **statistics**:
      - Mean
    - **data**:
      - MNIST (LeCun et al. 1998) subset of 100 images
    - **test**:
      - Simple comparison (smaller is better)


#### General

The LLM has overall captured the analysis details...

[X] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)

#### Remarks
- **data**:
      - MNIST (LeCun et al. 1998) subset of 100 images - the whole test set was also included

### analysis_3

This analysis has the following description/reasoning:
To test if the robustness distributions follow a log-normal distribution.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the analysis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This analysis is based on the following experiment(s) (outcomes): experiment_2, experiment_3
Your corrected answer (empty if correct): 

#### Metrics list
The measured metrics in this analysis are: p-value, test statistic
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: p-value
Your corrected list (empty if correct):

#### Analysis Test

The analysis test is summarised as: Kolmogorov-Smirnov (K-S) test (p < 0.05)
Your corrected answer (empty if correct):

#### Results

The LLM has found the data of the analysis in the study, which is summarised below. It states either the figures, tables or in text values where it has been found. It describes each with a caption (in case of figure/table), a reason, and subsets of the sets stated before: the metrics used for the analysis, the statistics used, which input data was used, and, which test was applied to reflect upon research questions or confirm/reject hypotheses.

The analysed results were found in the following locations:

- **Tables**:
  - **Table 7**:
    - **caption**:
      - K-S test for log-normality for the robustness distributions computed of different neural networks using alpha, beta-CROWN on the first 100 images for the epsilon* and the p* values.
    - **reason**:
      - Shows log-normality test results for the verifier.
    - **metrics**:
      - p-value
      - test statistic
    - **statistics**:
      - p-value
    - **data**:
      - MNIST (LeCun et al. 1998) subset of 100 images
    - **test**:
      - Kolmogorov-Smirnov (K-S) test (p < 0.05)
  - **Table 8**:
    - **caption**:
      - K-S test for log-normality for the robustness distributions computed using attacks on the first 100 images.
    - **reason**:
      - Shows log-normality test results for attacks on the subset.
    - **metrics**:
      - p-value
      - test statistic
    - **statistics**:
      - p-value
    - **data**:
      - MNIST (LeCun et al. 1998) subset of 100 images
    - **test**:
      - Kolmogorov-Smirnov (K-S) test (p < 0.05)
  - **Table 9**:
    - **caption**:
      - K-S test for log-normality for the robustness distributions computed using attacks on all MNIST test images.
    - **reason**:
      - Shows log-normality test results for attacks on the full test set.
    - **metrics**:
      - p-value
      - test statistic
    - **statistics**:
      - p-value
    - **data**:
      - MNIST (LeCun et al. 1998) complete test set
    - **test**:
      - Kolmogorov-Smirnov (K-S) test (p < 0.05)
- **Figures**:
- **Text**:
  - **Section 5.2**:
    - **value**:
      - By testing the hypothesis of log-normality using the Kolmogorov-Smirnov (K-S) test with a confidence level of 0.05, we found evidence that most of the robustness distributions constructed using the adversarial attack methods we considered tend to follow log-normal distributions.
    - **reason**:
      - Summarises the findings of the log-normality tests on the subset.
    - **metrics**:
      - p-value
    - **statistics**:
      - p-value
    - **data**:
      - MNIST (LeCun et al. 1998) subset of 100 images
    - **test**:
      - Kolmogorov-Smirnov (K-S) test (p < 0.05)


#### General

The LLM has overall captured the analysis details...

[X] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)

### analysis_4

This analysis has the following description/reasoning:
To see if the distributions on the 100-image subset are statistically similar to the complete test set.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the analysis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This analysis is based on the following experiment(s) (outcomes): experiment_3
Your corrected answer (empty if correct): 

#### Metrics list
The measured metrics in this analysis are: p-value
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: p-value
Your corrected list (empty if correct):

#### Analysis Test

The analysis test is summarised as: Kolmogorov-Smirnov (K-S) test (p < 0.05)
Your corrected answer (empty if correct):

#### Results

The LLM has found the data of the analysis in the study, which is summarised below. It states either the figures, tables or in text values where it has been found. It describes each with a caption (in case of figure/table), a reason, and subsets of the sets stated before: the metrics used for the analysis, the statistics used, which input data was used, and, which test was applied to reflect upon research questions or confirm/reject hypotheses.

The analysed results were found in the following locations:

- **Tables**:
  - **Table 10**:
    - **caption**:
      - K-S test to compare the minimum adversarial perturbation distributions for the first 100 images with the distributions for the whole dataset.
    - **reason**:
      - Provides the statistical test results comparing subset and full set distributions.
    - **metrics**:
      - p-value
    - **statistics**:
      - p-value
    - **data**:
      - MNIST (LeCun et al. 1998) complete test set
      - MNIST (LeCun et al. 1998) subset of 100 images
    - **test**:
      - Kolmogorov-Smirnov (K-S) test (p < 0.05)
- **Figures**:
  - **Figure 3**:
    - **caption**:
      - To assess the similarities and differences of the robustness distributions on the 100-image subset and the test set, we plot the respective CDFs. Here we show the results for AutoAttack and all networks used in our study.
    - **reason**:
      - Visualises the comparison between subset and full set distributions.
    - **metrics**:
    - **statistics**:
    - **data**:
      - MNIST (LeCun et al. 1998) complete test set
      - MNIST (LeCun et al. 1998) subset of 100 images
    - **test**:
- **Text**:
  - **Section 5.3**:
    - **value**:
      - Using the K-S test we compare the distributions on the subset and the whole test set in Appendix F Table 10. We find general similarities between the results on the whole test dataset and the subset robustness distributions...
    - **reason**:
      - Summarises the findings of the comparison between subset and full set.
    - **metrics**:
      - p-value
    - **statistics**:
      - p-value
    - **data**:
      - MNIST (LeCun et al. 1998) complete test set
      - MNIST (LeCun et al. 1998) subset of 100 images
    - **test**:
      - Kolmogorov-Smirnov (K-S) test (p < 0.05)


#### General

The LLM has overall captured the analysis details...

[X] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
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
As these counterexamples to the monotonicity assumption occur rarely, we argue that using binary search is valid for the computation of the robustness values.

The LLM has provided the following notes on its reasoning:
Authors conclude that binary search is a valid approximation despite rare violations.

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
Most of the adversarial attack methods lead to p*-values close to the ones obtained using complete verification... Using the adversarial attack methods, we observed running times two to four magnitudes smaller than those for complete verification.

The LLM has provided the following notes on its reasoning:
Authors interpret the results as showing attacks are efficient and accurate approximations.

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
we found evidence that most of the robustness distributions constructed using the adversarial attack methods we considered tend to follow log-normal distributions... In contrast to the distributions on the first 100 images, we could not find evidence for the distributions on the entire test set to follow log-normal distributions using K-S tests. This is expected, as the K-S test tends to become overly conservative for large samples of discrete data...

The LLM has provided the following notes on its reasoning:
Authors interpret the K-S test results, noting the limitation of the test on large discrete samples.

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
We find general similarities between the results on the whole test dataset and the subset robustness distributions, indicating that looking at a subset of the MNIST dataset should generally be sufficient for computing a robustness distribution...

The LLM has provided the following notes on its reasoning:
Authors interpret the K-S test comparing subset and full set.

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
Furthermore, we examined the feasibility of using binary search and provided evidence that for adversarial attacks with non-random initialisation, our search space is mostly monotonic.

The LLM has provided the following notes on this conclusion:
Final conclusion on RQ2.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the conclusion?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This conclusion is based on the following interpretations: interpretation_1
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

### conclusion_2

This conclusion has the following description/reasoning:
We have shown that adversarial attack methods can provide tight upper bounds at significantly lower computational costs than required for running complete verification methods.

The LLM has provided the following notes on this conclusion:
Final conclusion on RQ1.

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

This conclusion is to answer (or reflect) upon the following research questions: research_question_1, research_question_4
Your corrected answer (empty if correct):

This conclusion is to support (or not) the following hypotheses: hypothesis_1
Your corrected answer (empty if correct):

This conclusion supports the hypothesis: [True]
Your corrected answer (empty if correct):

### conclusion_3

This conclusion has the following description/reasoning:
We also find no significant difference in the distributions on the subset and that on the complete dataset, while our statistical tests suggest that the distributions on the entire dataset do not follow log-normal distributions; this is likely due to our test becoming overly conservative for large samples of discrete data.

The LLM has provided the following notes on this conclusion:
Final conclusion on RQ3 and log-normality.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the conclusion?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This conclusion is based on the following interpretations: interpretation_3, interpretation_4
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

This conclusion is to answer (or reflect) upon the following research questions: research_question_3
Your corrected answer (empty if correct):

This conclusion is to support (or not) the following hypotheses: hypothesis_3, hypothesis_4
Your corrected answer (empty if correct):

This conclusion supports the hypothesis: [True, True]
Your corrected answer (empty if correct):


### General Conclusion Questions

The LLM has provided you with one or more conclusions from your work. Is this amount of conclusions the same as the amount you specified?

Please write the amount of conclusions you had for the study: [3]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Future Work

The LLM has also found possible future work directions in terms of research questions or hypotheses yielded from an exploratory angle of your study.

### Suggested Research Questions

#### suggested_research_question_1

The LLM has found the following suggested research question: How well do adversarial attack methods approximate robustness distributions on more complex datasets (e.g., CIFAR-10, GTSRB, ImageNet) and more sophisticated network architectures?
Please correct the suggestion if wrong (leave empty if correct):

The LLM has provided the following note/location on the suggestion: Section 6 (Discussion and conclusions)

The LLM has provided the following reason for the suggestion: Section 6 (Discussion and conclusions)

The LLM has linked the suggestion to the following conclusions: conclusion_2
Please correct the IDs if wrong/missing (leave empty if correct):

Please grade the suggestion below:
[X] The LLM has (nearly) perfectly captured a future research direction suggested by our work.
[] The LLM has stated a future research direction that was implied by our work, but not strongly suggested.
[] The LLM has stated a future research direction from our work that is partially correct.
[] The LLM has stated a future research direction that has some overlap with our work but has introduced incorrect or false information.
[] The LLM has stated a future research direction that was not stated or implied in our work; the LLM has hallucinated this information.

#### suggested_research_question_2

The LLM has found the following suggested research question: What are effective methods for finding tight and inexpensive lower bounds for robustness distributions?
Please correct the suggestion if wrong (leave empty if correct):

The LLM has provided the following note/location on the suggestion: Section 6 (Discussion and conclusions)

The LLM has provided the following reason for the suggestion: Section 6 (Discussion and conclusions)

The LLM has linked the suggestion to the following conclusions: conclusion_2
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

The LLM has found the following suggested hypothesis: The authors hypothesise that the approach of using adversarial attacks for upper bounds is scalable to more complex datasets and sophisticated network architectures.
Please correct the suggestion if wrong (leave empty if correct):

The LLM has provided the following note/location on the suggestion: Section 6 (Discussion and conclusions)

The LLM has provided the following reason for the suggestion: Derived from the statement that the approach is more scalable and it would be interesting to apply it to more complex datasets.

The LLM has linked the suggestion to the following conclusions: conclusion_2
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
