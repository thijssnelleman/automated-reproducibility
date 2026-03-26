# Automatic Extraction of Study Representation: DATA EFFICIENT PRE-TRAINING FOR LANGUAGE MODELS: AN EMPIRICAL STUDY OF COMPUTE EFFICIENCY AND LINGUISTIC COMPETENCE
*Andreas Paraskeva, Max Johannes van Duijn, Maarten de Rijke, Suzan Verberne, Jan N. van Rijn*


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

How do dataset size, complexity, and sampled domains (specifically narrative vs. open-domain) influence formal and functional linguistic competence when pre-training small language models?

The LLM has provided the following reasoning with this research question:

Implied in the Introduction and Section 1 (Contributions): 'These contributions amount to a better understanding of how dataset size, complexity, and sampled domains influence linguistic competence when pre-training language models...'

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

How do dataset size, complexity, and sampled domains (specifically synthetic narrative vs. human source open-domain) influence formal and functional linguistic competence when pre-training small language models?

### research_question_2

The LLM has found the following **implied** research question:

How do these dataset differences impact the compute efficiency and practical deployment of the models?

The LLM has provided the following reasoning with this research question:

Implied in the Introduction and Section 1 (Contributions): '...and how they impact practical applications of compute efficiency and model deployment.'

Please grade the research question stated from the following options:

The LLM ...
[] captures the research question (nearly) perfectly.
[] has stated a research question capturing the general spirit of our work.
[X] has stated an incomplete research question; the answer is correct but is missing key information.
[] has stated a general research question but has introduced false or incorrect information.
[] has stated a research question similar to ours, but is far too innaccurate to consider correct.
[] has stated a research question that has (nearly) no overlap with our work.
[] has stated a research question of lesser quality than described above: If it is an hallucination, please explain below.


Based on the LLMs answer, would you like to improve the answer to more accurately capture the research question?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

How do these dataset differences impact the compute efficiency of the models and model performance throughout the pre-training life cycle?

### General Research Questions questions

The LLM has provided you with one or more research questions from your work. Is this the amount of research questions the same as the amount you specified or implied?

Please write the amount of research questions you had for the study: [2]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Hypotheses

### hypothesis_1

The LLM has found the following **implied** hypothesis:

The authors hypothesise that pre-training small language models on diverse, open-domain data (BabyLM) yields better formal and functional linguistic competence and more consistent performance than pre-training on simple, synthetic narrative data (TinyStories).

The LLM has provided the following reasoning with this hypothesis:

Implied from the experimental setup comparing the two datasets and the statement in the contributions (Section 1): 'We show that models trained on BabyLM achieve significantly higher performance on formal linguistic competence and show lower variance...'

The LLM has linked the hypothesis to the following research questions: research_question_1
Your corrected list (empty if correct):

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

The authors hypothesise that pre-training small language models on diverse, open-domain data (BabyLM) yields better formal linguistic competence and more consistent performance than pre-training on simple, synthetic narrative data (TinyStories).

### hypothesis_2

The LLM has found the following **implied** hypothesis:

The authors hypothesise that early performance metrics on small data samples (token-based anchors) are representative of a model's ultimate performance, enabling early discarding of unpromising candidate models.

The LLM has provided the following reasoning with this hypothesis:

Implied from the contributions (Section 1): 'We demonstrate that early performance metrics can be used in model selection, allowing us to discard unpromising candidate models.'

The LLM has linked the hypothesis to the following research questions: research_question_2
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

The authors hypothesise that early performance metrics on small data samples (token-based anchors) are representative of a model's ultimate performance, potentially enabling early discarding of unpromising candidate models.

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
Pre-training Llama-based decoder-only models of three sizes (17M, 58M, 91M) from scratch on progressively larger token-based anchors of the BabyLM and TinyStories datasets, and evaluating them on the BLiMP benchmark without fine-tuning to assess formal linguistic competence.

The LLM ...
[X] has described the experiment (nearly) perfectly
[] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

The LLM has found the following strategy or protocol for the experiment: Token-based anchors using a geometric sampling scheme ([2, 4, 8, 16, 32, 64, 96, 128, 160] million tokens). 3 repetitions per anchor-model-dataset combination.
Your corrected answer (empty if correct):

The LLM has found the following data (sets) used as input for the experiment: BabyLM-100m (Choshen et al., 2024), TinyStories (Eldan & Li, 2023), BLiMP benchmark (Warstadt et al., 2020)
Your corrected answer (empty if correct):

This experiment is used to answer the following research questions: research_question_1, research_question_2
Your corrected list (empty if correct):

This experiment is used for the following hypotheses: hypothesis_1, hypothesis_2
Your corrected list (empty if correct):

### experiment_2

The LLM describes this experiment as follows:
Pre-training the same Llama-based models on the same token-based anchors of BabyLM and TinyStories, followed by supervised fine-tuning on individual tasks from a subset of the GLUE benchmark to assess functional linguistic competence.

The LLM ...
[] has described the experiment (nearly) perfectly
[X] has described the experiment but is lacking information
[] has described the experiment but has introduced false information or made mistakes
[] has described an experiment which has nearly no overlap with that found in our work
[] Other. If it has hallucinated, please describe below.

The LLM has found the following strategy or protocol for the experiment: Token-based anchors using a geometric sampling scheme ([2, 4, 8, 16, 32, 64, 96, 128, 160] million tokens). 3 repetitions per anchor-model-dataset combination. Fine-tuning on individual GLUE tasks.
Your corrected answer (empty if correct):

The LLM has found the following data (sets) used as input for the experiment: BabyLM-100m (Choshen et al., 2024), TinyStories (Eldan & Li, 2023), GLUE benchmark subset (Wang et al., 2019b)
Your corrected answer (empty if correct):

This experiment is used to answer the following research questions: research_question_1, research_question_2
Your corrected list (empty if correct):

This experiment is used for the following hypotheses: hypothesis_1, hypothesis_2
Your corrected list (empty if correct):


### General Experiment Questions

The LLM has provided you with one or more experiments from your work. Is this amount of experiments the same as the amount you specified?

Please write the amount of experiments you had for the study: [2]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Analysis

The LLM has found one or more analyses that were used to investigate the outcomes of your experiment(s).

### analysis_1

This analysis has the following description/reasoning:
To compare the formal linguistic competence of models trained on BabyLM vs TinyStories across different model sizes and data scales.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the analysis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This analysis is based on the following experiment(s) (outcomes): experiment_1
Your corrected answer (empty if correct): 

#### Metrics list
The measured metrics in this analysis are: Accuracy (BLiMP)
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Average, Variance / Standard Deviation, Median, Distribution (Boxplots)
Your corrected list (empty if correct):

#### Analysis Test

The analysis test is summarised as: Simple comparison (greater than, less than, visual inspection of learning curves and boxplots)
Your corrected answer (empty if correct):

#### Results

The LLM has found the data of the analysis in the study, which is summarised below. It states either the figures, tables or in text values where it has been found. It describes each with a caption (in case of figure/table), a reason, and subsets of the sets stated before: the metrics used for the analysis, the statistics used, which input data was used, and, which test was applied to reflect upon research questions or confirm/reject hypotheses.

The analysed results were found in the following locations:

- **Tables**:
- **Figures**:
  - **Figure 2**:
    - **caption**:
      - Learning curves (on three repetitions) for BLiMP performance comparing model sizes (17M, 58M and 91M) on two datasets: BabyLM and TinyStories. Dashed lines represent the performance on the full dataset for each model-dataset combination, following the same colouration.
    - **reason**:
      - Shows the average BLiMP accuracy across token anchors to evaluate formal linguistic competence.
    - **metrics**:
      - Accuracy (BLiMP)
    - **statistics**:
      - Average
      - Variance / Standard Deviation
    - **data**:
      - BabyLM-100m (Choshen et al., 2024)
      - TinyStories (Eldan & Li, 2023)
      - BLiMP benchmark (Warstadt et al., 2020)
    - **test**:
      - Simple comparison (greater than, less than, visual inspection of learning curves and boxplots)
  - **Figure 3**:
    - **caption**:
      - Heatmap of average accuracy scores (for three repetitions) across models (17M, 58M, and 91M) and all BLiMP tasks on two datasets: BabyLM and TinyStories, with 160M tokens (this being the largest anchor that occurs in both datasets). Each cell reports the score of a given fine-tuned model on a specific task. The background colour gives a row-wise indication of how the specific model performed, with yellow colours indicating better performance. The boxplot on the right depicts the distributions of performances across the BLiMP tasks.
    - **reason**:
      - Shows task-specific performance and distribution of scores for formal linguistic competence.
    - **metrics**:
      - Accuracy (BLiMP)
    - **statistics**:
      - Average
      - Median
      - Distribution (Boxplots)
    - **data**:
      - BabyLM-100m (Choshen et al., 2024)
      - TinyStories (Eldan & Li, 2023)
      - BLiMP benchmark (Warstadt et al., 2020)
    - **test**:
      - Simple comparison (greater than, less than, visual inspection of learning curves and boxplots)
- **Text**:
  - **Section 4.1**:
    - **value**:
      - Comparing the two datasets indicates that models trained with the BabyLM dataset achieve higher overall BLiMP accuracy across the whole learning curve. Moreover, the models trained on TinyStories show slower improvement and reach a performance plateau at around 64 million sampled tokens for all model sizes.
    - **reason**:
      - Describes the main findings from the BLiMP evaluation.
    - **metrics**:
      - Accuracy (BLiMP)
    - **statistics**:
      - Average
    - **data**:
      - BabyLM-100m (Choshen et al., 2024)
      - TinyStories (Eldan & Li, 2023)
      - BLiMP benchmark (Warstadt et al., 2020)
    - **test**:
      - Simple comparison (greater than, less than, visual inspection of learning curves and boxplots)


#### General

The LLM has overall captured the analysis details...

[X] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)

### analysis_2

This analysis has the following description/reasoning:
To compare the functional linguistic competence of models trained on BabyLM vs TinyStories across different model sizes and data scales.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the analysis?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This analysis is based on the following experiment(s) (outcomes): experiment_2
Your corrected answer (empty if correct): 

#### Metrics list
The measured metrics in this analysis are: Accuracy/F1 (GLUE)
Your corrected list (empty if correct):

#### Statistics
The statistics for the metrics used are: Average, Variance / Standard Deviation, Median, Distribution (Boxplots)
Your corrected list (empty if correct):

#### Analysis Test

The analysis test is summarised as: Simple comparison (greater than, less than, visual inspection of learning curves and boxplots)
Your corrected answer (empty if correct):

#### Results

The LLM has found the data of the analysis in the study, which is summarised below. It states either the figures, tables or in text values where it has been found. It describes each with a caption (in case of figure/table), a reason, and subsets of the sets stated before: the metrics used for the analysis, the statistics used, which input data was used, and, which test was applied to reflect upon research questions or confirm/reject hypotheses.

The analysed results were found in the following locations:

- **Tables**:
- **Figures**:
  - **Figure 4**:
    - **caption**:
      - Learning curves (on three repetitions) for a subset of GLUE tasks comparing model sizes (17m, 58M and 91M) on two datasets: BabyLM and TinyStories. Dashed lines represent the performance on the full dataset for each model-dataset combination, following the same colouration.
    - **reason**:
      - Shows the average GLUE performance across token anchors to evaluate functional linguistic competence.
    - **metrics**:
      - Accuracy/F1 (GLUE)
    - **statistics**:
      - Average
      - Variance / Standard Deviation
    - **data**:
      - BabyLM-100m (Choshen et al., 2024)
      - TinyStories (Eldan & Li, 2023)
      - GLUE benchmark subset (Wang et al., 2019b)
    - **test**:
      - Simple comparison (greater than, less than, visual inspection of learning curves and boxplots)
  - **Figure 5**:
    - **caption**:
      - Heatmap of average accuracy scores (for three repetitions) across models (17M, 58M, and 91M) and GLUE tasks on two datasets: BabyLM and TinyStories, with 160M tokens (this being the largest anchor that occurs in both datasets). Each cell reports the score of a given fine-tuned model on a specific task. The background colour gives a row-wise indication of how the specific model performed, with yellow colours indicating better performance. The boxplot on the right depicts the distributions of performances across the GLUE tasks.
    - **reason**:
      - Shows task-specific performance and distribution of scores for functional linguistic competence.
    - **metrics**:
      - Accuracy/F1 (GLUE)
    - **statistics**:
      - Average
      - Median
      - Distribution (Boxplots)
    - **data**:
      - BabyLM-100m (Choshen et al., 2024)
      - TinyStories (Eldan & Li, 2023)
      - GLUE benchmark subset (Wang et al., 2019b)
    - **test**:
      - Simple comparison (greater than, less than, visual inspection of learning curves and boxplots)
- **Text**:
  - **Section 4.2**:
    - **value**:
      - Similar to the BLiMP evaluation (see Section 4.1), model–variants of all sizes perform better when trained on the BabyLM dataset compared to the TinyStories. The performance gap here is less pronounced but still evident.
    - **reason**:
      - Describes the main findings from the GLUE evaluation.
    - **metrics**:
      - Accuracy/F1 (GLUE)
    - **statistics**:
      - Average
    - **data**:
      - BabyLM-100m (Choshen et al., 2024)
      - TinyStories (Eldan & Li, 2023)
      - GLUE benchmark subset (Wang et al., 2019b)
    - **test**:
      - Simple comparison (greater than, less than, visual inspection of learning curves and boxplots)


#### General

The LLM has overall captured the analysis details...

[X] Very well (No major mistakes and/or missing information)
[] Well (Missing some information and/or minor mistakes)
[] Okay (Missing important information and/or substantial mistakes)
[] Poorly (Missing crucial information and/or severe mistakes)
[] Incorrect (The LLM has missed the point of the experiment and/or has hallucinated)


### General Analysis Questions

The LLM has provided you with one or more analyses from your work. Is this amount of analyses the same as the amount you specified?

Please write the amount of analyses you had for the study: [2]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Interpretation

Experiment outcomes are analysed and interpreted to determine whether the experiment supports the hypothesis or not. 

The LLM has found the following interpretations of the experiment outcomes;

### interpretation_1

This interpretation has the following description/reasoning:
Possibly, the TinyStories dataset lacks rich linguistic features due to its vocabulary that was kept simple by design... In addition, since the dataset is synthetic, there is little variation in the structure of the stories. These factors could likely explain the inability of models trained on TinyStories to reach higher accuracy on BLiMP, with clear stagnation around the 64 million tokens.

The LLM has provided the following notes on its reasoning:
Explains why BabyLM outperforms TinyStories on formal competence and why TinyStories plateaus early, found in Section 4.1.

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
Notably, unlike for the BLiMP results, using the full TinyStories dataset beyond 160M tokens (dashed lines in Figure 4) substantially improves performance. This suggests that the underlying data in TinyStories, despite being limited in vocabulary and complex grammatical structure, does enable the models to effectively capture fundamental linguistic patterns and structures needed for language use and understanding.

The LLM has provided the following notes on its reasoning:
Explains the value of narrative datasets for functional competence despite their simplicity, found in Section 4.2.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

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
We demonstrate that early performance metrics can be used in model selection, allowing us to discard unpromising candidate models.

The LLM has provided the following notes on its reasoning:
Interprets the learning curves as a reliable proxy for final performance, found in Section 1 and supported by the learning curve analyses.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the interpretation?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason:

This interpretation is based on the following analyses: analysis_1, analysis_2
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

## Conclusions

The interpretations are used to draw conclusions, which either reflect upon the previous research questions or hypotheses, or yield new research questions or hypotheses.

The LLM has found the following conclusions on the interpretations;

### conclusion_1

This conclusion has the following description/reasoning:
Our findings indicate that models trained with the BabyLM dataset outperform models trained with the TinyStories dataset on formal linguistic competence... These insights support the usage of BabyLM for pre-training language models in resource-constrained settings, where performance on small dataset samples can reliably predict the final achieved performance (such as mixture of experts (MoE) development).

The LLM has provided the following notes on this conclusion:
Concludes on the superiority of BabyLM for formal competence and its utility for compute-efficient model selection, found in Section 6.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the conclusion?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason: Our findings indicate that models trained with the BabyLM dataset outperform models trained with the TinyStories dataset on formal linguistic competence. These insights support the usage of BabyLM for pre-training language models in resource-constrained settings, where performance on small dataset samples can reliably predict the final achieved performance (such as mixture of experts (MoE) development).

This conclusion is based on the following interpretations: interpretation_1, interpretation_3
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

This conclusion is to support (or not) the following hypotheses: hypothesis_1, hypothesis_2
Your corrected answer (empty if correct):

This conclusion supports the hypothesis: [True, True]
Your corrected answer (empty if correct):

### conclusion_2

This conclusion has the following description/reasoning:
The gap in functional linguistic competence is less pronounced, with models trained on TinyStories achieving comparable performance but showing smaller deviations across model sizes... These empirical findings suggest that TinyStories lacks certain rich linguistic features, likely due to its simpler vocabulary and synthetic origin, yet still supports the idea that narrative structures could contribute to functional linguistic competence.

The LLM has provided the following notes on this conclusion:
Concludes on the specific utility of narrative datasets for functional competence, found in Section 6.

Based on the LLMs answer, would you like to improve the answer to more accurately capture the conclusion?
- If you wish to change nothing, leave blank.
- If you wish to improve the answer, please copy the original answer and adapt it below.
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording.

Corrected reason: The gap in functional linguistic competence is less pronounced, with models trained on TinyStories achieving comparable performance but showing smaller deviations across model sizes. These empirical findings suggest that TinyStories lacks certain rich linguistic features, likely due to its simpler vocabulary and synthetic origin, yet still supports the idea that narrative structures could contribute to functional linguistic competence.

This conclusion is based on the following interpretations: interpretation_2
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

This conclusion is to answer (or reflect) upon the following research questions: research_question_1
Your corrected answer (empty if correct):

This conclusion is to support (or not) the following hypotheses: hypothesis_1
Your corrected answer (empty if correct):

This conclusion supports the hypothesis: [True]
Your corrected answer (empty if correct):


### General Conclusion Questions

The LLM has provided you with one or more conclusions from your work. Is this amount of conclusions the same as the amount you specified?

Please write the amount of conclusions you had for the study: [2]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;


## Future Work

The LLM has also found possible future work directions in terms of research questions or hypotheses yielded from an exploratory angle of your study.

### Suggested Research Questions

#### suggested_research_question_1

The LLM has found the following suggested research question: How does child-directed speech (e.g., TinyDialogues) compare to the datasets analysed here (BabyLM and TinyStories) in terms of linguistic competence and computational efficiency?
Please correct the suggestion if wrong (leave empty if correct):

The LLM has provided the following note/location on the suggestion: Section 5 (Limitations and Future Work)

The LLM has provided the following reason for the suggestion: Section 5 (Limitations and Future Work)

The LLM has linked the suggestion to the following conclusions: conclusion_1, conclusion_2
Please correct the IDs if wrong/missing (leave empty if correct):

Please grade the suggestion below:
[X] The LLM has (nearly) perfectly captured a future research direction suggested by our work.
[] The LLM has stated a future research direction that was implied by our work, but not strongly suggested.
[] The LLM has stated a future research direction from our work that is partially correct.
[] The LLM has stated a future research direction that has some overlap with our work but has introduced incorrect or false information.
[] The LLM has stated a future research direction that was not stated or implied in our work; the LLM has hallucinated this information.

#### suggested_research_question_2

The LLM has found the following suggested research question: How do these findings generalize to a greater variety of model architectures, larger model sizes, tokeniser vocabulary sizes, and other training paradigms (e.g., model distillation and reinforcement learning)?
Please correct the suggestion if wrong (leave empty if correct):

The LLM has provided the following note/location on the suggestion: Section 5 (Limitations and Future Work)

The LLM has provided the following reason for the suggestion: Section 5 (Limitations and Future Work)

The LLM has linked the suggestion to the following conclusions: conclusion_1, conclusion_2
Please correct the IDs if wrong/missing (leave empty if correct):

Please grade the suggestion below:
[X] The LLM has (nearly) perfectly captured a future research direction suggested by our work.
[] The LLM has stated a future research direction that was implied by our work, but not strongly suggested.
[] The LLM has stated a future research direction from our work that is partially correct.
[] The LLM has stated a future research direction that has some overlap with our work but has introduced incorrect or false information.
[] The LLM has stated a future research direction that was not stated or implied in our work; the LLM has hallucinated this information.

#### suggested_research_question_3

The LLM has found the following suggested research question: Can curriculum learning, incorporating progressively complex data sourced from other domains or more complex narrative samples, enrich vocabulary and improve performance?
Please correct the suggestion if wrong (leave empty if correct):

The LLM has provided the following note/location on the suggestion: Section 6 (Conclusions)

The LLM has provided the following reason for the suggestion: Section 6 (Conclusions)

The LLM has linked the suggestion to the following conclusions: conclusion_2
Please correct the IDs if wrong/missing (leave empty if correct):

Please grade the suggestion below:
[X] The LLM has (nearly) perfectly captured a future research direction suggested by our work.
[] The LLM has stated a future research direction that was implied by our work, but not strongly suggested.
[] The LLM has stated a future research direction from our work that is partially correct.
[] The LLM has stated a future research direction that has some overlap with our work but has introduced incorrect or false information.
[] The LLM has stated a future research direction that was not stated or implied in our work; the LLM has hallucinated this information.


#### Suggested Research Questions General

The LLM has provided you with one or more Suggested Research Questions from your work. Is this amount of Suggested Research Questions the same as the amount you specified?

Please write the amount of Suggested Research Questions you had for the study: [5]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;
- Suggested RQ1 has an overarching question to it as well: How do other datasets from other specific subdomains or other scaled sizes compare to the datasets analysed here (BabyLM and TinyStories) in terms of linguistic competence and computational efficiency?
- Paragraph 3 Section 5: "The subset of the GLUE benchmark that we used includes a variety of downstream tasks, but integrating the full benchmark or tasks from more diverse benchmarking suites (e.g., SuperGLUE (Wang et al., 2019a)) could offer a more comprehensive and concrete assessment of functional linguistic competence."

### Suggested Hypotheses

#### suggested_hypothesis_1

The LLM has found the following suggested hypothesis: The authors hypothesise that optimising the hyperparameters to all specific downstream tasks would provide more reliable results for the ultimate performance of the various models.
Please correct the suggestion if wrong (leave empty if correct): 

The LLM has provided the following note/location on the suggestion: Section 5 (Limitations and Future Work)

The LLM has provided the following reason for the suggestion: The authors suggest that hyperparameter optimization, which was skipped due to cost, would yield more reliable ultimate performance results.

The LLM has linked the suggestion to the following conclusions: conclusion_1, conclusion_2
Please correct the IDs if wrong/missing (leave empty if correct):

Please grade the suggestion below:
[X] The LLM has (nearly) perfectly captured a future research direction suggested by our work.
[] The LLM has stated a future research direction that was implied by our work, but not strongly suggested.
[] The LLM has stated a future research direction from our work that is partially correct.
[] The LLM has stated a future research direction that has some overlap with our work but has introduced incorrect or false information.
[] The LLM has stated a future research direction that was not stated or implied in our work; the LLM has hallucinated this information.


#### Suggested Hypotheses General

The LLM has provided you with one or more Suggested Hypotheses from your work. Is this amount of Suggested Hypotheses the same as the amount you specified?

Please write the amount of Suggested Hypotheses you had for the study: [1]

If this amount does not overlap with the LLMs answer, feel free to specify reasons below;
