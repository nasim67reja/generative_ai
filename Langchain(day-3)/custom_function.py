import json
from openai import OpenAI

client = OpenAI()

student_custom_function = [
    {
        'name': 'extract_student_info',
        'description': 'Get the student information from the body of the input text',
        'parameters': {
            'type': 'object',
            'properties': {
                'name': {
                    'type': 'string',
                    'description': 'Name of the person'
                },
                'college': {
                    'type': 'string',
                    'description': 'The college name.'
                },
                'grades': {
                    'type': 'integer',
                    'description': 'CGPA of the student.'
                },
                'club': {
                    'type': 'string',
                    'description': 'college club for extracurricular activities. '
                }

            }
        }
    }
]
student_description = "sunny savita is a student of computer science at IIT delhi. He is an indian and has a 8.5 GPA. Sunny is known for his programming skills and is an active member of the college's AI Club. He hopes to pursue a career in artificial intelligence after graduating."

student_description_two = "krish naik is a student of computer science at IIT Mumbai. He is an indian and has a 9.5 GPA. krish is known for his programming skills and is an active member of the college's data science Club. He hopes to pursue a career in artificial intelligence after graduating."

student_description_three = "sudhanshu kumar is a student of computer science at IIT bengalore. He is an indian and has a 9.2 GPA. krish is known for his programming skills and is an active member of the college's MLops Club. He hopes to pursue a career in artificial intelligence after graduating."

student_info = [student_description,
                student_description_two, student_description_three]

for student in student_info:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{'role': "user", 'content': student}],
        functions=student_custom_function,
        function_call="auto"
    )
    print(response.choices[0].message.function_call.arguments)
    print(json.loads(response.choices[0].message.function_call.arguments))


# response = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[{'role': "user", 'content': prompt}],
#     functions=student_custom_function,
#     function_call="auto"
# )

# print(response.choices[0].message.function_call.arguments)
# print(json.loads(response.choices[0].message.function_call.arguments))
