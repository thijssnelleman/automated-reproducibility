# Automatic Extraction of Study Representation: Growing with Experience: Growing Neural Networks in Deep Reinforcement Learning
*Lukas Fehring, Marius Lindauer, Theresa Eimer*


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

How can increased network capacity be enabled in Deep Reinforcement Learning while maintaining network trainability?

The LLM has provided the following reasoning with this research question:

In the Abstract and Introduction, the authors highlight that training mid-sized networks for RL is a struggle, which limits policy complexity. They motivate their work by aiming to 'enable increased network capacity while maintaining network trainability'.

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

Does incrementally growing a neural network during training improve the performance of RL agents compared to using static networks?

The LLM has provided the following reasoning with this research question:

The authors introduce GrowNN to tackle the trade-off between small and large networks and evaluate its potential against static networks of unchanging size to see if it allows larger networks to solve previously impossible tasks.

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

Does incrementally growing a neural network during training improve the performance of RL agents compared to using static networks of the final size of the growing network?

### General Research Questions questions

The LLM has provided you with one or more research questions from your work. Is this the amount of research questions the same as the amount you specified or implied?

Please write the amount of research questions you had for the study: [2]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Hypotheses

### hypothesis_1

The LLM has found the following **implied** hypothesis:

The authors hypothesise that incrementally growing the network during training (GrowNN) enables agents to utilize deeper networks effectively, achieving higher performance and solving more complex tasks than static networks of the same size.

The LLM has provided the following reasoning with this hypothesis:

In the Introduction, the authors state: 'Instead, our approach GrowNN tackles this tradeoff by incrementally growing the network during training... enabling the use of appropriately sized networks...'. They expect this to allow larger networks to solve previously impossible tasks without algorithmic changes.

The LLM has linked the hypothesis to the following research questions: research_question_1, research_question_2
Your corrected list (empty if correct):

Please grade the hypothesis stated from the following options:

The LLM ...
[] captures the hypothesis (nearly) perfectly.
[] has stated a hypothesis capturing the general spirit of our work.
[] has stated an incomplete hypothesis; the answer is correct but is missing key information.
[X] has stated the general hypothesis but has introduced false or incorrect information.
[] has stated a hypothesis similar to ours, but is far too innaccurate to consider correct.
[] has stated a hypothesis that has (nearly) no overlap with our work.
[] has stated a hypothesis of lesser quality than described above: If it is an hallucination, please explain below.


Based on the LLMs answer, would you like to improve the answer to more accurately capture the hypothesis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

The authors hypothesise that incrementally growing the network during training (GrowNN) enables agents to utilize deeper networks effectively, achieving higher performance than static networks of the same final size.

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
Evaluating the impact of network growth (GrowNN) against static network baselines using the PPO algorithm on the MiniHack Room and MuJoCo Ant environments.

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

The LLM has found the following strategy or protocol for the experiment: Hyperparameter optimization using a modified version of BOHB with SMAC3. A static fidelity schedule is used, and the network is grown after each fidelity. Baselines are trained with at least the same budget.
Your corrected answer (empty if correct):

The LLM has found the following data (sets) used as input for the experiment: MiniHack Room (Samvelyan et al., 2021), MuJoCo Ant (Todorov et al., 2012)
Your corrected answer (empty if correct):

This experiment is used to answer the following research questions: research_question_1, research_question_2
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
Comparing the learning curves and final performance of GrowNN against static networks of various depths to determine if progressive growth yields better policies.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the analysis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This analysis is based on the following experiment(s) (outcomes): experiment_1
Your corrected answer (empty if correct): 

#### Metrics list
The measured metrics in this analysis are: Evaluation Episode Returns, Solution rates, Final reward
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Interquartile Mean (IQM), Confidence intervals, Percentages
Your corrected list (empty if correct):

#### Analysis Test

The analysis test is summarised as: Simple comparison (greater than) of final returns and solution rates.
Your corrected answer (empty if correct):

#### Results

The LLM has found the data of the analysis in the study, which is summarised below. It states either the figures, tables or in text values where it has been found. It describes each with a caption (in case of figure/table), a reason, and subsets of the sets stated before: the metrics used for the analysis, the statistics used, which input data was used, and, which test was applied to reflect upon research questions or confirm/reject hypotheses.

The analysed results were found in the following locations:

- **Tables**:
- **Figures**:
  - **Figure 2**:
    - **caption**:
      - Training curves for static (solid lines) and GrowNN (dotted lines) networks on MiniHack Room 10x10 (left) and MuJoCo Ant (right). Dotted vertical lines show the evenly spaced growing points for the network. The number of layers for GrowNN networks refers to the final size.
    - **reason**:
      - This figure visually demonstrates the performance difference between the growing networks and the static baselines over the course of training.
    - **metrics**:
      - Evaluation Episode Returns
    - **statistics**:
      - Interquartile Mean (IQM)
      - Confidence intervals
    - **data**:
      - MiniHack Room (Samvelyan et al., 2021)
      - MuJoCo Ant (Todorov et al., 2012)
    - **test**:
      - Simple comparison
- **Text**:
  - **Section 4**:
    - **value**:
      - While on MiniHack, the baseline configured with a static depth 1 outperforms our growth approach, as soon as we increase the depth of the feature extractor, GrowNN is superior to statically trained networks with drastically higher solution rates of over 50% compared to 0%. On Ant, the effect is comparable: the baselines do not improve over a return of 1000, which the environment yields just by avoiding death states. However, the GrowNN agents learn policies in which the ant actively moves forward with an improvement of 65% in terms of final reward.
    - **reason**:
      - Provides the quantitative results of the comparison between GrowNN and static baselines, explicitly stating the performance gains.
    - **metrics**:
      - Solution rates
      - Final reward
    - **statistics**:
      - Percentages
    - **data**:
      - MiniHack Room (Samvelyan et al., 2021)
      - MuJoCo Ant (Todorov et al., 2012)
    - **test**:
      - Simple comparison


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
The authors interpret that GrowNN is superior to statically trained networks with drastically higher solution rates on MiniHack when depth is increased. On Ant, they note that GrowNN agents learn policies to actively move forward, whereas baselines only learn to avoid death states.

The LLM has provided the following notes on its reasoning:
This interpretation directly links the observed higher returns and solution rates to the success of the GrowNN method in training deeper networks that static training fails to optimize.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason: The authors interpret that GrowNN is superior to statically trained networks with drastically higher solution rates on MiniHack. On Ant, they note that GrowNN agents learn policies to actively move forward, whereas baselines only learn to avoid death states.

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

Please write the amount of interpretations you had for the study: [1]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;

## Conclusions

The interpretations are used to draw conclusions, which either reflect upon the previous research questions or hypotheses, or yield new research questions or hypotheses.

The LLM has found the following conclusions on the interpretations;

### conclusion_1

This conclusion has the following description/reasoning:
The authors conclude that incremental depth increase benefits learning on MiniHack and Ant, and that growing the network with the agent's capabilities is a promising avenue for scaling RL. They state that GrowNN allows larger networks to solve previously impossible tasks without algorithmic changes.

The LLM has provided the following notes on this conclusion:
Found in Section 5 (Conclusion) and Section 1 (Introduction), summarizing the success of the proposed method in addressing the research questions and supporting the hypothesis.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the conclusion?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason: The authors conclude that incremental depth increase benefits learning on MiniHack and Ant, and that growing the network with the agent's capabilities is a promising avenue for scaling RL. They state that GrowNN allows larger networks to solve previously hard to solve tasks without algorithmic changes.

This conclusion is based on the following interpretations: interpretation_1
Your corrected answer (empty if correct):

Answer this question about the (possibly **corrected!**) interpretation_id.
This conclusion based on the interpretation(s) is ...
[] Correct
[X] Almost correct (few and minor misinterpretations or mistakes)
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

The LLM has found the following suggested research question: How does incremental network growth perform on other network architectures, such as Convolutional Neural Networks (CNNs)?
Please correct the suggestion if wrong (leave empty if correct):

The LLM has provided the following note/location on the suggestion: Section 5 (Conclusion)

The LLM has provided the following reason for the suggestion: Section 5 (Conclusion)

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

Please write the amount of Suggested Research Questions you had for the study: [1]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


### Suggested Hypotheses

#### suggested_hypothesis_1

The LLM has found the following suggested hypothesis: The authors hypothesise that GrowNN can be successfully integrated into most deep RL methods due to its independence from algorithm choice.
Please correct the suggestion if wrong (leave empty if correct):

The LLM has provided the following note/location on the suggestion: Section 5 (Conclusion)

The LLM has provided the following reason for the suggestion: They state 'GrowNN is independent of algorithm choice and can thus be integrated into most deep RL methods', implying a hypothesis for future integration and testing across different RL algorithms.

The LLM has linked the suggestion to the following conclusions: conclusion_1
Please correct the IDs if wrong/missing (leave empty if correct):

Please grade the suggestion below:
[] The LLM has (nearly) perfectly captured a future research direction suggested by our work.
[X] The LLM has stated a future research direction that was implied by our work, but not strongly suggested.
[] The LLM has stated a future research direction from our work that is partially correct.
[] The LLM has stated a future research direction that has some overlap with our work but has introduced incorrect or false information.
[] The LLM has stated a future research direction that was not stated or implied in our work; the LLM has hallucinated this information.


#### Suggested Hypotheses General

The LLM has provided you with one or more Suggested Hypotheses from your work. Is this amount of Suggested Hypotheses the same as the amount you specified?

Please write the amount of Suggested Hypotheses you had for the study: [1]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;
