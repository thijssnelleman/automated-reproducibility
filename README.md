# Automating Reproducibility

## Extracting a Hypothesis

1. Place your Google Gemini API key in a .env in this directory.
2. Build your Python venv and install the requirements from `requirements.txt`
3. Run `python hypothesis_extractor.py path/to/your/paper.pdf` and wait for the API call to be done.
4. Find the JSON in `llm_output/your_paper_name.json`

## Create a review form

Run `python review_compiler.py path/to/the/output.json` and find the result in `reviews/your_paper_name.md`
