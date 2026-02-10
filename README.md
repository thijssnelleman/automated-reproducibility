# Automating Reproducibility

This repository accompanies our paper "Automated Reproducibility Has a Problem Statement Problem". We have the following directory structure;

```bash
- llm_output -> The raw LLM output files of the dataset
- papers -> The PDF files provided to the LLM
- plots -> The plots used in our paper
- review_template -> The templates used to create review forms for the authors
- reviews -> The reviews of the author for the LLM output
```

Furthermore:
- `analysis.ipynb` contains the code to generate our tables and figures.
- `study_extractor.py` is the main entry point of our code to generate LLM output
- `study_prompt.yaml` contains the prompt accompanying the paper for the LLM
- `output_compiler.py` creates the `output.csv` dataset from the reviews
- `review_compiler.py` creates a review from an LLM output JSON and the templates
- `tokencalc.py` was used to determine how many tokens each LLM API call uses
- `requirements.txt` contains the required packages and their versions to run the code.

## Extracting a Hypothesis

1. Place your Google Gemini API key in a .env in this directory.
2. Build your Python venv and install the requirements from `requirements.txt`
3. Run `python hypothesis_extractor.py path/to/your/paper.pdf` and wait for the API call to be done.
4. Find the JSON in `llm_output/your_paper_name.json`

## Create a review form

Run `python review_compiler.py path/to/the/output.json` and find the result in `reviews/your_paper_name.md`

## How to Cite

@article{snelleman2026automatedreproducibility,
  title={Automated Reproducibility Has a Problem Statement Problem},
  author={Snelleman, Thijs and Lundestad Lawrence, Peter and Hoos, Holger H and Gundersen, Odd Erik},
  booktitle={Reproducible AI Workshop at the Fortieth AAAI Conference on Artificial Intelligence},
  year={2026}
}
