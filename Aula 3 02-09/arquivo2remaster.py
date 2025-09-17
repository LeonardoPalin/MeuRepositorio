import os
from dotenv import load_dotenv
load_dotenv ()

from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Sou lindo?",
        }
    ],
    model="openai/gpt-oss-20b",
    stream=False,
)

print(chat_completion.choices[0].message.content)