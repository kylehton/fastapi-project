#basic api call function for later implementation

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are going to help us with resume suggestions"},
        {
            "role": "user",
            "content": "Show me how I can improve this section of my resume"
        }
    ]
)

print(completion.choices[0].message.content)