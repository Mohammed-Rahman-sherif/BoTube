import cv2
import numpy as np
import moviepy.editor as mp

# Read text file
with open("../Contents/wKXfq.txt", "r") as file:
    text = file.readlines()

# Load audio file
audio = mp.AudioFileClip("../Audio/Original/fBFeM.wav")

# Get audio duration in seconds
audio_duration = audio.duration

# Define number of frames per second
fps = 25

# Calculate total number of frames
total_frames = int(audio_duration * fps)

# Define video clip
def create_frame(t):
    img = np.zeros((500, 1000, 3), dtype=np.uint8)
    img.fill(0)
    add_text(img, text, -int(t * fps))
    return img

# Create black image
img = np.zeros((500, 1000, 3), dtype=np.uint8)
img.fill(0)

# Add text to image
def add_text(img, text, pos):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.0
    font_color = (255, 255, 255)
    thickness = 2
    text_height = 50
    x = (img.shape[1] - img.shape[1]) // 2
    y = (img.shape[0] + text_height) // 2
    for line in text:
        text_size = cv2.getTextSize(line, font, font_scale, thickness)
        text_width = text_size[0][0]
        cv2.putText(img, line, (x, y + pos), font, font_scale, font_color, thickness, cv2.LINE_AA)
        y = y + text_height

# Define video frame size and create video writer
frame_size = (1000, 500)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
video_writer = cv2.VideoWriter("star_wars_opening.avi", fourcc, 50, frame_size)

# Generate video frames
for i in range(total_frames):
    img.fill(0)
    add_text(img, text, -i)
    video_writer.write(img)
    cv2.imshow("Star Wars Opening", img)
    cv2.waitKey(20)

# Release video writer
video_writer.release()

# Destroy all windows
cv2.destroyAllWindows()
