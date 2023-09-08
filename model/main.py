from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelWithLMHead
from huggingface_hub import login
import torch
from utils import encode_context, decode_context
import config
import json

login(token=config.HF_TOKEN)

checkpoint = config.CHECKPOINT
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelWithLMHead.from_pretrained(checkpoint)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

params = {
    'top_k': 30,
    'top_p': 0.95,
    'num_beams': 3,
    'num_return_sequences': 1,
    'do_sample': True,
    'no_repeat_ngram_size': 2,
    'temperature': 1.2,
    'repetition_penalty': 1.2,
    'length_penalty': 1.0,
    'eos_token_id': 50257,
    'max_new_tokens': 40,
}

app = FastAPI()


@app.post("/generate")
def generate(context: list[str]):
    inputs = tokenizer(encode_context(context), return_tensors='pt').to(device)

    generated_token_ids = model.generate(
        **inputs,
        **params
    )

    context_with_response = [tokenizer.decode(sample_token_ids) for sample_token_ids in generated_token_ids]
    response = decode_context(context_with_response)[-1]

    return response
