# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI


client = OpenAI(api_key="sk-128375233cd24f6db5dc60b814d42ff8", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)