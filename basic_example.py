import requests
import json

key = "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"
prompt = "How are you?"
max_tokens = 10
temperature = 1

headers = {
  "Authorization": "Bearer " + key,
  "Content-Type": "application/json"
}
data = {
  "messages": [
    {
      "role": "user",
      "content": prompt
    }
  ],
  "max_tokens": max_tokens,
  "temperature": temperature,
  "model": "gpt-3.5-turbo"
}

r = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps(data))
r_json = r.json()
print(r_json["choices"][0]["message"]["content"])