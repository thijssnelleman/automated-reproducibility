import os
import base64
from pathlib import Path
from dotenv import load_dotenv
from mistralai import Mistral
# from mistralai.models import UserMessage

load_dotenv()
api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-small-latest"
#model = "mistral-medium-2508"  # Latest premium model

# Load PDF

def encode_pdf(file_path: Path):
    with file_path.open("rb") as pdf_file:
        pdf_bytes = pdf_file.read()
    return base64.b64encode(pdf_bytes).decode("utf-8")

paper_path = Path("papers/Edge-Based Graph Component Pooling.pdf")
pdf_encoded = encode_pdf(paper_path)

client = Mistral(api_key=api_key)

messages = [
    {
        "role": "user",
        "content": "Can you summarise what this paper is about?",
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

chat_response = client.chat.complete(
    model=model,
    temperature=0.0,  # For determinism
    messages=messages,
    max_tokens=
)
print(chat_response.choices[0].message.content)