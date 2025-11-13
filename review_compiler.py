"""Compiles the LLM output into a review file."""
from pathlib import Path
import json
import sys

general_template = Path("review_template/review_general.md").open().read()
hypothesis_template = Path("review_template/review_hypothesis.md").open().read()
experiment_template = Path("review_template/review_experiment.md").open().read()
interpretation_template = Path("review_template/review_interpretation.md").open().read()

input_path = Path(sys.argv[1])

if not input_path.exists() or input_path.suffix != ".json":
    print("File does not exist or is not a JSON file.")
    sys.exit(1)

with input_path.open() as json_file:
    llm_output = json.load(json_file)

output = Path(f"reviews/{input_path.stem}.md").open("w")

hypothesis_sections, experiment_sections, interpretation_sections = [], [], []

paper_title = llm_output["Meta"]["title"]
authors = ", ".join(llm_output["Meta"]["authors"])

general_template = general_template.replace("@@@PAPER_TITLE@@@", paper_title)
general_template = general_template.replace("@@@AUTHORS@@@", authors)

for key in llm_output["Hypothesis"]:
    hypo_o = hypothesis_template.replace("@@@HYPOTHESIS_ID@@@", key)
    type = "explicit" if llm_output["Hypothesis"][key]["explicit"] else "implied"
    hypo_o = hypo_o.replace("@@@HYPOTHESIS_TYPE@@@", type)
    hypo_o = hypo_o.replace("@@@HYPOTHESIS_VALUE@@@", llm_output["Hypothesis"][key]["hypothesis"])
    hypo_o = hypo_o.replace("@@@HYPOTHESIS_REASON@@@", llm_output["Hypothesis"][key]["reason"])
    hypothesis_sections.append(hypo_o)

for key in llm_output["Experiment"]:
    exp_o = experiment_template.replace("@@@EXPERIMENT_ID@@@", key)
    exp_o = exp_o.replace("@@@EXPERIMENT_DESCRIPTION@@@", llm_output["Experiment"][key]["experiment_description"])
    exp_o = exp_o.replace("@@@EXPERIMENT_HYPOTHESIS@@@", ", ".join(llm_output["Experiment"][key]["hypothesis"]))
    exp_o = exp_o.replace("@@@EXPERIMENT_METRICS@@@", ", ".join(llm_output["Experiment"][key]["metrics"]))
    statistics = llm_output["Experiment"][key]["statistics"]
    statistics = ", ".join(statistics) if isinstance(statistics, list) else statistics
    exp_o = exp_o.replace("@@@EXPERIMENT_STATISTICS@@@", statistics)
    exp_o = exp_o.replace("@@@EXPERIMENT_STRATEGY@@@", llm_output["Experiment"][key]["strategy"])
    test = llm_output["Experiment"][key]["test"]
    test = ", ".join(test) if isinstance(test, list) else test
    exp_o = exp_o.replace("@@@EXPERIMENT_TEST@@@", test)

    # We concatenate the raw JSON instead, due to the volatility of this output.
    exp_o = exp_o.replace("@@@EXPERIMENT_RESULTS_TABLE@@@", json.dumps(llm_output["Experiment"][key]["results"], indent=4, ensure_ascii=False))
    experiment_sections.append(exp_o)

for key in llm_output["Interpretation"]:
    int_o = interpretation_template.replace("@@@INTERPRETATION_ID@@@", key)
    int_o = int_o.replace("@@@REASON@@@", llm_output["Interpretation"][key]["reason"])
    experiment_ids = llm_output["Interpretation"][key]["experiment"]
    experiment_ids = ", ".join(llm_output["Interpretation"][key]["experiment"]) if isinstance(experiment_ids, list) else experiment_ids
    int_o = int_o.replace("@@@EXPERIMENT_ID@@@", experiment_ids)
    int_o = int_o.replace("@@@HYPOTHESIS_ID@@@", llm_output["Interpretation"][key]["hypothesis"])
    int_o = int_o.replace("@@@SUPPORT@@@", str(llm_output["Interpretation"][key]["support"]))
    interpretation_sections.append(int_o)


general_template = general_template.replace("@@@HYPOTHESIS_SECTIONS@@@", "\n".join(hypothesis_sections))
general_template = general_template.replace("@@@EXPERIMENT_SECTIONS@@@", "\n".join(experiment_sections))
general_template = general_template.replace("@@@INTERPRETATION_SECTIONS@@@", "\n".join(interpretation_sections))    

output.write(general_template)
output.close()
