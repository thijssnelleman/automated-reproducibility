# Automatic Extraction of Hypothesis: Towards General Negotiation Strategies with End-to-End Reinforcement Learning
*Bram M. Renting, Thomas M. Moerland, Holger H. Hoos, Catholijn M. Jonker*


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

The authors hypothesise that their end-to-end reinforcement learning method, using a graph representation and Graph Neural Networks (GNNs), can (1) effectively learn to negotiate in a fixed negotiation problem, performing comparably to existing specialized methods, and (2) learn a general negotiation strategy that successfully negotiates on diverse, never-before-seen negotiation problems.

The LLM has provided the following reasoning with this hypothesis:

The hypothesis is implied from statements in the abstract, introduction, and conclusion. The abstract states, 'we show that our method is effective and that we can learn to negotiate with other agents on never-before-seen negotiation problems.' The introduction (p. 2) outlines the goal to create a 'more general RL-based negotiation strategy capable of dealing with various negotiation problems'. The conclusion (p. 8) summarizes the findings, stating that 'our method performs as well as a recent end-to-end method that is not transferrable beyond a single fixed negotiation problem' and 'we have shown how an agent can learn to negotiate on diverse negotiation problems in such a way that performance generalises to never-before-seen negotiation problems.' These claims directly correspond to the two clauses of the formulated hypothesis.

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

The authors hypothesise that their end-to-end reinforcement learning method, using a graph representation and Graph Neural Networks (GNNs), can (1) effectively learn to negotiate in a fixed negotiation problem, performing comparably to a recent work, and (2) learn a general negotiation strategy that successfully negotiates on diverse, never-before-seen negotiation problems.


### General Hypothesis questions

The LLM has provided you with one or more hypothesis from your work. Is this the amount of hypothesis the same as the amount you specified?

Please write the amount of hypothesis you had for the study: [1]

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
To test the effectiveness of the proposed GNN-based policy on a fixed negotiation problem, it is compared against a recent end-to-end RL method by Higa et al. (2023), which is designed for such fixed problems. Both methods are trained and evaluated against a set of four baseline negotiation agents.

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
The measured metrics in this experiment are: Episodic return, Average obtained utility
Your corrected list (empty if correct): Average obtained utility

#### Statistics
The statistics for the metrics used are: Mean and 99% confidence interval over 10 random seeds.
Your corrected list (empty if correct):

#### Strategy and Test
The experiment strategy is summarised as: The policy is trained for 2,000,000 timesteps. Evaluation consists of 1000 negotiation games against each opponent. The entire process is repeated for 10 random seeds.
Your corrected answer (empty if correct):

The experiment test is summarised as: Visual comparison of the mean values and their 99% confidence intervals.
Your corrected answer (empty if correct):

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

The results of the experiment are as follows:

{
    "A single, fixed negotiation problem with baseline opponents (BoulwareAgent, ConcederAgent, LinearAgent, RandomAgent)": {
        "Average obtained utility": "In evaluation, the proposed method achieves nearly identical average utility scores against all four baseline opponents compared to the Higa et al. method. For example, against BoulwareAgent, both methods score ~0.9 utility, and against ConcederAgent, both score ~0.9 utility (Figure 3)."
    }
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
To test the generalizability of the proposed GNN-based policy, it is trained and evaluated on randomly generated negotiation problems that are never seen before during evaluation. The experiment is conducted against two sets of opponents: a smaller set of baseline agents and a larger, more challenging set of competition agents from the ANAC 2022 competition.

The LLM ...
[] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[X] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.



#### Hypothesis list
This experiment is used for the following hypotheses: hypothesis_1
Your corrected list (empty if correct):

#### Metrics list
The measured metrics in this experiment are: Episodic return, Average obtained utility
Your corrected list (empty if correct): Average obtained utility

#### Statistics
The statistics for the metrics used are: Mean and 99% confidence interval over 10 random seeds.
Your corrected list (empty if correct):

#### Strategy and Test
The experiment strategy is summarised as: The policy is trained for 2,000,000 timesteps, with a new negotiation problem and opponent randomly selected for each episode. Evaluation consists of 1000 negotiation games against each opponent on newly generated random problems. The entire process is repeated for 10 random seeds.
Your corrected answer (empty if correct):

The experiment test is summarised as: Visual comparison of the mean values and their 99% confidence intervals.
Your corrected answer (empty if correct): Visual comparison of the mean Utility values and their 99% confidence intervals.

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

The results of the experiment are as follows:

{
    "Randomly generated negotiation problems with baseline opponents": {
        "Average obtained utility": "The agent performs well, achieving high utility scores against all baseline agents (e.g., ~0.85 against BoulwareAgent and ConcederAgent)."
    },
    "Randomly generated negotiation problems with competition opponents": {
        "Average obtained utility": "The agent's performance is significantly lower and more varied against the full set of opponents. Its average utility against many competitive agents is in the 0.5-0.7 range, and its performance against the baseline agents is also reduced compared to when trained only against them (Figure 5b)."
    }
}

#### General

The LLM has overall captured the experiment details...

[] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[X] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)


### General Experiment Questions

The LLM has provided you with one or more experiments from your work. Is this amount of experiments the same as the amount you specified?

Please write the amount of experiments you had for the study: [2]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Interpretation

Experiment outcomes are analysed and interpreted to determine whether the experiment supports the hypothesis or not. 

The LLM has found the following interpretations of the experiment outcomes;

### interpretation_1

This interpretation has the following description/reasoning:
The results support the first clause of the hypothesis. The authors state on p. 7, 'We can see in Figure 3 that our method performs similarly to the method proposed by Higa et al. (2023). This result is mostly a sanity check that our method can successfully learn to negotiate in a relatively simple setup despite being more complex and broadly usable.' The empirical results show that the proposed GNN-based method is as effective as a specialized state-of-the-art method on a fixed negotiation problem.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

The results support the first clause of the hypothesis. The authors state on p. 7, 'We can see in Figure 3 that our method performs similarly to the method proposed by Higa et al. (2023). This result is mostly a sanity check that our method can successfully learn to negotiate in a relatively simple setup despite being more complex and broadly usable.' The empirical results show that the proposed GNN-based method is as effective as a recent method on a fixed negotiation problem.

This interpretation is for the outcome of the following experiment: experiment_1
Your corrected answer (empty if correct):

Answer this question about the (possibly **corrected!**) experiment_id.
This interpretation of the experiment outcome is ...
[] Correct
[X] Almost correct (few and minor misinterpretations or mistakes)
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
The results support the second clause of the hypothesis, albeit with limitations. The agent demonstrates that it can learn a policy that generalizes to negotiate on never-before-seen problems. As stated on p. 7, 'our method performs well against all baseline agents while negotiating on various structured negotiation problems it has never seen before. It is promising that an end-to-end learned GNN-based policy appears to generalise over such different problems.' However, the authors also note a key limitation: performance drops significantly against a broad set of highly competitive agents (p. 8). This suggests that while the principle of generalization is proven, the quality of the generalized strategy leaves 'room for improvement' against more complex opponents, which the authors attribute to the current feature design's limited ability to adapt to opponent strategies.

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


