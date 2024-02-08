from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

question = input("What do you want to ask ChatGPT? ")

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": question}
]

# Create a chat completion
chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)

# print(chat)
print(chat.choices[0].message.content)


# messages = [ {"role": "system", "content":  
#               "You are a intelligent assistant."} ] 
# while True: 
#     message = input("User : ") 
#     if message: 
#         messages.append( 
#             {"role": "user", "content": message}, 
#         ) 
#         chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages) 
#     reply = chat.choices[0].message.content 
#     print(f"ChatGPT: {reply}") 
#     messages.append({"role": "assistant", "content": reply}) 