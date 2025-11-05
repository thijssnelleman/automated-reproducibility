# import os
import base64
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

load_dotenv()
#api_key = os.environ["MISTRAL_API_KEY"]

client = genai.Client()
model = "gemini-2.5-pro"  # Alternative: "gemini-2.5-flash", 

# Load PDF

def encode_pdf(file_path: Path):
    with file_path.open("rb") as pdf_file:
        pdf_bytes = pdf_file.read()
    return base64.b64encode(pdf_bytes).decode("utf-8")

papers = Path("papers").glob("*.pdf")

# Override for testing

if len(sys.argv) == 2 and Path(sys.argv[1]).exists():
    papers = [Path(sys.argv[1])]
else:
    papers = [#Path("papers/Weighted Initialisation of Evolutionary Instrument and Pitch Detection in Polyphonic Music.pdf"),
            #Path("papers/Edge-Based Graph Component Pooling.pdf"),
            Path("papers/The Unreasonable Effectiveness of Open Science in AI A Replication Study.pdf"),
            ]

for paper_path in papers:
    pdf_encoded = encode_pdf(paper_path)
    output_path = Path("llm_output") / f"{paper_path.stem}.json"
    #if output_path.exists():  # Continue, do not replace responses anymore
    #    continue
    prompt = Path("hypothesis_prompt.yaml").open().read()
    response = response = client.models.generate_content(
        model=model,
        contents=[
            types.Part.from_bytes(
                data=pdf_encoded,
                mime_type="application/pdf",
            ),
            prompt
        ],
        config={
            "temperature": 0.0,  # 0.0 = deterministic
        }
    )
    with output_path.open("w+") as f:
        response_data = response.text
        if response_data[:7] == "```json":  # Trim leading ```json
            response_data = response_data[7:]
        if response_data[-3:] == "```":  # Trim trailing ```
            response_data = response_data[:-3]
        print("Writing to: ", output_path)
        f.write(response_data)
