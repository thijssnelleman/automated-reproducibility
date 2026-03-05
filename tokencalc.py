import base64
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

load_dotenv()

client = genai.Client()
model = "gemini-3-preview"  # Alternative: "gemini-2.5-pro", 

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

for paper_path in papers:
    pdf_encoded = encode_pdf(paper_path)
    prompt = Path("study_prompt.yaml").open().read()
    response = client.models.count_tokens(
        model=model,
        contents=[
            types.Part.from_bytes(
                data=pdf_encoded,
                mime_type="application/pdf",
            ),
        ],
    )
    print(f"{paper_path.stem}: {response.total_tokens}")
