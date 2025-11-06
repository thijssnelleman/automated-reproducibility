# Automatic Extraction of Hypothesis: Empirical Analysis of Upper Bounds for Robustness Distributions using Adversarial Attacks
*Aaron Berger, Nils Eberhardt, Annelot W. Bosman, Henning Duwe, Holger H. Hoos, Jan N. van Rijn*


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

The authors hypothesise that adversarial attack methods can yield computationally efficient and tight upper bounds for robustness distributions, comparable in quality to those obtained from a state-of-the-art complete verifier, while highlighting complementarities where attacks achieve near-optimal bounds at a significantly reduced computational cost.

The LLM has provided the following reasoning with this hypothesis:

This hypothesis is implied from statements in the Abstract and Introduction. The Abstract states: '...we demonstrate that adversarial attacks yield computationally efficient and tight upper bounds for robustness distributions.' and 'The results highlight complementarities between verification and attack methods: Attacks achieve near-optimal upper bounds at a significantly reduced computational cost.' The Introduction (Page 2) further elaborates: 'As a cheap alternative to measuring robustness distributions, we propose using adversarial attack methods to determine an upper bound on the ɛ*-values... We empirically show that these approximations provide upper bounds of high quality.'

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

The authors hypothesise that adversarial attack methods can yield computationally efficient and tight upper bounds for robustness distributions, comparable in quality to those obtained from a state-of-the-art complete verifier, while highlighting scenarios where attacks achieve near-optimal bounds at a significantly reduced computational cost.

### General Hypothesis questions

The LLM has provided you with one or more hypothesis from your work. Is this the amount of hypothesis the same as the amount you specified?

Please write the amount of hypothesis you had for the study: [3]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;

We also had a subhypothesis:
1) We assumed that with different strengths of attack, attacks with smaller radius that succeed that attacks with large radius succeeds as well (And found this mostly to be the case with caveats where randomness is included.)
2) We assumed that robustness distribtions are lognormally distributed over larger datasets; Using the cheaper methods we provide new insights on how robustness distributions look.


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
The authors compare multiple adversarial attack methods (FGSM, PGD, AutoAttack, FAB) against a state-of-the-art complete verifier (α, β-CROWN) to compute upper bounds for robustness distributions on several neural networks trained on the MNIST dataset. The comparison is based on the computational cost (running time) and the quality of the obtained bounds (tightness, measured by the minimal adversarial perturbation size p*).

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
The measured metrics in this experiment are: Average running time, Average minimal adversarial perturbation size (p*), Relative Marginal Contribution (RMC), Ratio to the best p* (RB-p*)
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: mean
Your corrected list (empty if correct): Mean for running time and minimal adversarial perturbation size (p*)

#### Strategy and Test
The experiment strategy is summarised as: Evaluation on a test set subset and the complete test set using a binary search algorithm to find the minimal adversarial perturbation.
Your corrected answer (empty if correct):

The experiment test is summarised as: Direct comparison of metric values, Kolmogorov-Smirnov test (p < 0.05)
Your corrected answer (empty if correct):

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

The results of the experiment are as follows:

{
    "MNIST (100 images subset)": {
        "Average running time": {
            "VBA": 290.787,
            "abcrown": 3731.513,
            "autoattack": 20.233,
            "fgsm": 0.047,
            "pgd_40": 0.139,
            "pgd_40_random": 0.143,
            "targeted_fab": 0.333,
            "untargeted_fab": 0.55
        },
        "Average minimal adversarial perturbation size (p*)": {
            "VBA": 0.055,
            "abcrown": 0.055,
            "autoattack": 0.055,
            "fgsm": 0.095,
            "pgd_40": 0.08,
            "pgd_40_random": 0.064,
            "targeted_fab": 0.064,
            "untargeted_fab": 0.058
        },
        "Relative Marginal Contribution (RMC)": {
            "VBA": -,
            "abcrown": 0.066,
            "autoattack": 0.028,
            "fgsm": 0.0,
            "pgd_40": 0.0,
            "pgd_40_random": 0.0,
            "targeted_fab": 0.0,
            "untargeted_fab": 0.003
        },
        "Ratio to the best p* (RB-p*)": {
            "VBA": 1.000,
            "abcrown": 1.005,
            "autoattack": 1.006,
            "fgsm": 1.741,
            "pgd_40": 1.471,
            "pgd_40_random": 1.167,
            "targeted_fab": 1.164,
            "untargeted_fab": 1.052
        }
    },
    "MNIST (Complete test set)": {
        "Average running time": {
            "VBA": 7.316,
            "abcrown": -,
            "autoattack": 19.999,
            "fgsm": 0.046,
            "pgd_40": 0.14,
            "pgd_40_random": 0.142,
            "targeted_fab": 0.451,
            "untargeted_fab": 0.555
        },
        "Average minimal adversarial perturbation size (p*)": {
            "VBA": 0.063,
            "abcrown": -,
            "autoattack": 0.063,
            "fgsm": 0.107,
            "pgd_40": 0.089,
            "pgd_40_random": 0.075,
            "targeted_fab": 0.074,
            "untargeted_fab": 0.069
        },
        "Relative Marginal Contribution (RMC)": {
            "VBA": -,
            "abcrown": -,
            "autoattack": 0.214,
            "fgsm": 0.0,
            "pgd_40": 0.002,
            "pgd_40_random": 0.0,
            "targeted_fab": 0.0,
            "untargeted_fab": 0.003
        },
        "Ratio to the best p* (RB-p*)": {
            "VBA": 1.000,
            "abcrown": -,
            "autoattack": 1.002,
            "fgsm": 1.695,
            "pgd_40": 1.407,
            "pgd_40_random": 1.184,
            "targeted_fab": 1.171,
            "untargeted_fab": 1.092
        }
    }
}

#### General

The LLM has overall captured the experiment details...

[] Very well (No major mistakes and/or missing information)
[X] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)


### General Experiment Questions

The LLM has provided you with one or more experiments from your work. Is this amount of experiments the same as the amount you specified?

Please write the amount of experiments you had for the study: [2]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;

The attack monotonicity experiment is missing.


## Interpretation

Experiment outcomes are analysed and interpreted to determine whether the experiment supports the hypothesis or not. 

The LLM has found the following interpretations of the experiment outcomes;

## interpretation_1

This interpretation has the following description/reasoning:
The results support the hypothesis. The authors show that adversarial attacks are significantly more computationally efficient than complete verification while providing tight upper bounds. 
1. **Computational Efficiency**: Table 1 (page 11) shows that attack methods are orders of magnitude faster. For the 100-image subset, the verifier `abcrown` took ~3731s on average, while `autoattack` took ~20s. The paper states this is 'two to four magnitudes smaller' (Page 9).
2. **Tightness of Bounds**: The best attack methods, like AutoAttack, produce bounds very close to the verifier. On the 100-image subset, `autoattack` and `abcrown` found the same average p* (0.055), and their RB-p* values were 1.006 and 1.005 respectively, indicating near-optimal performance. The paper notes that 'α, β-CROWN and AutoAttack obtain the same p* on 89% of the instances' (Page 10). The CDF plots in Figure 1 (page 10) also visually confirm the similarity.
3. **Complementarity**: The results show a trade-off. While the verifier provides formal guarantees, attacks provide fast and accurate estimations. The paper highlights that neither method is strictly dominant in finding the smallest perturbation in all cases: 'AutoAttack found a smaller p* for 4.3% of the instances and for 6.3% of the instances α, β-CROWN found a smaller p*' (Page 10). This demonstrates the complementarity and the value of attacks for large-scale analysis where verification is infeasible.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

The results show a trade-off. While the verifier provides formal guarantees, attacks provide fast and accurate estimations. The paper highlights that neither method is strictly dominant in finding the smallest perturbation in all cases: 'AutoAttack found a smaller p* for 4.3% of the instances and for 6.3% of the instances α, β-CROWN found a smaller p*' (Page 10). This demonstrates the complementarity and the value of attacks for large-scale analysis where verification is infeasible. Further, for the other attacks, α, β-CROWN strictly dominate the attacks in terms of accuracy, but require longer computation times.

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


