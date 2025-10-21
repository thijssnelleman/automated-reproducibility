# Automating Reproducibility

## Method

- Use LLM to reproduce AI studies, the output of which is validated by 'experts'
- LLM extracts and produces, based on PDF and link to GitHub repository, the following:
    1. Extract the hypothesis of the study, and state how this is tested in the study
    2. Show how the code can be setup including installing requirements and downloading the data
    3. Provide commands on how to run the code to produce the output per hypothesis
    4. State how the output should be interpreted according to the method of the study
    

OE:
- The whole process should be automated. We should try to 'keep the human out of the loop'. We need a very powerfull LLM like Chat-GPT 5 Codex, for which we need funding (I do not see any problem running our experiment 'live' on ChatGPT).
- This way we can ask the LLM to re-implement the entire method based on the paper, instead of running the author's code.
- This will be highly complicated and we will run into a lot of errors, which is the whole point: We can record this and analyse for the paper
- We do NOT limit ourselves to papers that have everything public: We try all R types.
- (?) We use Jupyter Notebooks as output produced by the LLM, s.t. the output is not only easily formatted and readable but also allows for smooth combination of text and code.

Thijs:
- The entire process should be based upon the scientific method; We need to cut up the task in a 'million little pieces', and can use this process to explain but also construct the output.