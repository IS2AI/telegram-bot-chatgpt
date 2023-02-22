import soundfile
import num2words
import os
import re

def convert2wav(audio_file):
    # save the audio file with appropriate parameters
    data, samplerate = soundfile.read(audio_file)
    soundfile.write(audio_file, data, samplerate, subtype='PCM_16')

def make_dir(dir_name):
    # Create a path if it does not exist
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print("[INFO] Directory ", dir_name,  " created")
    else:
        print("[INFO] Directory ", dir_name,  " already exists")

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"(\d+)", lambda x: num2words.num2words(int(x.group(0)), lang='kz'), text)
    return text