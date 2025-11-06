# Automatic Extraction of Hypothesis: Growing with Experience: Growing Neural Networks in Deep Reinforcement Learning
*Lukas Fehring, Marius Lindauer, Theresa Eimer*


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

The authors hypothesise that incrementally growing a neural network's depth during deep reinforcement learning training leads to better agent performance compared to training a static network of the same final size from the start, particularly for networks that are otherwise difficult to train.

The LLM has provided the following reasoning with this hypothesis:

The hypothesis is implied in the Abstract and Introduction. The Abstract states that their method, GrowNN, which uses 'progressive network growth', shows 'improved agent performance, with incrementally GrowNN deeper networks outperforming their respective static counterparts'. The Introduction (Section 1) frames the problem as a tradeoff between small, trainable networks and large, high-capacity networks, and proposes their incremental growth approach to tackle this tradeoff. Their stated contribution is an 'experimental evaluation showing that our approach allows larger networks to solve previously impossible tasks', directly setting up the comparison against static networks.

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

The authors hypothesise that incrementally growing a neural network's depth during deep reinforcement learning training leads to better agent performance compared to training a static network of the same final size from the start, particularly for deeper networks that are otherwise difficult to train.

### General Hypothesis questions

The LLM has provided you with one or more hypothesis from your work. Is this the amount of hypothesis the same as the amount you specified?

Please write the amount of hypothesis you had for the study: [1]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;
We do find this an edge case; We find that there is an inner hypothesis within the work.

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
The authors compare their proposed GrowNN method against baseline PPO agents using static networks of different depths. The GrowNN method incrementally increases the depth of the network's feature extractor during training. The performance is evaluated on two deep reinforcement learning environments.

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.



#### Hypothesis list
This experiment is used for the following hypotheses: hypothesis_1
Your corrected list (empty if correct):

#### Metrics list
The measured metrics in this experiment are: IQM of Evaluation Episode Returns
Your corrected list (empty if correct): Episode Returns

#### Statistics
The statistics for the metrics used are: Interquartile Mean (IQM) with a shaded area representing variance over multiple runs.
Your corrected list (empty if correct): Interquartile Mean (IQM) with a shaded area representing variation (95% CI, not stated in the paper) over multiple runs.

#### Strategy and Test
The experiment strategy is summarised as: Agents are trained for 2 million environment interactions. For GrowNN, the network is grown at evenly spaced intervals during training. Hyperparameters for all methods are tuned using a modified version of BOHB.
Your corrected answer (empty if correct): Agents are trained for 2 million environment interactions. For GrowNN, the network is grown at evenly spaced intervals during training after each fidelity. Hyperparameters for all methods are tuned using a modified version of BOHB.

The experiment test is summarised as: Visual comparison of learning curves and direct comparison of final performance values (greater than).
Your corrected answer (empty if correct):

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

The results of the experiment are as follows:

{
    "MiniHack Room (Samvelyan et al., 2021)": {
        "IQM of Evaluation Episode Returns": "GrowNN agents with final depths of 2 and 4 layers achieved solution rates of over 50%, while the static network counterparts achieved 0%. In contrast the static networks of depth 1 reach the best solution."
    },
    "MuJoCo Ant (Todorov et al., 2012)": {
        "IQM of Evaluation Episode Returns": "GrowNN agents achieved a final reward improvement of 65% over the static baselines, which did not improve beyond a return of 1000."
    }
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

Please write the amount of experiments you had for the study: [2]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;
As this study is on RL, I would have seperated the environments as the comparability across environments is very small.


## Interpretation

Experiment outcomes are analysed and interpreted to determine whether the experiment supports the hypothesis or not. 

The LLM has found the following interpretations of the experiment outcomes;

## interpretation_1

This interpretation has the following description/reasoning:
The results support the hypothesis. On both MiniHack and Ant environments, the GrowNN agents with deeper final networks significantly outperformed their static counterparts. As stated in Section 4, on MiniHack, for deeper networks, 'GrowNN is superior to statically trained networks with drastically higher solution rates of over 50% compared to 0%.' On Ant, 'the GrowNN agents learn policies in which the ant actively moves forward with an improvement of 65% in terms of final reward' over baselines that failed to learn a locomotion policy. The authors conclude in Section 5 that 'the incremental depth increase benefits learning on MiniHack and Ant'. A minor contradictory finding is that for the simplest network (depth 1) on MiniHack, the static baseline performed better, suggesting the benefit of growing is most pronounced for larger networks that are difficult to train from scratch.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

The results support the hypothesis. On both MiniHack and Ant environments, the GrowNN agents with deeper final networks significantly outperformed their static counterparts. As stated in Section 4, on MiniHack, for deeper networks, 'GrowNN is superior to statically trained networks with drastically higher solution rates of over 50% compared to 0%.' On Ant, 'the GrowNN agents learn policies in which the ant actively moves forward with an improvement of 65% in terms of final reward' over baselines that failed to learn a well performing policy. The authors conclude in Section 5 that 'the incremental depth increase benefits learning on MiniHack and Ant'. A minor contradictory finding is that for the simplest network (depth 1) on MiniHack, the static baseline performed better, suggesting the benefit of growing is most pronounced for larger networks that are difficult to train from scratch.

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


