# Automatic Extraction of Study Representation: Towards Consistent and Efficient Decision-based Attacks
*Henning Duwe, Anna Münz, Holger H. Hoos*


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

How can we develop a decision-based adversarial attack that performs consistently across different neural network architectures while being highly efficient in terms of both query budget and running time?

The LLM has provided the following reasoning with this research question:

In the abstract and introduction (Section 1), the authors state that previous decision-based attacks either perform inconsistently across different networks or are resource-intensive concerning running time. They motivate their work by addressing these limitations to make attacks applicable to real-world settings.

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

How can the Covariance Matrix Adaptation Evolutionary Strategy (CMA-ES) be adapted to overcome its inherently high query demand and effectively navigate the rugged loss landscapes of decision-based adversarial attacks?

The LLM has provided the following reasoning with this research question:

In Sections 1, 3.2, and 4, the authors discuss that CMA-ES has a naturally high query demand and that decision-based settings have rugged loss landscapes. They aim to address this by developing a selective query approach and an Initial Search Strategy (ISS).

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


### General Research Questions questions

The LLM has provided you with one or more research questions from your work. Is this the amount of research questions the same as the amount you specified or implied?

Please write the amount of research questions you had for the study: [2]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Hypotheses

### hypothesis_1

The LLM has found the following **implied** hypothesis:

The authors hypothesise that their proposed method, DACES (Decision-based Attack via CMA-ES), which incorporates a novel Initial Search Strategy and a selective query approach, will achieve a better average performance in creating minimal adversarial perturbations across various network architectures compared to state-of-the-art decision-based attacks.

The LLM has provided the following reasoning with this hypothesis:

In the abstract and introduction, the authors propose DACES to address the inconsistencies and inefficiencies of prior methods, implying it will outperform them in minimizing perturbations across different networks.

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


### hypothesis_2

The LLM has found the following **implied** hypothesis:

The authors hypothesise that DACES will be significantly faster in terms of running time compared to existing decision-based attacks, making it more applicable to real-world settings.

The LLM has provided the following reasoning with this hypothesis:

In the abstract and introduction, the authors emphasize running time as a critical constraint in real-world scenarios and claim their method is more than three times as fast as any other attack on ImageNet.

The LLM has linked the hypothesis to the following research questions:  research_question_1
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
The authors evaluate DACES against four baseline decision-based attacks (HSJA, TA, CGBA, (1+1)-CMA-ES) on multiple neural network architectures (ResNet-50, ResNet-101, VGG-16, ViT, and robust variants) using the ImageNet and CIFAR-100 datasets. They measure the median l2-norm perturbation over a budget of 30,000 queries and record the running time.

The LLM ...
[] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[X] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

The LLM has found the following strategy or protocol for the experiment: Run each attack for 30,000 queries. Average performances over ten runs using different seeds. Evaluate on 200 correctly classified images selected uniformly at random without replacement from the testing sets.
Your corrected answer (empty if correct):  Run each attack for 30,000 queries. Average performances over ten runs using different seeds for DACES. Evaluate on 200 correctly classified images selected uniformly at random without replacement from the testing sets.

The LLM has found the following data (sets) used as input for the experiment: ImageNet (Deng et al. 2009), CIFAR-100 (Krizhevsky et al. 2009)
Your corrected answer (empty if correct):

This experiment is used to answer the following research questions: research_question_1, research_question_2
Your corrected list (empty if correct):

This experiment is used for the following hypotheses: hypothesis_1, hypothesis_2
Your corrected list (empty if correct):


### General Experiment Questions

The LLM has provided you with one or more experiments from your work. Is this amount of experiments the same as the amount you specified?

Please write the amount of experiments you had for the study: [1]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Analysis

The LLM has found one or more analyses that were used to investigate the outcomes of your experiment(s).

### analysis_1

This analysis has the following description/reasoning:
To compare the performance of DACES against baseline attacks in terms of the cumulative perturbation cost (AUC) and running time across different network architectures.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the analysis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This analysis is based on the following experiment(s) (outcomes): experiment_1
Your corrected answer (empty if correct): 

#### Metrics list
The measured metrics in this analysis are: Area Under the Curve (AUC) of the median l2-norm perturbation, Median l2-norm perturbation, Running time (wall clock time)
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Average (Mean), Median
Your corrected list (empty if correct):

#### Analysis Test

The analysis test is summarised as: Direct comparison of average AUC, median distance, and average running time (lower is better).
Your corrected answer (empty if correct):

#### Results

The LLM has found the data of the analysis in the study, which is summarised below. It states either the figures, tables or in text values where it has been found. It describes each with a caption (in case of figure/table), a reason, and subsets of the sets stated before: the metrics used for the analysis, the statistics used, which input data was used, and, which test was applied to reflect upon research questions or confirm/reject hypotheses.

The analysed results were found in the following locations:

- **Tables**:
  - **Table 1**:
    - **caption**:
      - Average running time of each attack in seconds. HSJA is omitted as the only CPU-based method. Running DACES on CPU to compare it to HSJA reveals an advantage of 9.5% for DACES (4 332 compared to 4 743 seconds).
    - **reason**:
      - Shows the running time comparison supporting hypothesis 2.
    - **metrics**:
      - Running time (wall clock time)
    - **statistics**:
      - Average (Mean)
    - **data**:
      - ImageNet (Deng et al. 2009)
      - CIFAR-100 (Krizhevsky et al. 2009)
    - **test**:
      - Direct comparison of average running time (lower is better)
  - **Table 2**:
    - **caption**:
      - AUC over 200 images (per network) from the ImageNet testing set (lower is better).
    - **reason**:
      - Shows the AUC performance of all attacks on ImageNet models, supporting hypothesis 1.
    - **metrics**:
      - Area Under the Curve (AUC) of the median l2-norm perturbation
    - **statistics**:
      - Average (Mean)
    - **data**:
      - ImageNet (Deng et al. 2009)
    - **test**:
      - Direct comparison of average AUC (lower is better)
  - **Table 3**:
    - **caption**:
      - AUC over 200 images (per network) from CIFAR-100 testing set (lower is better).
    - **reason**:
      - Shows the AUC performance of all attacks on CIFAR-100 models, supporting hypothesis 1.
    - **metrics**:
      - Area Under the Curve (AUC) of the median l2-norm perturbation
    - **statistics**:
      - Average (Mean)
    - **data**:
      - CIFAR-100 (Krizhevsky et al. 2009)
    - **test**:
      - Direct comparison of average AUC (lower is better)
- **Figures**:
  - **Figure 2**:
    - **caption**:
      - Median distance versus number of model queries/time over 200 images from the ImageNet testing set (lower is better). For better readability, we concentrate on the better-performing DACES-NNI and neglect DACES-BI. DACES-NNI shows a consistently good performance over the ResNets, the VGG-16 and ViT architectures.
    - **reason**:
      - Visualizes the median l2-norm perturbation over queries and time, supporting both hypotheses.
    - **metrics**:
      - Median l2-norm perturbation
      - Running time (wall clock time)
    - **statistics**:
      - Median
    - **data**:
      - ImageNet (Deng et al. 2009)
    - **test**:
      - Direct comparison of median distance (lower is better)
- **Text**:
  - **Section 5.2**:
    - **value**:
      - Across all ImageNet networks, DACES-NNI was observed to obtain the best average AUC, followed by DACES-BI, HSJA, TA, (1+1)-CMA-ES and last CGBA. On CIFAR-100, HSJA performs best, followed by CGBA and DACES.
    - **reason**:
      - Summarizes the main findings from the tables regarding the AUC metric.
    - **metrics**:
      - Area Under the Curve (AUC) of the median l2-norm perturbation
    - **statistics**:
      - Average (Mean)
    - **data**:
      - ImageNet (Deng et al. 2009)
      - CIFAR-100 (Krizhevsky et al. 2009)
    - **test**:
      - Direct comparison of average AUC (lower is better)


#### General

The LLM has overall captured the analysis details...

[] Very well (No major mistakes and/or missing information)
[X] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)


### General Analysis Questions

The LLM has provided you with one or more analyses from your work. Is this amount of analyses the same as the amount you specified?

Please write the amount of analyses you had for the study: [2]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;
The analysis of 5.3 (Marginal contribution) was not included.


## Interpretation

Experiment outcomes are analysed and interpreted to determine whether the experiment supports the hypothesis or not. 

The LLM has found the following interpretations of the experiment outcomes;

### interpretation_1

This interpretation has the following description/reasoning:
The authors interpret that DACES-NNI is the fastest attack on ImageNet, being 3 times faster on average than the next quickest attack, CGBA. They state these results show that DACES is specifically suitable for attacking large ImageNet networks in a setting where not only the query budget but also the time is constrained (Section 5.2).

The LLM has provided the following notes on its reasoning:
This interpretation directly addresses the running time results from Table 1 and Figure 2, linking them to real-world applicability.

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
The authors note that DACES-NNI obtains the best average AUC across all ImageNet networks, including robustly trained models. However, they acknowledge that on CIFAR-100, HSJA performs best, followed by CGBA and DACES (Section 5.2).

The LLM has provided the following notes on its reasoning:
This interpretation summarizes the performance metrics from Tables 2 and 3, showing where the proposed method excels and where it falls short.

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
The interpertation in section 5.3 is missing (marginal contribution); improved state of the art is an important interpretation here.

## Conclusions

The interpretations are used to draw conclusions, which either reflect upon the previous research questions or hypotheses, or yield new research questions or hypotheses.

The LLM has found the following conclusions on the interpretations;

### conclusion_1

This conclusion has the following description/reasoning:
The authors conclude that DACES achieves the best average performance on various neural networks for ImageNet and CIFAR-100, successfully utilizing a novel initial search strategy and query strategy. They also conclude that DACES fully utilizes modern GPUs, making it 3 times faster than the next quickest attack on ImageNet, thus supporting their hypotheses regarding efficiency and performance (Section 6).

The LLM has provided the following notes on this conclusion:
Found in Section 6 (Conclusion), where the authors explicitly state these points as the main takeaways of their study, confirming their initial claims.

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

This conclusion is to support (or not) the following hypotheses: hypothesis_1, hypothesis_2
Your corrected answer (empty if correct):

This conclusion supports the hypothesis: [True, True]
Your corrected answer (empty if correct):


### General Conclusion Questions

The LLM has provided you with one or more conclusions from your work. Is this amount of conclusions the same as the amount you specified?

Please write the amount of conclusions you had for the study: [1]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Future Work

The LLM has also found possible future work directions in terms of research questions or hypotheses yielded from an exploratory angle of your study.

### Suggested Research Questions



#### Suggested Research Questions General

The LLM has provided you with one or more Suggested Research Questions from your work. Is this amount of Suggested Research Questions the same as the amount you specified?

Please write the amount of Suggested Research Questions you had for the study: [0]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


### Suggested Hypotheses



#### Suggested Hypotheses General

The LLM has provided you with one or more Suggested Hypotheses from your work. Is this amount of Suggested Hypotheses the same as the amount you specified?

Please write the amount of Suggested Hypotheses you had for the study: [0]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;
