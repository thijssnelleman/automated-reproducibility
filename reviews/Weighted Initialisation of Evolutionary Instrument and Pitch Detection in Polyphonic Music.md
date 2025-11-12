# Automatic Extraction of Hypothesis: Weighted Initialisation of Evolutionary Instrument and Pitch Detection in Polyphonic Music
*Justin Dettmer, Igor Vatolkin, Tobias Glasmachers*


You will be presented with the output of an LLM which was tasked to extract the hypothesis from your paper, including the experiment used to test the hypothesis and the interpretation of the outcome of the experiment.

We ask you to **open your PDF** that was presented to the LLM, to reflect upon the LLM's answer with your paper.

The answer of the LLM is structured into three parts; Hypothesis, experiments and interpretation (of experiment outcome).
- For each experiment the LLM has linked it to one or more hypothesis
- For each interpretation, the LLM has linked it to **one** experiment and **one** hypothesis.

The LLM has been tasked to extract a hypothesis **including an expected outcome**. This may not always be the case for each study; it should be interpreted as a post-hoc hypothesis.

Please answer the following questions:

## Hypotheses

### hypothesis_1

The LLM has found the following **implied** hypothesis:

The authors hypothesise that modifying an evolutionary algorithm for polyphonic music approximation by using spectral information to initialise populations with probable pitches will result in significantly faster convergence speed and slightly improved pitch and instrument detection errors compared to the baseline algorithm with random initialisation.

The LLM has provided the following reasoning with this hypothesis:

The hypothesis is implied. The abstract introduces a modification to an evolutionary algorithm that 'uses spectral information to initialise populations with probable pitches'. It then states the expected outcome: 'our modification still shows significantly faster convergence speed and slightly improved pitch and instrument detection errors over the baseline algorithm on both single onset and full piece experiments.' (Abstract, page 1). This establishes a clear comparison between their proposed method and a baseline, with expected quantitative improvements.

Please grade each hypothesis stated from the following options:

The LLM ...

[] captures the hypothesis (nearly) perfectly.

[X] has stated a hypothesis capturing the general spirit of our work.

[] has stated an incomplete hypothesis; The answer is correct but is missing key information.

[] has stated the general hypothesis but has introduced false or incorrect information.

[] has stated a hypothesis similar to ours, but is far too innaccurate to consider correct.

[] has stated a hypothesis that has (nearly) no overlap with our work.

[] has stated a hypothesis of lesser quality than described above: If it is an hallucination, please explain below.



Based on the LLMs answer, would you like to improve the answer to more accurately capture the hypothesis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

The authors hypothesise that modifying an evolutionary algorithm for polyphonic music approximation by using spectral information to initialise populations with probable pitches will result in significantly faster convergence speed and improved pitch and instrument detection errors compared to the baseline algorithm with random initialisation.


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
The baseline and modified evolutionary algorithms are run on a dataset of 1000 single-onset polyphonic audio mixes where the ground truth is known and perfectly reproducible. The goal is to measure the algorithms' ability to find the global optimum and to compare their convergence speed and final detection errors.

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has stated the experiment but has introduced false information or made mistakes
[] has stated the experiment but has nearly no overlap with our work
[] Other. If it has hallucinated, please describe below.



#### Hypothesis list
This experiment is used for the following hypotheses: hypothesis_1
Your corrected list (empty if correct):

#### Metrics list
The measured metrics in this experiment are: Jaccard error for instrument classes (Ji), Jaccard error for pitch classes (Jp), Jaccard error for joint instrument-pitch tuples (Jip)
Your corrected list (empty if correct): Jaccard error for instrument classes (Ji), Jaccard error for pitch classes (Jp), Jaccard error for joint instrument-pitch tuples (Jip), Mean Fitness

#### Statistics
The statistics for the metrics used are: Mean error across 1000 target examples, plotted over generations.
Your corrected list (empty if correct):

#### Strategy and Test
The experiment strategy is summarised as: Each algorithm is run once for all 1000 targets for up to 10000 generations. The experiment terminates early for a target if an individual with zero fitness is found. (Section 5.2, page 8).
Your corrected answer (empty if correct):

The experiment test is summarised as: Visual comparison of the mean error curves over 10000 generations between the baseline algorithm (Fig. 4) and the modified algorithm (Fig. 6).
Your corrected answer (empty if correct):

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom.

The results of the experiment are as follows:

{
    "Ground Truth Search Dataset (This work)": {
        "Jaccard error for instrument classes (Ji)": "Baseline converges to ~0.21. Modified converges to a similar value but with a steeper initial descent.",
        "Jaccard error for pitch classes (Jp)": "Baseline converges to ~0.18. Modified starts much lower (~0.65 vs ~1.0), has a small initial increase, then converges to a similar value as the baseline but faster.",
        "Jaccard error for joint instrument-pitch tuples (Jip)": "Baseline converges to ~0.23. Modified converges to a similar value but with a steeper initial descent."
    }
}

#### General

The LLM has overall captured the experiment details...

[X] Very well (No major mistakes and/or missing information)
[] Well (Some missing information and/or minor mistakes)
[] Okay (Substantial missing information and/or mistakes)
[] Poorly (Severe missing information and/or mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)

### experiment_2

The LLM describes this experiment as follows:
The baseline and modified evolutionary algorithms are run on a dataset of 20 full, artificially created musical pieces to evaluate performance on a more realistic, complex task. The experiment compares initial errors, convergence speed, and final errors after 10000 generations.

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has stated the experiment but has introduced false information or made mistakes
[] has stated the experiment but has nearly no overlap with our work
[] Other. If it has hallucinated, please describe below.



#### Hypothesis list
This experiment is used for the following hypotheses: hypothesis_1
Your corrected list (empty if correct):

#### Metrics list
The measured metrics in this experiment are: Jaccard error for instrument classes (Ji), Jaccard error for pitch classes (Jp), Jaccard error for joint instrument-pitch tuples (Jip)
Your corrected list (empty if correct): Jaccard error for instrument classes (Ji), Jaccard error for pitch classes (Jp), Jaccard error for joint instrument-pitch tuples (Jip), Mean Fitness

#### Statistics
The statistics for the metrics used are: Mean error across 20 repeated runs per piece, plotted over generations.
Your corrected list (empty if correct):

#### Strategy and Test
The experiment strategy is summarised as: Each experiment is repeated 20 times for a total of 10000 generations. Population size is increased to 300. (Section 5.3, page 8).
Your corrected answer (empty if correct):

The experiment test is summarised as: Visual comparison of the mean error curves over 10000 generations between the baseline algorithm (dotted lines) and the modified algorithm (solid lines) in Fig. 8.
Your corrected answer (empty if correct): Visual and numerical comparison of the mean error curves over 10000 generations between the baseline algorithm (dotted lines) and the modified algorithm (solid lines) in Fig. 8.

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom.

The results of the experiment are as follows:

{
    "Artificial Audio Multitracks (AAM) dataset [30]": {
        "Jaccard error for instrument classes (Ji)": "Modified algorithm shows lower initial error and slightly lower final error compared to baseline.",
        "Jaccard error for pitch classes (Jp)": "Modified algorithm shows lower initial error and slightly lower final error compared to baseline.",
        "Jaccard error for joint instrument-pitch tuples (Jip)": "Modified algorithm shows lower initial error and slightly lower final error compared to baseline."
    }
}

#### General

The LLM has overall captured the experiment details...

[] Very well (No major mistakes and/or missing information)
[] Well (Some missing information and/or minor mistakes)
[X] Okay (Substantial missing information and/or mistakes)
[] Poorly (Severe missing information and/or mistakes)
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
The results support the hypothesis regarding faster convergence. The authors state that 'the slopes in the first few thousand generations are steeper in our modified algorithm,' which means it converges faster. They conclude, 'In cases where there is not ample time to run the algorithm for the full 10000 generations, using our proposed method will provide better detection upon early termination.' (Section 6.1, page 9). While the final errors are described as 'comparable', the significant improvement in convergence speed supports a key part of the hypothesis.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

The results support the hypothesis regarding faster convergence. The authors state that 'the slopes in the first few thousand generations are steeper in our modified algorithm,' which means the error decreases faster. They conclude, 'In cases where there is not ample time to run the algorithm for the full 10000 generations, using our proposed method will provide better detection upon early termination.' (Section 6.1, page 9). While the final errors are described as 'comparable', the significant improvement in convergence speed supports a key part of the hypothesis.

This interpretation is for the outcome of the following experiment: experiment_1
Your corrected answer (empty if correct):

Answer this question about the (possibly **corrected!**) experiment_id.
This interpretation of the experiment outcome is ...
[] Representative
[] Adequate
[] Acceptable
[X] (Partially) Incorrect
[] Incorrect
[] Hallucinatory, if so explain below:



This interpretation is to support (or not) the following hypothesis: hypothesis_1
Your corrected answer (empty if correct):

This interpretation supports the hypothesis: True
Your corrected answer (empty if correct):

### interpretation_2

This interpretation has the following description/reasoning:
The results support both parts of the hypothesis. The authors observe 'lower initial errors for all three error classes' and 'a slight improvement in errors after convergence for the modified algorithm' (Section 6.2, page 11). The lower initial errors and faster initial descent support the 'faster convergence' claim. The slightly lower final errors support the 'slightly improved detection errors' claim. The authors conclude that 'even its slight improvements in converged errors makes it a useful addition regardless.' (Section 6.2, page 11).

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

The results support both parts of the hypothesis. The authors observe 'lower initial errors for all three error classes' and 'a slight improvement in errors after convergence for the modified algorithm' (Section 6.2, page 11). The slightly lower final errors support the 'slightly improved detection errors' claim. The authors conclude that 'even its slight improvements in converged errors makes it a useful addition regardless.' (Section 6.2, page 11).

This interpretation is for the outcome of the following experiment: experiment_2
Your corrected answer (empty if correct):

Answer this question about the (possibly **corrected!**) experiment_id.
This interpretation of the experiment outcome is ...
[] Representative
[] Adequate
[] Acceptable
[X] (Partially) Incorrect
[] Incorrect
[] Hallucinatory, if so explain below:



This interpretation is to support (or not) the following hypothesis: hypothesis_1
Your corrected answer (empty if correct):

This interpretation supports the hypothesis: True
Your corrected answer (empty if correct):


