from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

def main():
    messages = build_message()
    chat = get_chatgpt_response(messages)

    print(chat.choices[0].message.content)

def build_message():
    question = input("What do you want to ask JD LLM? ")
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question}
    ]

    return messages

def get_chatgpt_response(msgs):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # client = OpenAI(api_ke 
    chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=msgs)
    return chat

main()