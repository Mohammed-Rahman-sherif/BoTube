import cv2
import numpy as np

# Read text from file
with open("../Contents/qtXpF.txt", "r") as file:
    text = file.read()

# Create black image
img = np.zeros((500, 1000, 3), dtype=np.uint8)
img.fill(0)

# Add text to image
def add_text(img, text, pos):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.0
    font_color = (255, 255, 255)
    thickness = 2
    text_size = cv2.getTextSize(text, font, font_scale, thickness)
    text_width = text_size[0][0]
    text_height = text_size[0][1]
    x = (img.shape[1] - text_width) // 2
    y = (img.shape[0] + text_height) // 2
    cv2.putText(img, text, (x, y + pos), font, font_scale, font_color, thickness, cv2.LINE_AA)

# Define video frame size and create video writer
frame_size = (1000, 500)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
video_writer = cv2.VideoWriter("star_wars_opening.avi", fourcc, 25, frame_size)

# Generate video frames
for i in range(100):
    img.fill(0)
    add_text(img, text, -i)
    video_writer.write(img)
    cv2.imshow("Star Wars Opening", img)
    cv2.waitKey(20)

# Release video writer
video_writer.release()

# Destroy all windows
cv2.destroyAllWindows()
