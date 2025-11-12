# Automatic Extraction of Hypothesis: carps: A Framework for Comparing N Hyperparameter Optimizers on M Benchmarks
*Carolin Benjamins, Helena Graf, Sarah Segel, Difan Deng, Tim Ruhkopf, Leona Hennig, Soham Basu, Neeratyoy Mallik, Edward Bergman, Deyao Chen, François Clément, Alexander Tornede, Matthias Feurer, Katharina Eggensperger, Frank Hutter, Carola Doerr, Marius Lindauer*


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

The authors hypothesise that the representative subsets of HPO benchmark tasks, created by minimizing the star discrepancy in the performance space, will yield consistent relative performance rankings of HPO optimizers across the disjoint development and test sets.

The LLM has provided the following reasoning with this hypothesis:

The paper proposes a method to create representative subsets of HPO tasks to make benchmarking more efficient and less biased. A key feature is the creation of disjoint development (dev) and test sets (Abstract, Section 7). The authors then empirically validate this methodology by comparing the performance of optimizers across these sets. The implied hypothesis is that if the subsets are truly representative and useful, the relative performance of optimizers should be stable between the dev and test sets. This validation is explicitly mentioned in Appendix H.2: 'In order to validate that the ranking remains consistent across the subsets, we calculate the rank the same way as described in Section 8.1 for each task type and then determine the order. The following tables [...] show that the ranking is consistent across the subsets for each task type.' This shows a clear intent to empirically test the consistency of rankings between the created subsets.

Please grade the hypothesis stated from the following options:

The LLM ...

[] captures the hypothesis (nearly) perfectly.

[] has stated a hypothesis capturing the general spirit of our work.

[X] has stated an incomplete hypothesis; the answer is correct but is missing key information.

[] has stated the general hypothesis but has introduced false or incorrect information.

[] has stated a hypothesis similar to ours, but is far too innaccurate to consider correct.

[] has stated a hypothesis that has (nearly) no overlap with our work.

[] has stated a hypothesis of lesser quality than described above: If it is an hallucination, please explain below.



Based on the LLMs answer, would you like to improve the answer to more accurately capture the hypothesis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

The authors hypothesise that the representative subsets of HPO benchmark tasks, created by minimizing the star discrepancy in the performance space, will yield consistent relative performance rankings of HPO optimizers across the disjoint development and test sets. The design criterium for the subsets selection of different hyperparameters itself is to yield the same performance rankings across the subsets of the optimisers producing the data; any optimiser comparison will show the same ranking on those sets.

### General Hypothesis questions

The LLM has provided you with one or more hypothesis from your work. Is this the amount of hypothesis the same as the amount you specified?

Please write the amount of hypothesis you had for the study: [2]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;
hypothesis_2: On the subsets, we can observe different performance rankings for different optimisers.


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
A selection of representative HPO optimizers are run on the proposed development and test subsets for four different HPO task types (blackbox, multi-fidelity, multi-objective, and multi-fidelity-multi-objective). The final performance of each optimizer on each task is recorded. These performances are then used to compute the mean rank of each optimizer across the tasks within each subset. Finally, the rank ordering of optimizers is compared between the development and test set for each task type to assess consistency.

The LLM ...
[] has described the experiment (nearly) perfectly
[X] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.



#### Hypothesis list
This experiment is used for the following hypotheses: hypothesis_1
Your corrected list (empty if correct):

#### Metrics list
The measured metrics in this experiment are: mean rank
Your corrected list (empty if correct): Performance of optimiser (Final incumbant cost)

#### Statistics
The statistics for the metrics used are: mean rank
Your corrected list (empty if correct): Mean

#### Strategy and Test
The experiment strategy is summarised as: Each optimizer is run on each task for 20 random seeds. The optimization budget is n_trials = [20 + 40 * sqrt(d)], where d is the dimensionality of the task's configuration space.
Your corrected answer (empty if correct):

The experiment test is summarised as: Friedman test, Nemenyi test (α = 0.05), Qualitative comparison of rank ordering
Your corrected answer (empty if correct): Friedman test, Nemenyi test (α = 0.05), Quantitative comparison of rank ordering

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

The results of the experiment are as follows:

{
    "carps blackbox dev subset": {
        "mean rank": {
            "Nevergrad-CMA-ES": 1.65,
            "SMAC3-BlackBoxFacade": 1.65,
            "RandomSearch": 2.7
        }
    },
    "carps blackbox test subset": {
        "mean rank": {
            "SMAC3-BlackBoxFacade": 1.5,
            "Nevergrad-CMA-ES": 1.82,
            "RandomSearch": 2.67
        }
    },
    "carps multi-fidelity dev subset": {
        "mean rank": {
            "SMAC3-MultiFidelityFacade": 1.35,
            "DEHB": 2.23,
            "SMAC3-Hyperband": 2.42
        }
    },
    "carps multi-fidelity test subset": {
        "mean rank": {
            "SMAC3-MultiFidelityFacade": 1.57,
            "DEHB": 2.15,
            "SMAC3-Hyperband": 2.27
        }
    },
    "carps multi-objective dev subset": {
        "mean rank": {
            "Optuna-MO-TPE": 1.3,
            "Nevergrad-DE": 2.2,
            "RandomSearch": 2.5
        }
    },
    "carps multi-objective test subset": {
        "mean rank": {
            "Nevergrad-DE": 1.7,
            "Optuna-MO-TPE": 1.8,
            "RandomSearch": 2.5
        }
    },
    "carps multi-fidelity-objective dev subset": {
        "mean rank": {
            "SMAC3-MOMF-GP": 1.56,
            "RandomSearch": 1.78,
            "Nevergrad-DE": 2.67
        }
    },
    "carps multi-fidelity-objective test subset": {
        "mean rank": {
            "SMAC3-MOMF-GP": 1.44,
            "RandomSearch": 2.0,
            "Nevergrad-DE": 2.56
        }
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
experiment_2: In figure 5 & 6 & 7 we report the main results of our benchmarking study

## Interpretation

Experiment outcomes are analysed and interpreted to determine whether the experiment supports the hypothesis or not. 

The LLM has found the following interpretations of the experiment outcomes;

### interpretation_1

This interpretation has the following description/reasoning:
The authors conclude that the rankings are consistent across the development and test subsets, thus supporting the hypothesis. Their reasoning, presented in Appendix H.2 and Section 8.2, is that for most task types, the rank ordering of optimizers remains stable. For example, for the multi-fidelity task type (Table 6), the rank order is identical between the dev and test sets. The authors acknowledge that for some task types, like multi-objective, the ranks of the top two optimizers flip (Table 8). However, they argue this does not invalidate the result because the statistical tests (Friedman/Nemenyi) show that the performance differences between these optimizers on the test set are not significant (Table 8, 'significant' column is 'no'). Therefore, they conclude that where ranks are stable, the hypothesis is supported, and where they are not, the underlying performance differences are negligible, meaning the subsets are still behaving as expected.

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


