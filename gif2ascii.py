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
    frames = []
    _, frame = gif.read()
    while True:
        try:
            ok, frame = gif.read()
            if not ok:
                print("Err: Unable to read GIF frame")
                break
            frame = cv2.resize(frame, (100,50))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frames.append(frame)
            num += 1
        except KeyboardInterrupt:
            break
    gif.release()
    return frames


def frame_to_ascii(frame, n):
    out = []
    img = np.array(frame)
    h, w = img.shape
    for i in range(h):
        row = []
        for j in range(w):
            row.append(text[math.floor((img[i][j]/255)*n -1)])
        out.append(row)
    os.system("clear")
    for i in range(h):
        for j in range(w):
            print(out[i][j], end="")
        print()

def main():
    gif_path = sys.argv[1]
    n = len(text)
    gif = cv2.VideoCapture(gif_path)
    if not gif.isOpened():
        print("Err: Can't open")
    frame_list = convert_gif_to_frames(gif)
    d = len(frame_list)
    idx = 0
    while True:
        frame_to_ascii(frame_list[idx], n)
        idx = (idx+1)%d
        sleep(0.03)

if __name__ == '__main__':
    main()

