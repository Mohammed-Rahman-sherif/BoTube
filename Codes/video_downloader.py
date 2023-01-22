from pytube import YouTube
import moviepy.editor
import random
import string
import os

path = '../Media'
link = "https://youtu.be/RpaCXJ8dNMc"

class Media:
    def video():
        name = (''.join(random.choices(string.ascii_letters, k = 5)))
        print(type(name))
        youtubeObject = YouTube(link)

        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            youtubeObject.download(output_path=path, filename=name)
            #youtubeObject.streams.first().download(filename=name)
            #os.rename(youtubeObject.streams.first().default_filename, 'new_filename.ext')
        except:
            print("An error has occurred")
        print("Download is completed successfully")

        video = moviepy.editor.VideoFileClip(f"../Media/{name}.mp4")
        audio = video.audio
        audio.write_audiofile(f"../Audio/{name}.mp3")


Video1 = Media.video()