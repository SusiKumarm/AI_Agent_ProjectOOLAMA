import ollama

user_input = input("Enter your prompt: ")

response = ollama.chat(
    model='mistral',
    messages=[
        {'role': 'user', 'content': user_input}
    ]
)

print("\nResponse:\n")
print(response['message']['content'])
