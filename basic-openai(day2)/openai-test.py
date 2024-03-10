import pandas as pd
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the OPENAI_API_KEY environment variable
api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise Exception("OPENAI_API_KEY not found in environment variables.")

client = openai.OpenAI(api_key=api_key)

# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#         {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#     ]
# )

# print(completion.choices[0].message)

response = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        {
          "role": "system",
          "content": "Being rude if user ask anything not related to medical science and do not give answer on that topic"
        },
        {
            "role": "user",
            "content": "How to make money.?"
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response.choices[0].message)


# 👉👉👉👉👉 Just Pandas things

# openai.api_key = api_key
# all_models = openai.models.list()

# pd_value = pd.DataFrame(list(all_models), columns=[
#                         "id", "created", "object", "owned_by"])

# print(pd_value)
