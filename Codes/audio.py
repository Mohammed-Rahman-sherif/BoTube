import moviepy.editor

video = moviepy.editor.VideoFileClip("../Media/video.mp4")
audio = video.audio
audio.write_audiofile("../Audio/sample.mp3")