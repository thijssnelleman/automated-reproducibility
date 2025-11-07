# Automatic Extraction of Hypothesis: Hyperparameters in Reinforcement Learning and How To Tune Them
*Theresa Eimer, Marius Lindauer, Roberta Raileanu*


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

The authors hypothesise that principled Hyperparameter Optimization (HPO) methods from AutoML are capable of producing better performing, more stable, and more easily comparable RL agents than traditional manual tuning or grid search, while using significantly fewer computational resources.

The LLM has provided the following reasoning with this hypothesis:

This hypothesis is implied from claims made in the abstract and introduction. The abstract states, "we show that HPO approaches often have higher performance and lower compute overhead." On page 2, the authors state more strongly: "we demonstrate that compared to tuning hyperparameters by hand, existing HPO tools are capable of producing better performing, more stable, and more easily comparable RL agents, while using fewer computational resources." This is the central claim investigated throughout the paper, especially in Section 5.

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

The authors hypothesise that principled Hyperparameter Optimization (HPO) methods from AutoML are capable of producing better performing RL agents than traditional manual tuning or grid search, while using significantly fewer computational resources.

### hypothesis_2

The LLM has found the following **implied** hypothesis:

The authors hypothesise that failing to separate tuning seeds from testing seeds in Reinforcement Learning leads to overfitting and unreliable performance evaluations, making this separation a crucial best practice for reproducibility.

The LLM has provided the following reasoning with this hypothesis:

This hypothesis is implied from the abstract, which proposes adopting "established best practices from AutoML, such as the separation of tuning and testing seeds". Section 4.3, "How Do We Account for Noise?", is dedicated to investigating this issue. The authors state on page 6, "The performance difference between tuning and testing is significant in many cases... This presents a challenge for reproducibility given that currently it is almost impossible to know what seeds were used for tuning or evaluation." This suggests a core belief that this separation is necessary and that its absence is a major problem.

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

The authors hypothesise that failing to separate tuning seeds from testing seeds in Reinforcement Learning leads to unreliable performance evaluations, making this separation a crucial best practice for reproducibility.

### General Hypothesis questions

The LLM has provided you with one or more hypothesis from your work. Is this the amount of hypothesis the same as the amount you specified?

Please write the amount of hypothesis you had for the study: [2]

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
The authors investigate the sensitivity of RL algorithms (PPO, SAC) to various hyperparameters and random seeds on simple continuous control tasks. They then compare the performance of different HPO methods (Random Search, DEHB, PB2) against a comprehensive sweep. Finally, they vary the number of seeds used for tuning to analyze the effect on generalization to unseen test seeds.

The LLM ...
[] has described the experiment (nearly) perfectly
[X] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.



#### Hypothesis list
This experiment is used for the following hypotheses: hypothesis_1, hypothesis_2
Your corrected list (empty if correct):

#### Metrics list
The measured metrics in this experiment are: Negative Evaluation Reward
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Mean and standard deviation across tuning runs or seeds.
Your corrected list (empty if correct):

#### Strategy and Test
The experiment strategy is summarised as: HPO methods are run with a budget of 10 full RL runs. The sweep baseline consists of 125 runs per environment. For the noise analysis, tuning is performed on 1, 3, 5, or 10 seeds, and the resulting best configuration is evaluated on 10 separate, unseen test seeds.
Your corrected answer (empty if correct):

The experiment test is summarised as: Comparison of mean values and their standard deviations.
Your corrected answer (empty if correct):

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

The results of the experiment are as follows:

{
    "Acrobot": {
        "Negative Evaluation Reward": "For the full search space (Table 1), the best incumbent rewards were: DEHB: 71 ± 3, PB2: 305 ± 186, RS: 83 ± 5. The best single seed from the sweep achieved 81. For the seed generalization analysis (Table 2), the test performance for DEHB with 1 tuning seed was 341.3 ± 183.1, while with 10 tuning seeds it was 464.8 ± 36.5, showing a large gap between incumbent and test performance."
    },
    "Pendulum": {
        "Negative Evaluation Reward": "For the full search space (Table 1), the best incumbent rewards were: DEHB: 112 ± 24, PB2: 78 ± 19, RS: 144 ± 48. The best single seed from the sweep achieved 117. For the seed generalization analysis (Table 2), the test performance for DEHB with 1 tuning seed was 150.5 ± 13.4, while with 10 tuning seeds it was 318.6 ± 281.3, again showing a large generalization gap."
    }
    TODO: Add full table 1 and table 2
}

#### General

The LLM has overall captured the experiment details...

[] Very well (No major mistakes and/or missing information)
[X] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)

### experiment_2

The LLM describes this experiment as follows:
The authors compare several HPO methods (DEHB, BGT, RS) against the published, manually-tuned hyperparameters for state-of-the-art RL algorithms on challenging benchmark environments (Brax and Procgen).

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.



#### Hypothesis list
This experiment is used for the following hypotheses: hypothesis_1
Your corrected list (empty if correct): hypothesis_1, hypothesis_2

#### Metrics list
The measured metrics in this experiment are: Mean Evaluation Reward
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Mean and 98% confidence interval across 3 tuning runs.
Your corrected list (empty if correct):

#### Strategy and Test
The experiment strategy is summarised as: HPO methods are given a budget of 16 or 64 full algorithm runs. The IDAAC baseline on Procgen uses a budget of 810 runs. Tuning is performed across 5 seeds, and the best-found configuration is tested on 10 unseen seeds. The entire tuning process is repeated 3 times for statistical robustness.
Your corrected answer (empty if correct):

The experiment test is summarised as: Comparison of mean values and their confidence intervals. The authors also compute and compare the mean ranks of the methods across all environments within a benchmark.
Your corrected answer (empty if correct):

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

The results of the experiment are as follows:

{
    "Brax (Ant, Halfcheetah, Humanoid)": {
        "Mean Evaluation Reward": "With a 64-run budget (Table 8), DEHB Test performance was: Ant: 4696 ± 1252 (Baseline: 3448 ± 343), Halfcheetah: 8039 ± 636 (Baseline: 6904 ± 377), Humanoid: 5205 ± 2781 (Baseline: 3235 ± 758)."
    },
    "Procgen (Bigfish, Climber, Plunder)": {
        "Mean Evaluation Reward": "With a 64-run budget (Table 9), DEHB Test performance was: Bigfish: 9.4 ± 2.5 (Baseline: 6.8 ± 3.2), Climber: 3.9 ± 1.9 (Baseline: 4.1 ± 1.4), Plunder: 8.7 ± 0.7 (Baseline: 11.8 ± 5.5)."
    }
    TODO: Ranks are missing
}

#### General

The LLM has overall captured the experiment details...

[X] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)


### General Experiment Questions

The LLM has provided you with one or more experiments from your work. Is this amount of experiments the same as the amount you specified?

Please write the amount of experiments you had for the study: [4]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;
I would seperate the first experiment into three; One for the baseline sweeps, one for the search space size, and one for the number of seeds.

## Interpretation

Experiment outcomes are analysed and interpreted to determine whether the experiment supports the hypothesis or not. 

The LLM has found the following interpretations of the experiment outcomes;

### interpretation_1

This interpretation has the following description/reasoning:
The results in Table 1 show that even with a small budget of 10 runs, HPO methods can find configurations that perform as well as or better than the best configuration found in a much larger sweep. The authors state: "On this small budget, they are able to match or outperform the single best seeds in all our sweep runs which use a total of 125 runs per environment." (Page 5).

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
Table 2 demonstrates a significant performance drop when configurations tuned on a set of seeds are evaluated on a separate, unseen set of test seeds. This gap indicates overfitting to the tuning seeds. The authors highlight this by stating, "we can see e.g. on Acrobot that the best incumbent configurations, found by DEHB, perform more than four times worse on test seeds. We can find this effect in all tuning methods, especially on Pendulum. This presents a challenge for reproducibility..." (Page 6). This strongly supports the hypothesis that separating tuning and test seeds is critical for obtaining reliable results.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Figures 5 and 6 demonstrate a significant performance drop when configurations tuned on a set of seeds are evaluated on a separate, unseen set of test seeds. This gap indicates overfitting to the tuning seeds. The authors highlight this by stating, "we can see e.g. on Acrobot that the best incumbent configurations, found by DEHB, perform more than four times worse on test seeds. We can find this effect in all tuning methods, especially on Pendulum. This presents a challenge for reproducibility..." (Page 6). This strongly supports the hypothesis that separating tuning and test seeds is critical for obtaining reliable results.

This interpretation is for the outcome of the following experiment: experiment_1
Your corrected answer (empty if correct):

Answer this question about the (possibly **corrected!**) experiment_id.
This interpretation of the experiment outcome is ...
[] Correct
[] Almost correct (few and minor misinterpretations or mistakes)
[] Acceptable (some misinterpretations or mistakes)
[X] (Partially) Incorrect (serious misinterpretations or mistakes)
[] Incorrect
[] Hallucinatory, if so explain below:



This interpretation is to support (or not) the following hypothesis: hypothesis_2
Your corrected answer (empty if correct):

This interpretation supports the hypothesis: True
Your corrected answer (empty if correct):

### interpretation_3

This interpretation has the following description/reasoning:
The results in Figures 5 & 6 and Tables 8 & 9 show that HPO methods, particularly DEHB, consistently match or outperform the highly-tuned baselines on both Brax and Procgen, while using a fraction of the computational budget. The authors summarize this on page 7: "On Brax, DEHB outperforms the baseline with a mean rank of 1.3 compared to 1.7 for the 16 run budget and a rank of 1.0 compared to the baselines's 1.3 with 64 runs." They conclude on page 8: "Overall, we see that even computationally cheap methods with small tuning budgets can generally match or outperform painstakingly hand-tuned configurations that use orders of magnitude more compute."

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



This interpretation is to support (or not) the following hypothesis: hypothesis_1
Your corrected answer (empty if correct):

This interpretation supports the hypothesis: True
Your corrected answer (empty if correct):


