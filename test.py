from openai import OpenAI
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    

    messages = build_message()

    chat = get_chatgpt_response(messages)

    # print(chat)
    print(chat.choices[0].message.content)

def build_message():
    question = input("What do you want to ask ChatGPT? ")

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question}
    ]

    return messages

def get_chatgpt_response(msgs):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # Create a chat completion
    chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=msgs)
    return chat

main()

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