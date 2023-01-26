import os
import random
import string

from moviepy.editor import VideoFileClip
from pytube import YouTube
import speech_recognition as sr

class YouTubeTranscribe:
    def __init__(self, link: str, path: str = "../Media", audio_path: str = "../Audio"):
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

    def download_video(self):
        try:
            self.video_stream.download(output_path=self.path, filename=self.video_file)
        except Exception as e:
            print(f"An error occurred while downloading the video: {e}")

    def extract_audio(self):
        try:
            video = VideoFileClip(os.path.join(self.path, self.video_file))
            audio = video.audio
            audio.write_audiofile(os.path.join(self.audio_path, self.audio_file))
        except Exception as e:
            print(f"An error occurred while extracting the audio: {e}")

    def transcribe_audio(self):
        try:
            r = sr.Recognizer()
            with sr.AudioFile(os.path.join(self.audio_path, self.audio_file)) as source:
                audio = r.record(source)
            text = r.recognize_google(audio, show_all=True)
            print(text["alternative"][0]["transcript"])
            with open(os.path.join("../Contents",f"{self.name}.txt"), "w") as file:
                file.write(text["alternative"][0]["transcript"])
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred while transcribing the audio: {e}")
        return ""

youtube_transcribe = YouTubeTranscribe("https://youtu.be/7COmHMJztgI")