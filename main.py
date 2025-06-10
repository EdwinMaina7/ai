from openai import OpenAI
from config import OPENROUTER_API_KEY, SITE_URL, SITE_TITLE

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=OPENROUTER_API_KEY,
)

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": SITE_URL,
    "X-Title": SITE_TITLE,
  },
  extra_body={},
  model="deepseek/deepseek-r1-0528:free",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
print(completion.choices[0].message.content)