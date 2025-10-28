# Automatic Extraction of Hypothesis

You will be presented with the output of an LLM which was tasked to extract the hypothesis from your paper.

The answer is structured into two parts; First the LLM aims to extract the hypothesis from your paper and **formulate it** through paraphrasing or quoting.

Second, the LLM will aim to describe how this hypothesis was tested; Indentify the metrics used, the input data for your method, possible statistical tests or comparisons to test your hypothesis, and under what strategy these values were acquired.

Please answer the following questions:

## Hypothesis

The LLM states a hypothesis in its answer. Please grade the answer from the following options:

The LLM ...

[] captures the hypothesis (nearly) perfectly.

[] has stated an incomplete hypothesis; The answer is correct but is missing key information.

[] has stated the general hypothesis but has introduced false or incorrect information.

[] has stated a hypothesis similar to ours, but is far too innaccurate to consider correct.

[] has stated an hypothesis that has (nearly) no overlap with our work.

[] Other: If it is an hallucination, please explain below.

Based on the LLMs answer, can you improve the answer to more accurately capture the hypothesis?
- If you wish to change nothing, simply state the answer of the LLM
- If you wish to improve the answer, please adapt the original answer
- If you consider the answer completely wrong, feel free to rephrase completely in your own wording

## Hypothesis testing

The LLM has provided a table stating how your hypothesis was tested.

For each cell in the table, please mark if you find the answer correct or in correct.

In case there are missing rows in the table, please state in below which information is missing. Feel free to either:
- Create your own table with missing information
- Write lines of text, where each line represents one missing row in the table
