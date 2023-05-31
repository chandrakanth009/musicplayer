import pygame
from tkinter import *
from tkinter import filedialog
import os
from pygame import mixer
from PIL import ImageTk, Image

root = Tk()
root.title("Music Player")
root.geometry("300x300")


def browse_file():
    file_path = filedialog.askopenfilename()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
def set_volume(volume):
    pygame.mixer.music.set_volume(float(volume)/100)
def set_pos(pos):
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.set_pos(float(pos))

def update_seekbar():
    current_time = pygame.mixer.music.get_pos() / 1000
    seek_bar.set(current_time)
    seek_bar.after(1000, update_seekbar)
def next_music():
    # code to play the next music file
    pass

browse_button = Button(root, text="Browse", command=browse_file)
browse_button.pack()

pause_button = Button(root, text="Pause", command=pygame.mixer.music.pause)
pause_button.pack()

unpause_button = Button(root, text="Unpause", command=pygame.mixer.music.unpause)
unpause_button.pack()

stop_button = Button(root, text="Stop", command=pygame.mixer.music.stop)
stop_button.pack()
next_button = Button(root, text="Next", command=next_music)
next_button.pack()
volume_label = Label(root, text="Volume")
volume_label.pack(pady=10)
volume_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
volume_slider.pack()

seek_bar = Scale(root, from_=0, to=300, orient=HORIZONTAL, command=set_pos)
seek_bar.pack(pady=10)

pygame.init()

update_seekbar()


root.mainloop()
