import base64
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
import time

load_dotenv()

client = genai.Client()
model = "gemini-3.1-pro-preview"  # Alternative: "gemini-2.5-pro", 

def encode_pdf(file_path: Path):
    """PDF Loader."""
    with file_path.open("rb") as pdf_file:
        pdf_bytes = pdf_file.read()
    return base64.b64encode(pdf_bytes).decode("utf-8")

if len(sys.argv) == 2:
    assert Path(sys.argv[1]).exists()
    assert Path(sys.argv[1]).suffix == ".pdf"
    papers = [Path(sys.argv[1])]
else:
    papers = Path("papers").glob("*.pdf")

prompt = Path("study_prompt.yaml").open().read()
for paper_path in papers:
    pdf_encoded = encode_pdf(paper_path)
    output_path = Path("llm_output") / f"{paper_path.stem}.json"
    if output_path.exists():  # Continue, do not replace responses anymore
        print(f"Output already exists for paper {paper_path}. Do you wish to replace it? (y/n): ", end="")
        if input().lower() != "y":
            continue
    response = client.models.generate_content(
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
    time.sleep(5)  # Avoid API overload
