import tkinter as tk
import pygame
from PIL import Image, ImageTk

"""Play music function"""
def play_music(song):
    pygame.mixer.init()
    pygame.mixer.music.load("view\music\\" + song + ".mp3")
    pygame.mixer.music.play(-1)  # -1 means endless play

root = tk.Tk()
root.title("RPG game")
root.geometry("800x600")

play_music("title")

bg_image = tk.PhotoImage(file="view\wallpapers\\title.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
= image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
# image = Image.open("view\wallpapers\\title.jpeg")
# image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
# photo = ImageTk.PhotoImage(image)

# # Создание метки с изображением и установка на весь экран
# label = tk.Label(root, image=photo)
# label.pack(fill=tk.BOTH, expand=True)

# Add a button widget
button = tk.Button(root, text = "Start the game")#, command=on_button_click)
button.pack()

# Add a label widget
label = tk.Label(root, text = "Start your adventure")
label.pack()

root.mainloop()