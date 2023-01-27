import os
import random
import string
from gtts import gTTS
from pytube import YouTube
import speech_recognition as sr
from playsound import playsound
from googletrans import Translator
from moviepy.video.io.VideoFileClip import VideoFileClip

class YouTubeTranscribe:
    def __init__(self, link: str, path: str = "../Media", audio_path: str = "../Audio/Original"):
        self.youtube = YouTube(link)
        self.video_stream = self.youtube.streams.get_highest_resolution()

        self.name = ''.join(random.choices(string.ascii_letters, k=5))
        self.video_file = f"{self.name}.mp4"
        self.audio_file = f"{self.name}.wav"
        self.path = path
        self.audio_path = audio_path
        self.download_video()
        self.extract_audio()
        self.transcribe_audio()

        self.option = input("Enter 'ta' for Tamil, 'te' for Telugu, 'zh-cn' for Chinese: ")
        self.translate_file(f'../Contents/{self.name}.txt', self.option)
        self.speak_text(self.translation.text)

    def download_video(self):
        try:
            self.video_stream.download(output_path=self.path, filename=self.video_file)
        except Exception as e:
            print(f"An error occurred while downloading the video: {e}")

    def extract_audio(self):
        try:
            video = VideoFileClip(os.path.join(self.path, self.video_file))
            audio = video.audio
            self.duration = video.duration
            print('Duration: ', self.duration)
            audio.write_audiofile(os.path.join(self.audio_path, self.audio_file))
        except Exception as e:
            print(f"An error occurred while extracting the audio: {e}")

    def transcribe_audio(self):
        try:
            r = sr.Recognizer()
            counter = 0
            failed_counter = 0
            with sr.AudioFile(os.path.join(self.audio_path, self.audio_file)) as source:
                r.adjust_for_ambient_noise(source)
                audio = r.record(source)
                duration = len(audio.get_wav_data()) / audio.sample_rate / audio.sample_width
                chunk_duration = 60  # duration of each chunk in seconds
                offset = 0  # starting point of the first chunk
                transcribed_text = ""
                while offset < duration:
                    with sr.AudioFile(os.path.join(self.audio_path, self.audio_file)) as source:
                        audio_chunk = r.record(source, offset=offset, duration=chunk_duration)
                        if offset < duration:
                            try:
                                text = r.recognize_google(audio_chunk)
                                transcribed_text += text + "\n"
                                counter += 1
                            except sr.UnknownValueError:
                                print("Could not understand audio, skipping chunk...")
                                failed_counter += 1
                        else:
                            pass
                        offset += chunk_duration
                with open(os.path.join("../Contents", f"{self.name}.txt"), "w") as file:
                    file.write(transcribed_text)
                print(transcribed_text)
                print("Total chunks processed:", counter)
                print("Total chunks failed:", failed_counter)

        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

        return ""

    def translate_file(self, file_path, dest_language):
        # Initialize the translator
        translator = Translator()
        try:
            # Open the file for reading
            with open(file_path, 'r') as file:
                # Read the contents of the file
                file_contents = file.read()

            # Translate the text
            self.translation = translator.translate(file_contents, dest=dest_language)

            # Open the file for writing
            with open(f'../Contents/{dest_language}/{self.name}.txt', 'w', encoding='utf-8') as file:
                # Write the translation to the file
                file.write(self.translation.text)

        except Exception as e:
            print(f'An error occurred while translating the file: {e}')

    def speak_text(self, text: str, path: str = "../Audio/Translated"):
        try:
            tts = gTTS(self.translation.text, lang=self.option)
            tts.save(os.path.join(path, self.option, self.name + '.mp3'))
            #print(os.path.join(path, self.name + '.mp3'))
            #playsound(os.path.join(path, self.name + '.mp3'))
        
        except Exception as e:
            print(f'An error occured while generating translated audio: {e}')

youtube_transcribe = YouTubeTranscribe("https://youtu.be/7COmHMJztgI")
