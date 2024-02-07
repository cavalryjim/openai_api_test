from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the best shtf rifle?"}
]

# Create a chat completion
chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)

print(chat)


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