import moviepy.editor as mp

def generate_video(text_file, output_file):
    with open(text_file, 'r') as file:
        text = file.read()
    
    clip = mp.TextClip(text, font='Arial', fontsize=30, color='white')
    clip.fps = 30
    clip.duration = len(text) / 30
    clip.write_videofile(output_file, fps=30)

generate_video("../Contents/qtXpF.txt", "output.mp4")
