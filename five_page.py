
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import os
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/daniil/Human_project/assets/frame5")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("440x956")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 956,
    width = 440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_back = PhotoImage(
    file=relative_to_assets("back.png"))
image_back = canvas.create_image(
    219,
    470,
    image=image_image_back
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    219.0,
    705.0,
    image=image_image_1
)


image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    145.0,
    292.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    bg="#FFFFFF"
)
button_1.place(
    x=30.0,
    y=563.0,
    width=181.0,
    height=128.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    218.0,
    503.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=35.0,
    y=484.0,
    width=340.0,
    height=45.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    217.5,
    422.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)

entry_2.insert(0, "Введите название чата: ")
entry_1.insert(0, "Введите название потока: ")

import tkinter as tk

def on_entry_click(event, entry_num):
    """Функция, которая вызывается при нажатии на поле ввода."""
    if entry_num == 2:
        if entry_2.get() == "Введите название чата: ":  # Проверяем, если текст по умолчани
            entry_2.delete(0, END)  # Удаляем текст
            entry_2.config(fg='black')  # Меняем цвет текста на черный
    elif entry_num == 1:
        if entry_1.get() == "Введите название потока: ":
            entry_1.delete(0, END)
            entry_1.config(fg="black") 

def on_focusout(event, entry_num):
    """Функция, которая вызывается, когда поле ввода теряет фокус."""
    if entry_num == 2:
        if entry_2.get() == "":  # Проверяем, если текст по умолчани
            entry_2.insert(0, "Введите название чата: ")  # Удаляем текст
            entry_2.config(fg='grey')  # Меняем цвет текста на черный
    elif entry_num == 1:
        if entry_1.get() == "":
            entry_1.insert(0, "Введите название потока: ")
            entry_1.config(fg="grey") 


entry_2.bind('<FocusIn>', lambda event: on_entry_click(event, 2))  # Привязываем событие нажатия
entry_2.bind('<FocusOut>', lambda event: on_focusout(event, 2))  # Привязываем событие потери фокуса

entry_1.bind('<FocusIn>', lambda event: on_entry_click(event, 1))  # Привязываем событие нажатия
entry_1.bind('<FocusOut>', lambda event: on_focusout(event, 1))  # Привязываем событие потери фокуса


entry_2.place(
    x=35.0,
    y=403.0,
    width=340.0,
    height=45.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    161.0,
    356.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    313.0,
    624.0,
    image=image_image_4
)

def switch_to_page6():
    window.destroy()
    os.system("python3 /home/daniil/Human_project/six_page.py")

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=switch_to_page6,
    relief="flat",
    bg="#FFFFFF"
)
button_2.place(
    x=115.0,
    y=728.0,
    width=209.0,
    height=48.0
)
window.resizable(False, False)
window.mainloop()
