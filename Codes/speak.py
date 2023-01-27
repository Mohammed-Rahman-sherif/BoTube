import os
from gtts import gTTS

text = "வணக்கம், உங்கள் தமிழ் பாட்டுக்கு அனுப்பப்பட்டுள்ளது."

tts = gTTS(text, lang='ta')
tts.save("hello.mp3")

from playsound import playsound
#playsound("hello.mp3")

audio_path = '../Audio/Translated'
name = 'xhsbs'
des = 'ta'
print(os.path.join(audio_path, des, name + '.mp3'))
