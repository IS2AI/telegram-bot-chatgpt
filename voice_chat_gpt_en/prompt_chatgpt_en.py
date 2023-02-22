from revChatGPT.V1 import Chatbot
import json

config = json.load(open("config.json"))
chatbot = Chatbot(config=config)

response = ""

while True:
    prompt = input("You: ")
    if prompt == 'q':
        break

    for data in chatbot.ask(prompt):
        response = data["message"]

    print("ChatGPT:", response)