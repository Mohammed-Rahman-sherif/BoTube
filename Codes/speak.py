import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
print(len(voices))
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    
engine.setProperty('voice', voices[2].id)

#engine.setProperty('voice', 'com.apple.speech.synthesis.voice.daniel')

engine.say("Hello, how are you today?")

engine.runAndWait()
