# Automatic Extraction of Hypothesis: Examining the robustness of Physics-Informed Neural Networks to noise for Inverse Problems
*Aleksandra Jekic, Afroditi Natsaridou, Signe Riemer-Sørensen, Helge Langseth, Odd Erik Gundersen*

You will be presented with the output of an LLM which was tasked to extract the hypothesis from your paper, including the experiment used to test the hypothesis and the interpretation of the outcome of the experiment.

We ask you to **open your PDF** that was presented to the LLM, to reflect upon the LLM's answer with your paper.

The answer of the LLM is structured into three parts; Hypothesis, experiments and interpretation (of experiment outcome).

- For each experiment the LLM has linked it to one or more hypothesis
- For each interpretation, the LLM has linked it to **one** experiment and **one** hypothesis.

The LLM has been tasked to extract a hypothesis **including an expected outcome**. This may not always be the case for each study; it should be interpreted as a post-hoc hypothesis.

Please answer the questions in the following sections.

## Hypotheses

### hypothesis_1

The LLM has found the following **implied** hypothesis:

The authors hypothesise that a traditional approach combining the Finite Element Method (FEM) with a numerical optimizer outperforms Physics-Informed Neural Networks (PINNs) on noisy inverse problems.

The LLM has provided the following reasoning with this hypothesis:

The hypothesis is implied in the abstract and introduction. The abstract states: "We compare the performance of PINNs in solving inverse problems with that of a traditional approach using the finite element method combined with a numerical optimizer... We find that while PINNs may require less human effort and specialized knowledge, they are outperformed by the traditional approach." (Page 1). Section 1.1 further clarifies the goal: "Our purpose is to compare PINNs to a similarly easily accessible but reasonable choice of standard methods, without extensive tuning." (Page 2).

Please grade the hypothesis stated from the following options:

The LLM ...

[] captures the hypothesis (nearly) perfectly.

[] has stated a hypothesis capturing the general spirit of our work.

[] has stated an incomplete hypothesis; the answer is correct but is missing key information.

[] has stated the general hypothesis but has introduced false or incorrect information.

[X] has stated a hypothesis similar to ours, but is far too innaccurate to consider correct.

[] has stated a hypothesis that has (nearly) no overlap with our work.

[] has stated a hypothesis of lesser quality than described above: If it is an hallucination, please explain below.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the hypothesis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

If we compare their performance we may gain new insights into the properties of PINNs.

(The LLM insinuates that the researchears had an initial preference of models, which is not true).

### hypothesis_2

The LLM has found the following **implied** hypothesis:

The authors hypothesise that the performance gap between PINNs and the traditional FEM-based approach decreases as the problem dimensionality and the amount of available data increase.

The LLM has provided the following reasoning with this hypothesis:

This hypothesis is implied in the abstract and conclusion. The abstract states: "However, the difference appears to decrease with higher dimensions and more data." (Page 1). The conclusion reinforces this: "We have also found that relative to the baseline, the loss-based physics regularization appears to work better when more training data is available and that PINNs scale better with more difficult problems." (Page 21).

Please grade the hypothesis stated from the following options:

The LLM ...

[] captures the hypothesis (nearly) perfectly.

[] has stated a hypothesis capturing the general spirit of our work.

[] has stated an incomplete hypothesis; the answer is correct but is missing key information.

[] has stated the general hypothesis but has introduced false or incorrect information.

[X] has stated a hypothesis similar to ours, but is far too innaccurate to consider correct.

[] has stated a hypothesis that has (nearly) no overlap with our work.

[] has stated a hypothesis of lesser quality than described above: If it is an hallucination, please explain below.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the hypothesis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

The authors hypothesise that the performance of PINNs improve as the problem dimensionality and the amount of available data increase.

(The stated hypothesis is to strong, it implies a to simple and linear relation between performance gaps)

### General Hypothesis questions

The LLM has provided you with one or more hypothesis from your work. Is this the amount of hypothesis the same as the amount you specified?

Please write the amount of hypothesis you had for the study: [1]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;

The second hypothesis was related to insights from observations of the results.

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
Solving the inverse problem for the 1D Burgers' equation to identify the viscosity parameter (ν). The experiment is run with 30 random initializations for various levels of Gaussian noise (σ) added to the training data.

The LLM ...
[] has described the experiment (nearly) perfectly
[X] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

Lacking info about data, used parameters and setup.

#### Hypothesis list

This experiment is used for the following hypotheses: hypothesis_1, hypothesis_2
Your corrected list (empty if correct): hypothesis_1

#### Metrics list

The measured metrics in this experiment are: Prediction accuracy (RMSE), Parameter accuracy
Your corrected list (empty if correct): Prediction accuracy (RMSE), Parameter accuracy, MSE

#### Statistics

The statistics for the metrics used are: Mean and standard deviation over 30 runs, visualized with error bars in plots.
Your corrected list (empty if correct): Mean and standard deviation over 30 runs, visualized with error bars in plots. Loss history.

#### Strategy and Test

The experiment strategy is summarised as: Random split (training = 10%, validation = 2%, test = 88%)
Your corrected answer (empty if correct): Random split (training = 10%, validation = 2%, test = 88%), loss history not included

The experiment test is summarised as: Visual comparison of mean values and standard deviation error bars in plots.
Your corrected answer (empty if correct): Visual and numerical comparison of mean values and standard deviation error bars in plots. Loss history.

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

Author comment: Missing reward hacking phenomena. The results are superficial and lacking in detail.

The results of the experiment are as follows:

{
    "1D Burgers' equation data (Raissi et al. 2019)": {
        "Prediction accuracy (RMSE)": "Without noise (σ=0), PINN slightly outperforms the FEM-based models. With increasing noise, FEM/SLSQP generally has a lower mean RMSE, but the authors state the difference is not significant as the standard deviations overlap (Figure 1, Page 10).",
        "Parameter accuracy": "FEM/SLSQP tends to estimate higher than the ground truth. PINN on average estimates lower up to σ=3. For most noise levels, FEM/SLSQP is closer to the ground truth on average (Figure 1, Page 10)."
    }
}

#### General

The LLM has overall captured the experiment details...

[] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[X] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)

### experiment_2

The LLM describes this experiment as follows:
Solving the inverse problem for the 2D Taylor-Green vortex (Navier-Stokes equations) to identify the viscosity parameter (ν). The experiment is run with 5 random initializations for various levels of Gaussian noise (σ) added to the training data.

The LLM ...
[] has described the experiment (nearly) perfectly
[X] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

Lacking info about data, used parameters and setup.

#### Hypothesis list

This experiment is used for the following hypotheses: hypothesis_1, hypothesis_2
Your corrected list (empty if correct): hypothesis_1

#### Metrics list

The measured metrics in this experiment are: Prediction accuracy (RMSE), Parameter accuracy
Your corrected list (empty if correct): Prediction accuracy (RMSE), Parameter accuracy, MSE

#### Statistics

The statistics for the metrics used are: Mean and standard deviation over 5 runs, visualized with error bars in plots.
Your corrected list (empty if correct): Mean and standard deviation over 5 runs, visualized with error bars in plots. Loss history.

#### Strategy and Test

The experiment strategy is summarised as: Random split (training ≈ 1.26%, validation ≈ 0.25%, test ≈ 98.49%)
Your corrected answer (empty if correct): Random split (training ≈ 1.26%, validation ≈ 0.25%, test ≈ 98.49%). Loss history.

The experiment test is summarised as: Visual comparison of mean values and standard deviation error bars in plots.
Your corrected answer (empty if correct): Visual and numerical comparison of mean values and standard deviation error bars in plots. Loss history.

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

Author comment: The results are superficial and lacking in detail.

The results of the experiment are as follows:

{
    "2D Taylor-Green vortex data (This work)": {
        "Prediction accuracy (RMSE)": "The FEM/SLSQP model consistently outperforms both PINN models (pure PINN and PINN/FEM) across all tested noise levels (Figure 3, Page 13).",
        "Parameter accuracy": "The FEM/SLSQP model provides estimates that are much closer to the ground truth and more stable. PINN models show a tendency to estimate a lower viscosity, and their performance degrades significantly with higher noise (Figure 3, Page 13)."
    }
}

#### General

The LLM has overall captured the experiment details...

[] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[X] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)

### experiment_3

The LLM describes this experiment as follows:
Solving the inverse problem for the 3D Taylor-Green vortex (Navier-Stokes equations) to identify the viscosity parameter (ν). The experiment is run with 5 random initializations for various levels of Gaussian noise (σ) added to the training data.

The LLM ...
[] has described the experiment (nearly) perfectly
[X] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

Lacking info about data, used parameters and setup.

#### Hypothesis list

This experiment is used for the following hypotheses: hypothesis_1, hypothesis_2
Your corrected list (empty if correct):

#### Metrics list

The measured metrics in this experiment are: Prediction accuracy (RMSE), Parameter accuracy
Your corrected list (empty if correct): Prediction accuracy (RMSE), Parameter accuracy, MSE

#### Statistics

The statistics for the metrics used are: Mean and standard deviation over 5 runs, visualized with error bars in plots.
Your corrected list (empty if correct): Mean and standard deviation over 5 runs, visualized with error bars in plots. Loss history.

#### Strategy and Test

The experiment strategy is summarised as: Random split (training ≈ 27.3%, validation ≈ 9.1%, test ≈ 63.6%)
Your corrected answer (empty if correct): Random split (training ≈ 27.3%, validation ≈ 9.1%, test ≈ 63.6%). Loss history.

The experiment test is summarised as: Visual comparison of mean values and standard deviation error bars in plots.
Your corrected answer (empty if correct): Visual and numerical comparison of mean values and standard deviation error bars in plots. Loss history.

#### Results

The LLM has found results for the experiment and they are summarised in a table below. For each cell in the table, please update the values if they are incorrect. If values are missing or should be seperated, please add new rows at the bottom. If a JSON structure is shown, please adapt the values behind each key if incorrect, and if values are missing add keys accordingly.

Author comment: The results are superficial and lacking in detail.

The results of the experiment are as follows:

{
    "3D Taylor-Green vortex data (This work)": {
        "Prediction accuracy (RMSE)": "FEM/SLSQP is overall better than PINN, but the performance gap is smaller compared to the 2D experiment. The results even out more as noise is added (Figure 5, Page 17).",
        "Parameter accuracy": "FEM/SLSQP is generally closer to the ground truth. The PINN model still has a tendency to estimate the viscosity as lower than the ground truth (Figure 5, Page 17)."
    }
}

#### General

The LLM has overall captured the experiment details...

[] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[X] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)

### General Experiment Questions

The LLM has provided you with one or more experiments from your work. Is this amount of experiments the same as the amount you specified?

Please write the amount of experiments you had for the study: [3]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;

## Interpretation

Experiment outcomes are analysed and interpreted to determine whether the experiment supports the hypothesis or not.

The LLM has found the following interpretations of the experiment outcomes;

### interpretation_1

This interpretation has the following description/reasoning:
The results from the experiments collectively support the hypothesis. While the performance difference in the 1D case was not significant, the FEM/SLSQP baseline was clearly superior in the more complex 2D and 3D problems. The authors conclude: "Through three different experiments, we have observed that a simple baseline using FEM and an optimizer, largely outperforms PINNs on noisy inverse problems." (Section 6, Page 20).

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?

- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

The results from the experiments collectively support the hypothesis. While the performance difference in the 1D case was not significant, the FEM/SLSQP baseline was clearly superior in the more complex 2D problems. Differences where less clear in 3D. The authors conclude: "Through three different experiments, we have observed that a simple baseline using FEM and an optimizer, largely outperforms PINNs on noisy inverse problems." (Section 6, Page 20).

This interpretation is for the outcome of the following experiment: ['experiment_1', 'experiment_2', 'experiment_3']
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
The hypothesis is supported by comparing the results across the three experiments. The performance gap between the FEM baseline and PINNs was largest in the 2D case. In the 3D case, which used a significantly larger proportion of training data, the gap narrowed. The authors state, "Relative to FEM/SLSQP, PINN performs better with higher noise in 3D. This is likely due to the much larger amount of training data." (Page 17). They conclude that "PINNs scale better with more difficult problems. This is consistent with findings in existing literature" (Page 21).

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?

- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

This interpretation is for the outcome of the following experiment: ['experiment_1', 'experiment_2', 'experiment_3']
Your corrected answer (empty if correct):

Answer this question about the (possibly **corrected!**) experiment_id.
This interpretation of the experiment outcome is ...
[X] Correct
[] Almost correct (few and minor misinterpretations or mistakes)
[] Acceptable (some misinterpretations or mistakes)
[] (Partially) Incorrect (serious misinterpretations or mistakes)
[] Incorrect
[] Hallucinatory, if so explain below:

This interpretation is to support (or not) the following hypothesis: hypothesis_2
Your corrected answer (empty if correct):

This interpretation supports the hypothesis: True
Your corrected answer (empty if correct):
