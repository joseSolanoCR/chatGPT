

import openai
from transformers import pipeline

OPENAI_API_KEY = ""
org_id = ""


openai.organization = org_id
openai.api_key = OPENAI_API_KEY



generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B', tokenizer='EleutherAI/gpt-neo-2.7B')

def generate_response(prompt):
    response = generator(prompt, max_length=1024, do_sample=True, temperature=0.7)

    message = response[0]['generated_text'].strip()
    return message

print(generate_response("Hola, ¿cómo estás?"))
