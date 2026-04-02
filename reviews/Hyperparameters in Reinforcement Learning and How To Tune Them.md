# Automatic Extraction of Study Representation: Hyperparameters in Reinforcement Learning and How To Tune Them
*Theresa Eimer, Marius Lindauer, Roberta Raileanu*


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

How do hyperparameter choices and random seeds affect the final performance and sample efficiency of RL algorithms?

The LLM has provided the following reasoning with this research question:

Found in the Abstract and Introduction: 'we show that hyperparameter choices in RL can significantly affect the agent’s final performance... and that the hyperparameter landscape can strongly depend on the tuning seed'.

Please grade the research question stated from the following options:

The LLM ...
[] captures the research question (nearly) perfectly.
[] has stated a research question capturing the general spirit of our work.
[] has stated an incomplete research question; the answer is correct but is missing key information.
[X] has stated a general research question but has introduced false or incorrect information.
[] has stated a research question similar to ours, but is far too innaccurate to consider correct.
[] has stated a research question that has (nearly) no overlap with our work.
[] has stated a research question of lesser quality than described above: If it is an hallucination, please explain below.


Based on the LLMs answer, would you like to improve the answer to more accurately capture the research question?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

How do hyperparameter choices affect the final performance and sample efficiency of RL algorithms?

### research_question_2

The LLM has found the following **implied** research question:

Are existing Hyperparameter Optimization (HPO) tools capable of producing better performing, more stable, and more easily comparable RL agents while using fewer computational resources compared to hand-tuning?

The LLM has provided the following reasoning with this research question:

Found in Section 1: 'In this paper, we demonstrate that compared to tuning hyperparameters by hand, existing HPO tools are capable of producing better performing, more stable, and more easily comparable RL agents, while using fewer computational resources.'

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

Which RL Hyperparameters Should Be Tuned?

The LLM has provided the following reasoning with this research question:

Explicitly stated as the heading for Section 4.1.

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

Are Hyperparameters in RL Well Behaved?

The LLM has provided the following reasoning with this research question:

Explicitly stated as the heading for Section 4.2.

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


### research_question_5

The LLM has found the following **explicit** research question:

How Do We Account for Noise?

The LLM has provided the following reasoning with this research question:

Explicitly stated as the heading for Section 4.3.

Please grade the research question stated from the following options:

The LLM ...
[] captures the research question (nearly) perfectly.
[] has stated a research question capturing the general spirit of our work.
[] has stated an incomplete research question; the answer is correct but is missing key information.
[] has stated a general research question but has introduced false or incorrect information.
[X] has stated a research question similar to ours, but is far too innaccurate to consider correct.
[] has stated a research question that has (nearly) no overlap with our work.
[] has stated a research question of lesser quality than described above: If it is an hallucination, please explain below.


Based on the LLMs answer, would you like to improve the answer to more accurately capture the research question?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

How do we account for the noise in the RL algorithm while tuning RL hyperparameters?

### research_question_6

The LLM has found the following **implied** research question:

What are the tradeoffs for hyperparameter optimization in practice on complex environments?

The LLM has provided the following reasoning with this research question:

Implied from Section 5 heading and introduction: 'we now turn to more complex use cases of HPO... we want to see if HPO tools can improve upon the state of the art in these domains'.

Please grade the research question stated from the following options:

The LLM ...
[] captures the research question (nearly) perfectly.
[] has stated a research question capturing the general spirit of our work.
[] has stated an incomplete research question; the answer is correct but is missing key information.
[] has stated a general research question but has introduced false or incorrect information.
[X] has stated a research question similar to ours, but is far too innaccurate to consider correct.
[] has stated a research question that has (nearly) no overlap with our work.
[] has stated a research question of lesser quality than described above: If it is an hallucination, please explain below.


Based on the LLMs answer, would you like to improve the answer to more accurately capture the research question?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.



### General Research Questions questions

The LLM has provided you with one or more research questions from your work. Is this the amount of research questions the same as the amount you specified or implied?

Please write the amount of research questions you had for the study: [5]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;
Number 6 is a duplicate of RQ1 and RQ2 (stated again but on complex environments)


## Hypotheses

### hypothesis_1

The LLM has found the following **implied** hypothesis:

The authors hypothesise that hyperparameter choices in RL significantly affect the agent's final performance and sample efficiency, and that the hyperparameter landscape strongly depends on the tuning seed.

The LLM has provided the following reasoning with this hypothesis:

Implied in the Abstract: 'we show that hyperparameter choices in RL can significantly affect...'

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

The authors hypothesise that hyperparameter choices in RL significantly affect the agent's final performance and sample efficiency, and that the random seed has a strong influence on tuning results.

### hypothesis_2

The LLM has found the following **implied** hypothesis:

The authors hypothesise that existing HPO tools can produce better performing, more stable, and more easily comparable RL agents using fewer computational resources than hand-tuning.

The LLM has provided the following reasoning with this hypothesis:

Implied in Section 1: 'In this paper, we demonstrate that compared to tuning hyperparameters by hand, existing HPO tools are capable of producing better performing...'

The LLM has linked the hypothesis to the following research questions: research_question_2, research_question_6
Your corrected list (empty if correct): research_question_2

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

The authors hypothesise that RL hyperparameter landscapes are relatively smooth, making it possible to tune them effectively without RL-specific additions to the tuning algorithm.

The LLM has provided the following reasoning with this hypothesis:

Implied in Section 4.2: 'we want the algorithm’s performance to be predictable... in essence, a smooth optimization landscape'.

The LLM has linked the hypothesis to the following research questions: research_question_4
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

The authors hypothesise that RL hyperparameter landscapes are not smooth, making it difficult to tune them effectively without RL-specific additions to the tuning algorithm.

### hypothesis_4

The LLM has found the following **implied** hypothesis:

The authors hypothesise that evaluating configurations on multiple seeds (separating tuning and testing seeds) provides a more reliable estimate of true performance and prevents overfitting to tuning seeds.

The LLM has provided the following reasoning with this hypothesis:

Implied in Section 4.3: 'it is common to evaluate a configuration on multiple seeds in order to achieve a more reliable estimate of the true performance'.

The LLM has linked the hypothesis to the following research questions: research_question_5
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
Sweeping over 8-11 hyperparameters for DQN, SAC, and PPO across 5 random seeds to study hyperparameter influence, landscape smoothness, and importance.

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

The LLM has found the following strategy or protocol for the experiment: Grid sweep over individual hyperparameters (1D sweeps), 5 random seeds per configuration.
Your corrected answer (empty if correct):

The LLM has found the following data (sets) used as input for the experiment: Pendulum (Brockman et al., 2016), Acrobot (Brockman et al., 2016), MiniGrid Empty (Chevalier-Boisvert et al., 2018), MiniGrid DoorKey 5x5 (Chevalier-Boisvert et al., 2018), Brax Ant (Freeman et al., 2021), Brax Halfcheetah (Freeman et al., 2021), Brax Humanoid (Freeman et al., 2021)
Your corrected answer (empty if correct):

This experiment is used to answer the following research questions: research_question_1, research_question_3, research_question_4
Your corrected list (empty if correct): research_question_1, research_question_3, research_question_4, research_question_5

This experiment is used for the following hypotheses: hypothesis_1, hypothesis_3
Your corrected list (empty if correct): hypothesis_1, hypothesis_3, hypothesis_4

### experiment_2

The LLM describes this experiment as follows:
Comparing HPO methods (RS, DEHB, PB2) on differently sized search spaces with a small budget of 10 full RL runs, and evaluating the effect of tuning on multiple seeds.

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

The LLM has found the following strategy or protocol for the experiment: HPO budget of 10 full RL runs. Tuning on 1, 3, 5, or 10 seeds. Testing on 5 or 10 unseen test seeds.
Your corrected answer (empty if correct):

The LLM has found the following data (sets) used as input for the experiment: Pendulum (Brockman et al., 2016), Acrobot (Brockman et al., 2016)
Your corrected answer (empty if correct):

This experiment is used to answer the following research questions: research_question_2, research_question_5
Your corrected list (empty if correct): research_question_5

This experiment is used for the following hypotheses: hypothesis_2, hypothesis_4
Your corrected list (empty if correct): hypothesis_4

### experiment_3

The LLM describes this experiment as follows:
Tuning state-of-the-art RL algorithms (PPO, IDAAC) on complex environments (Brax, Procgen) using HPO tools (RS, DEHB, BGT, PB2) with budgets of 16 and 64 runs, comparing to hand-tuned baselines.

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

The LLM has found the following strategy or protocol for the experiment: HPO budgets of 16 and 64 full algorithm runs. Tuning 3 times across 5 seeds, testing best configuration on 10 unseen test seeds.
Your corrected answer (empty if correct):

The LLM has found the following data (sets) used as input for the experiment: Brax Ant (Freeman et al., 2021), Brax Halfcheetah (Freeman et al., 2021), Brax Humanoid (Freeman et al., 2021), Procgen Bigfish (Cobbe et al., 2020), Procgen Climber (Cobbe et al., 2020), Procgen Plunder (Cobbe et al., 2020)
Your corrected answer (empty if correct):

This experiment is used to answer the following research questions: research_question_2, research_question_6
Your corrected list (empty if correct): research_question_2

This experiment is used for the following hypotheses: hypothesis_2
Your corrected list (empty if correct):


### General Experiment Questions

The LLM has provided you with one or more experiments from your work. Is this amount of experiments the same as the amount you specified?

Please write the amount of experiments you had for the study: [3]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Analysis

The LLM has found one or more analyses that were used to investigate the outcomes of your experiment(s).

### analysis_1

This analysis has the following description/reasoning:
Analyzing the effect of individual hyperparameters on final performance and stability, and calculating hyperparameter importance using fANOVA.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the analysis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This analysis is based on the following experiment(s) (outcomes): experiment_1
Your corrected answer (empty if correct): 

#### Metrics list
The measured metrics in this analysis are: Average Episodic Return, Hyperparameter Importance (fANOVA)
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Mean, Standard Deviation, Median
Your corrected list (empty if correct):

#### Analysis Test

The analysis test is summarised as: Visual comparison of performance curves, fANOVA importance scores
Your corrected answer (empty if correct):

#### Results

The LLM has found the data of the analysis in the study, which is summarised below. It states either the figures, tables or in text values where it has been found. It describes each with a caption (in case of figure/table), a reason, and subsets of the sets stated before: the metrics used for the analysis, the statistics used, which input data was used, and, which test was applied to reflect upon research questions or confirm/reject hypotheses.

The analysed results were found in the following locations:

- **Tables**:
- **Figures**:
  - **Figure 2**:
    - **caption**:
      - Hyperparameter landscapes of learning rate, clip range and entropy coefficient for PPO on Brax and MiniGrid. For each hyperparameter value, we report the average final return and standard deviation across 5 seeds.
    - **reason**:
      - Shows the landscape smoothness and variance.
    - **metrics**:
      - Average Episodic Return
    - **statistics**:
      - Mean
      - Standard Deviation
    - **data**:
      - Brax Ant (Freeman et al., 2021)
      - Brax Halfcheetah (Freeman et al., 2021)
      - Brax Humanoid (Freeman et al., 2021)
      - MiniGrid Empty (Chevalier-Boisvert et al., 2018)
      - MiniGrid DoorKey 5x5 (Chevalier-Boisvert et al., 2018)
    - **test**:
      - Visual comparison of performance curves
  - **Figure 3**:
    - **caption**:
      - Hyperparameter Sweeps for PPO across learning rates, entropy coefficients and clip ranges on various environments. The mean and standard deviation are computed across 5 seeds.
    - **reason**:
      - Shows training stability over episodes.
    - **metrics**:
      - Average Episodic Return
    - **statistics**:
      - Mean
      - Standard Deviation
    - **data**:
      - Acrobot (Brockman et al., 2016)
      - MiniGrid Empty (Chevalier-Boisvert et al., 2018)
      - Brax Ant (Freeman et al., 2021)
      - MiniGrid DoorKey 5x5 (Chevalier-Boisvert et al., 2018)
    - **test**:
      - Visual comparison of performance curves
  - **Figure 25**:
    - **caption**:
      - PPO Hyperparameter Importances on Acrobot (left) and Pendulum (right).
    - **reason**:
      - Shows fANOVA importance.
    - **metrics**:
      - Hyperparameter Importance (fANOVA)
    - **statistics**:
      - Mean
    - **data**:
      - Acrobot (Brockman et al., 2016)
      - Pendulum (Brockman et al., 2016)
    - **test**:
      - fANOVA importance scores
  - !!! ADD FIGURE 17-30!!!
- **Text**:
  - **Section 4.1**:
    - **value**:
      - In total, we observed only the worst hyperparameter choice being within the best choice’s standard deviation 7 times out of 126 settings and only 13 times the median performance dropping by less than 20%.
    - **reason**:
      - Quantifies the large influence of hyperparameters.
    - **metrics**:
      - Average Episodic Return
    - **statistics**:
      - Standard Deviation
      - Median
    - **data**:
      - Pendulum (Brockman et al., 2016)
      - Acrobot (Brockman et al., 2016)
      - MiniGrid Empty (Chevalier-Boisvert et al., 2018)
      - MiniGrid DoorKey 5x5 (Chevalier-Boisvert et al., 2018)
      - Brax Ant (Freeman et al., 2021)
      - Brax Halfcheetah (Freeman et al., 2021)
      - Brax Humanoid (Freeman et al., 2021)
    - **test**:
      - Visual comparison of performance curves


#### General

The LLM has overall captured the analysis details...

[X] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)

### analysis_2

This analysis has the following description/reasoning:
Comparing the performance of DEHB, PB2, and RS across different search space sizes and different numbers of tuning seeds.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the analysis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This analysis is based on the following experiment(s) (outcomes): experiment_2
Your corrected answer (empty if correct): 

#### Metrics list
The measured metrics in this analysis are: Negative evaluation reward, Test performance (mean reward)
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Mean, Standard Deviation
Your corrected list (empty if correct):

#### Analysis Test

The analysis test is summarised as: Direct comparison of mean rewards
Your corrected answer (empty if correct):

#### Results

The LLM has found the data of the analysis in the study, which is summarised below. It states either the figures, tables or in text values where it has been found. It describes each with a caption (in case of figure/table), a reason, and subsets of the sets stated before: the metrics used for the analysis, the statistics used, which input data was used, and, which test was applied to reflect upon research questions or confirm/reject hypotheses.

The analysed results were found in the following locations:

- **Tables**:
  - **Table 1**:
    - **caption**:
      - Tuning PPO on Acrobot (top) and SAC on Pendulum (bottom) across different search space sizes (i.e. only learning rate, {learning rate, entropy coefficient, training epochs}, and full search space). Shown is the negative evaluation reward across 5 tuning runs. Lower numbers are better, best performance on each environment is highlighted. The best final performance on a single seed from our sweeps is also reported.
    - **reason**:
      - Shows HPO performance across search space sizes.
    - **metrics**:
      - Negative evaluation reward
    - **statistics**:
      - Mean
      - Standard Deviation
    - **data**:
      - Acrobot (Brockman et al., 2016)
      - Pendulum (Brockman et al., 2016)
    - **test**:
      - Direct comparison of mean rewards
  - **Table 2**:
    - **caption**:
      - Tuning PPO on Acrobot (top) and SAC on Pendulum (bottom) across the full search space and different numbers of seeds. Lower numbers are better, best test performance for each method and values within its standard deviation are highlighted. Test performances are aggregated across 10 separate test seeds using the mean for each tuning run. We report mean and standard deviation of these.
    - **reason**:
      - Shows the effect of tuning on multiple seeds vs testing on unseen seeds.
    - **metrics**:
      - Test performance (mean reward)
    - **statistics**:
      - Mean
      - Standard Deviation
    - **data**:
      - Acrobot (Brockman et al., 2016)
      - Pendulum (Brockman et al., 2016)
    - **test**:
      - Direct comparison of mean rewards
- **Figures**:
- **Text**:
  - **Section 4.3**:
    - **value**:
      - The performance difference between tuning and testing is significant in many cases and we can see e.g. on Acrobot that the best incumbent configurations, found by DEHB, perform more than four times worse on test seeds.
    - **reason**:
      - Highlights overfitting to tuning seeds.
    - **metrics**:
      - Test performance (mean reward)
    - **statistics**:
      - Mean
    - **data**:
      - Acrobot (Brockman et al., 2016)
    - **test**:
      - Direct comparison of mean rewards


#### General

The LLM has overall captured the analysis details...

[X] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)

### analysis_3

This analysis has the following description/reasoning:
Comparing HPO methods against hand-tuned baselines on Brax and Procgen with budgets of 16 and 64 runs.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the analysis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This analysis is based on the following experiment(s) (outcomes): experiment_3
Your corrected answer (empty if correct): 

#### Metrics list
The measured metrics in this analysis are: Mean Evaluation Reward, Rank
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Mean, 98% confidence interval, Standard Deviation
Your corrected list (empty if correct):

#### Analysis Test

The analysis test is summarised as: Direct comparison of mean rewards, Rank computation
Your corrected answer (empty if correct):

#### Results

The LLM has found the data of the analysis in the study, which is summarised below. It states either the figures, tables or in text values where it has been found. It describes each with a caption (in case of figure/table), a reason, and subsets of the sets stated before: the metrics used for the analysis, the statistics used, which input data was used, and, which test was applied to reflect upon research questions or confirm/reject hypotheses.

The analysed results were found in the following locations:

- **Tables**:
  - **Table 8**:
    - **caption**:
      - Tuning PPO on Brax’s Ant, Halfcheetah and Humanoid environments. Shown are tuning results across 3 runs across 5 seeds each, tested on 10 different test seeds.
    - **reason**:
      - Tabular results for Brax.
    - **metrics**:
      - Mean Evaluation Reward
    - **statistics**:
      - Mean
      - Standard Deviation
    - **data**:
      - Brax Ant (Freeman et al., 2021)
      - Brax Halfcheetah (Freeman et al., 2021)
      - Brax Humanoid (Freeman et al., 2021)
    - **test**:
      - Direct comparison of mean rewards
  - **Table 9**:
    - **caption**:
      - Tuning IDAAC on Procgen’s Bigfish, Climber and Plunder. Results are across 3 runs using 5 seeds each, and tested on 10 different test seeds.
    - **reason**:
      - Tabular results for Procgen.
    - **metrics**:
      - Mean Evaluation Reward
    - **statistics**:
      - Mean
      - Standard Deviation
    - **data**:
      - Procgen Bigfish (Cobbe et al., 2020)
      - Procgen Climber (Cobbe et al., 2020)
      - Procgen Plunder (Cobbe et al., 2020)
    - **test**:
      - Direct comparison of mean rewards
- **Figures**:
  - **Figure 5**:
    - **caption**:
      - Tuning Results for PPO on Brax. Shown is the mean evaluation reward across 10 episodes for 3 tuning runs as well as the 98% confidence interval across tuning runs.
    - **reason**:
      - Visual comparison of HPO vs baseline on Brax.
    - **metrics**:
      - Mean Evaluation Reward
    - **statistics**:
      - Mean
      - 98% confidence interval
    - **data**:
      - Brax Ant (Freeman et al., 2021)
      - Brax Halfcheetah (Freeman et al., 2021)
      - Brax Humanoid (Freeman et al., 2021)
    - **test**:
      - Direct comparison of mean rewards
  - **Figure 6**:
    - **caption**:
      - Tuning Results for IDAAC on Procgen. Shown is the mean evaluation reward across 10 episodes for 3 tuning runs as well as the 98% confidence interval across tuning runs.
    - **reason**:
      - Visual comparison of HPO vs baseline on Procgen.
    - **metrics**:
      - Mean Evaluation Reward
    - **statistics**:
      - Mean
      - 98% confidence interval
    - **data**:
      - Procgen Bigfish (Cobbe et al., 2020)
      - Procgen Climber (Cobbe et al., 2020)
      - Procgen Plunder (Cobbe et al., 2020)
    - **test**:
      - Direct comparison of mean rewards
- **Text**:
  - !!!! CHANGED !!! **Section 5**:
    - **value**:
      - On Brax, DEHB outperforms the baseline with a mean rank of 1.3 compared to 1.7 for the 16 run budget and a rank of 1.0 compared to the baselines’s 1.3 with 64 runs. On Procgen the comparison is similar with 1.7 to 2 for 16 runs and 1.0 to 1.3 for 64 runs.
    - **reason**:
      - Summarizes the rank performance of DEHB vs baseline.
    - **metrics**:
      - Rank
    - **statistics**:
      - Mean
    - **data**:
      - Brax Ant (Freeman et al., 2021)
      - Brax Halfcheetah (Freeman et al., 2021)
      - Brax Humanoid (Freeman et al., 2021)
      - Procgen Bigfish (Cobbe et al., 2020)
      - Procgen Plunder (Cobbe et al., 2020)
      - Procgen Climber (Cobbe et al., 2020)
    - **test**:
      - Rank computation


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
We did an analysis in Figure 4; on how different seeds behave differently for different hyperparameter values

## Interpretation

Experiment outcomes are analysed and interpreted to determine whether the experiment supports the hypothesis or not. 

The LLM has found the following interpretations of the experiment outcomes;

### interpretation_1

This interpretation has the following description/reasoning:
Since most hyperparameters have significant influences on performance, their importance varies across environments and there are only few interference effects, we recommend tuning as many hyperparameters as possible... it should be possible to tune RL hyperparameters just as well as the ones in any other fields without RL-specific additions to the tuning algorithm since RL hyperparameter landscapes appear to be rather smooth.

The LLM has provided the following notes on its reasoning:
Interprets the sweep and fANOVA results to conclude that landscapes are smooth but many HPs matter, supporting the use of general HPO tools.

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
Overall we see that finding well performing configurations across large search spaces is usually possible even with a simple algorithm like RS... evaluating the configurations across multiple seeds increases the difficulty of the HPO problem substantially, even though it can help avoid overfitting... Simply reporting the performance of tuned seeds for the proposed method and that of testing seeds for the baselines is an unfair comparison which can lead to wrong conclusions.

The LLM has provided the following notes on its reasoning:
Interprets the HPO results on small budgets and the effect of tuning vs testing seeds, highlighting the danger of overfitting to tuning seeds.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason: Evaluating the configurations across multiple seeds increases the difficulty of the HPO problem substantially, even though it can help avoid overfitting... Simply reporting the performance of tuned seeds for the proposed method and that of testing seeds for the baselines is an unfair comparison which can lead to wrong conclusions.

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
Overall, HPO tools conceived for the AC setting, as represented by DEHB, are the most consistent and reliable within our experimental setting... even computationally cheap methods with small tuning budgets can generally match or outperform painstakingly hand-tuned configurations that use orders of magnitude more compute.

The LLM has provided the following notes on its reasoning:
Interprets the results on Brax and Procgen, showing that DEHB outperforms baselines and other methods efficiently.

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
I would split interpretation 2 into two parts;
- Evaluating the configurations across multiple seeds increases the difficulty of the HPO problem substantially, even though it can help avoid overfitting
- Simply reporting the performance of tuned seeds for the proposed method and that of testing seeds for the baselines is an unfair comparison which can lead to wrong conclusions.

## Conclusions

The interpretations are used to draw conclusions, which either reflect upon the previous research questions or hypotheses, or yield new research questions or hypotheses.

The LLM has found the following conclusions on the interpretations;

### conclusion_1

This conclusion has the following description/reasoning:
We showed that hyperparameters in RL deserve more attention from the research community than they currently receive. Underreported tuning practices have the potential to distort algorithm evaluations while ignored hyperparameters may lead to suboptimal performance. With only small budgets, we demonstrate that HPO tools like DEHB can cover large search spaces to produce better performing configurations using fewer computational resources than hyperparameter sweeps or grid searches.

The LLM has provided the following notes on this conclusion:
The authors conclude that HPO is highly beneficial, landscapes are smooth enough for general tools, and proper seed separation is crucial for reproducibility.

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

This conclusion is to answer (or reflect) upon the following research questions: research_question_1, research_question_2, research_question_3, research_question_4, research_question_5, research_question_6
Your corrected answer (empty if correct):

This conclusion is to support (or not) the following hypotheses: hypothesis_1, hypothesis_2, hypothesis_3, hypothesis_4
Your corrected answer (empty if correct):

This conclusion supports the hypothesis: [True, True, True, True]
Your corrected answer (empty if correct):


### General Conclusion Questions

The LLM has provided you with one or more conclusions from your work. Is this amount of conclusions the same as the amount you specified?

Please write the amount of conclusions you had for the study: [2]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;
I would split conclusion 1 into two parts;
- Underreported tuning practices have the potential to distort algorithm evaluations.
- With only small budgets, we demonstrate that HPO tools like DEHB can cover large search spaces to produce better performing configurations using fewer computational resources than hyperparameter sweeps or grid searches.
 
## Future Work

The LLM has also found possible future work directions in terms of research questions or hypotheses yielded from an exploratory angle of your study.

### Suggested Research Questions

#### suggested_research_question_1

The LLM has found the following suggested research question: How can we develop HPO approaches tailored to the key challenges of RL, such as the high sensitivity to the random seed for a given hyperparameter configuration?
Please correct the suggestion if wrong (leave empty if correct):

The LLM has provided the following note/location on the suggestion: Section 7 (Conclusion)

The LLM has provided the following reason for the suggestion: Section 7 (Conclusion)

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

The LLM has found the following suggested hypothesis: Frameworks for learnt hyperparameter policies or gradient-based optimization methods can counteract the effect of high sensitivity to random seeds by reacting dynamically to an algorithm's behaviour on a given seed.
Please correct the suggestion if wrong (leave empty if correct):

The LLM has provided the following note/location on the suggestion: Section 7 (Conclusion)

The LLM has provided the following reason for the suggestion: Authors suggest this as a solution to the seed sensitivity problem.

The LLM has linked the suggestion to the following conclusions: conclusion_1
Please correct the IDs if wrong/missing (leave empty if correct):

Please grade the suggestion below:
[X] The LLM has (nearly) perfectly captured a future research direction suggested by our work.
[] The LLM has stated a future research direction that was implied by our work, but not strongly suggested.
[] The LLM has stated a future research direction from our work that is partially correct.
[] The LLM has stated a future research direction that has some overlap with our work but has introduced incorrect or false information.
[] The LLM has stated a future research direction that was not stated or implied in our work; the LLM has hallucinated this information.

#### suggested_hypothesis_2

The LLM has found the following suggested hypothesis: Higher-level AutoRL approaches that replace hyperparameters entirely by directing the algorithm's behavior could simplify and stabilize RL algorithms in the long term.
Please correct the suggestion if wrong (leave empty if correct):

The LLM has provided the following note/location on the suggestion: Section 7 (Conclusion)

The LLM has provided the following reason for the suggestion: Authors suggest this as a long-term goal for AutoRL.

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

Please write the amount of Suggested Hypotheses you had for the study: [2]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;
