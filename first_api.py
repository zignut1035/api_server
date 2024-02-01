import os
import openai

openai.api_key = os.getenv("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")

response = openai.Completion.create(
    engine = "gpt-3.5-turbo",
    prompt = "what is life",
    temperature = 0.4,
    max_token = 50
)

print(response)