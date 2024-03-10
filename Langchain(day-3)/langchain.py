from openai import OpenAI
client = OpenAI()


info = "Hellow guys! I am Nasim a dropout student from Hajee Mohammad Danesh Science And Technology University.My Subject was Fisheries but my insterest was the IT field that's why i have decided to leave my university."

prompt = f"""
Extract the following information as a JSON object from the given text:
- Name
- University
- Subject
- Reason for dropping out

Text to analyze:
"{info}"
"""

response = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        {
          "role": "user",
          "content": prompt
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response.choices[0].message.content)
