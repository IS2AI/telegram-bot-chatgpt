## Installation
Clone the repo and install [requirements.txt](https://github.com/IS2AI/telegram-bot-chatgpt/blob/main/voice_chat_gpt_en/requirements.txt)
```
git clone https://github.com/IS2AI/telegram-bot-chatgpt.git
cd telegram-bot-chatgpt
cd voice_chat_gpt_en
pip install -r requirements.txt
```

## Authentication 
1) Create an account on [OpenAI's ChatGPT](https://chat.openai.com)
2) Update ```config.json``` file with your email and password
3) Other authentication methods can be found [here](https://github.com/acheong08/ChatGPT)

## Create a new Telegram bot with [BotFather](https://telegram.me/botfather)
1) Start a new conversation with the [BotFather](https://telegram.me/botfather)
<img src = "https://github.com/IS2AI/telegram-bot-chatgpt/blob/main/botfather.png?raw=true" width="370" height="600">

2) Send /newbot to create a new Telegram bot.
3) When asked, enter a name for the bot.
4) Give the Telegram bot a unique username. Note that the bot name must end with the word "bot" (case-insensitive).
5) Insert the Telegram bot's access token to ```tele_token = "<YOUR TELEGRAM BOT TOKEN>"``` inside the ```telegram_chatgpt_en.py``` file.

## Run 
1) Launch the Telegram bot
```
python telegram_chatgpt_en.py
```
2) Open the bot on Telegram and a new conversation with ChatGPT via voice messages
<img src = "https://github.com/IS2AI/telegram-bot-chatgpt/blob/main/voice_chat_gpt_en/telegram%20en.png?raw=true" width="370" height="600">

## References
1) [revChatGPT](https://github.com/acheong08/ChatGPT)
2) [SpeechRecognition](https://github.com/Uberi/speech_recognition)
3) [gTTS](https://github.com/pndurette/gTTS/tree/6c6300c346747fb42f8daed70eb240c98e27cb88)
