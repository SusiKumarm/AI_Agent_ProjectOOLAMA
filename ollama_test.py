import ollama

response = ollama.chat(
    model='mistral',
    messages=[
        {
            'role': 'user',
            'content': 'Generate detailed positive and negative test cases for login functionality'
        }
    ]
)

print(response['message']['content'])
