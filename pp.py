import tkinter as tk
from tkinter import messagebox
import cv2
import numpy as np
import pygame
import os
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def set_volume_to_max():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(1.0, None)  

def play_video():

    pygame.mixer.init()
    pygame.mixer.music.load(r"C:\Users\Admin\Downloads\jtk\jeff-the-killer-screaming.mp3")
    

    set_volume_to_max()

    pygame.mixer.music.play(-1)


    cap = cv2.VideoCapture(r"C:\Users\Admin\Downloads\jtk\video.mp4")
    

    cv2.namedWindow('Video', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Video', frame)
        

        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break

    cap.release()
    cv2.destroyAllWindows()
    pygame.mixer.music.stop()

def on_yes():
    root.destroy()
    play_video()

def on_no():
    messagebox.showinfo("Ответ", "ебланне?")


root = tk.Tk()
root.title("Вопрос")


label = tk.Label(root, text="ты меня любишь?")
label.pack(pady=20)


button_yes = tk.Button(root, text="ба", command=on_yes)
button_yes.pack(side=tk.LEFT, padx=20)

button_no = tk.Button(root, text="нет", command=on_no)
button_no.pack(side=tk.RIGHT, padx=20)


root.mainloop()
