import os
import base64
from pathlib import Path
from dotenv import load_dotenv
from mistralai import Mistral
# from mistralai.models import UserMessage

load_dotenv()
api_key = os.environ["MISTRAL_API_KEY"]
#model = "mistral-small-latest"
model = "mistral-medium-2508"  # Latest premium model

# Load PDF

def encode_pdf(file_path: Path):
    with file_path.open("rb") as pdf_file:
        pdf_bytes = pdf_file.read()
    return base64.b64encode(pdf_bytes).decode("utf-8")

papers = Path("papers").glob("*.pdf")

# Override for testing
papers = [Path("papers/Edge-Based Graph Component Pooling.pdf"),
          Path("papers/The Unreasonable Effectiveness of Open Science in AI A Replication Study.pdf")]

for paper_path in papers:
    pdf_encoded = encode_pdf(paper_path)

    client = Mistral(api_key=api_key)

    prompt = Path("hypothesis_prompt.yaml").open().read()

    messages = [
        {
            "role": "user",
            "content": prompt,
        },
        {
            "role": "user",
            "type": "file",
            "content": pdf_encoded,
        }
        # {
        #     "type": "file",
        #     "content": pdf_encoded,
        #     "filename": "your_file.pdf",
        #     "mime_type": paper_path.name,
        # },
    ]

    # NOTE: Doesn't work due to model context length; "Prompt contains 627325 tokens and 0 draft tokens, too large for model with 131072 maximum context length"
    chat_response = client.chat.complete(
        model=model,
        temperature=0.0,  # For determinism
        messages=messages,
        #max_tokens=
    )
    output_path = Path("llm_output") / paper_path.stem + ".json"
    with output_path.open("w+") as f:
        f.write(chat_response.json())
    print(chat_response.choices[0].message.content)
    