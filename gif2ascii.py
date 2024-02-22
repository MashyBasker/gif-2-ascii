import cv2
import numpy as np
import math
import os
from time import sleep
import sys


#text = "#$@&MH%?;:=^~-"[::-1]
text = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
def convert_gif_to_frames(gif):
    num = 0
    gray_frames = []
    color_frames = []
    _, frame = gif.read()
    while True:
        try:
            ok, frame = gif.read()
            if not ok:
                print("Err: Unable to read GIF frame")
                break
            frame = cv2.resize(frame, (100,50))
            gframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            color_frame = frame
            gray_frames.append(gframe)
            color_frames.append(color_frame)
            num += 1
        except KeyboardInterrupt:
            break
    gif.release()
    return gray_frames, color_frames

def rgb_display(char, r, g, b):
    color = f"\033[38;2;{r};{g};{b}m"
    reset = "\033[0m"
    print(f"{color}{char}{reset}",end="")


def frame_to_ascii(gframe, cframe, n):
    out = []
    img = np.array(gframe)
    h, w = img.shape
    for i in range(h):
        row = []
        for j in range(w):
            row.append(text[math.floor((img[i][j]/255)*n -1)])
        out.append(row)
    os.system("clear")
    for i in range(h):
        for j in range(w):
            b, g, r = cframe[i][j]
            rgb_display(out[i][j], r, g, b)
        print()

def main():
    gif_path = sys.argv[1]
    n = len(text)
    gif = cv2.VideoCapture(gif_path)
    if not gif.isOpened():
        print("Err: Can't open")
    gray, color = convert_gif_to_frames(gif)
    d = len(gray)
    idx = 0
    while True:
        frame_to_ascii(gray[idx], color[idx], n)
        idx = (idx+1)%d
        sleep(0.05)

if __name__ == '__main__':
    main()

