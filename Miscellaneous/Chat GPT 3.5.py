# It's not free anymore. We need to pay some amount of money to execute the program.

import openai

openai.api_key = 'YOUR API KEY ADDRESS'

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]
     

while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})