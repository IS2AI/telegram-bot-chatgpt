from revChatGPT.V1 import Chatbot
from googletrans import Translator
import json

config = json.load(open("config.json"))
chatbot = Chatbot(config=config)

response = ""

# initialize translator
translator = Translator()
translate = False

while True:
    prompt = input("You (kk): ")
    if prompt == 'q':
        break

    prompt = translator.translate(prompt, src='kk', dest='en')
    prompt = prompt.text
    print("You (en):", prompt)

    for data in chatbot.ask(prompt):
        response = data["message"]

    print("ChatGPT (en):", response)
    response = translator.translate(response, src='en', dest='kk')
    print("ChatGPT (kz):", response.text)
