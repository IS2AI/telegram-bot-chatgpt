## Installation
Clone the repo and install [requirements.txt](https://github.com/IS2AI/telegram-bot-chatgpt/blob/main/voice_chat_gpt_kk/requirements.txt)
```
git clone https://github.com/IS2AI/telegram-bot-chatgpt.git
cd telegram-bot-chatgpt
cd voice_chat_gpt_kk
pip install -r requirements.txt
```
## Authentication 
1) Create an account on [OpenAI's ChatGPT](https://chat.openai.com)
2) Update ```config.json``` file with your email and password
3) Other authentication methods can be found [here](https://github.com/acheong08/ChatGPT)

## Create a new Telegram bot with [BotFather](https://telegram.me/botfather)
1) Start a new conversation with the [BotFather](https://telegram.me/botfather)
<img src = "https://github.com/IS2AI/telegram-bot-chatgpt/blob/main/botfather.png?raw=true" width="370" height="600">

2) Send ```/newbot``` to create a new Telegram bot.
3) When asked, enter a name for the bot.
4) Give the Telegram bot a unique username. Note that the bot name must end with the word "bot" (case-insensitive).
5) Send ```/token``` to generate authorization token
6) Insert the generated token on ```tele_token = "<YOUR TELEGRAM BOT TOKEN>"``` in ```telegram_chatgpt_kk.py``` file.

## Run
1) Download ```Kaz_TTS``` text-to-speech model from [Google Drive](https://drive.google.com/file/d/1jdoY7nxGeoscWgceWMYGQKqDAboHpGU3/view?usp=share_link)
2) Unzip the file and move ```exp``` folder inside the ```voice_chat_gpt_kz``` folder
3) Launch the Telegram bot
```
python telegram_chatgpt_kk.py
```
4) Open the bot on Telegram and start a new conversation with ChatGPT via voice messages
<img src = "https://github.com/IS2AI/telegram-bot-chatgpt/blob/main/voice_chat_gpt_kz/telegram%20kk.png?raw=true" width="370" height="600">

## Official ChatGPT API
1. Log/Sign in to [OpenAI platform](https://platform.openai.com/)
2. Go to the profile section (top right) and click on ```View API keys```
3. If you don't have an existing key then create a new one
4. Install the OpanAI package: ```pip install --upgrade openai```
5. Export your key on your working enviroment: ```export OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>```
6. Launch the telegram bot: ```python telegram_chatgpt_en_v2.py```
7. For more information about the official ChatGPT API: https://platform.openai.com/docs/guides/chat 

## TODO
1) Exception handling
2) Include voice feedback for the exceptions

## References
1) [revChatGPT](https://github.com/acheong08/ChatGPT)
2) [SpeechRecognition](https://github.com/Uberi/speech_recognition)
3) [Kaz_TTS](https://github.com/IS2AI/Kazakh_TTS)
4) [Google Translate](https://github.com/ssut/py-googletrans)
