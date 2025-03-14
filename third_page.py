from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, END
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/daniil/Human_project/assets/frame3")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("440x956")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=956,
    width=440,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    50.0,
    439.0,
    956.0,
    fill="#FFFFFF",
    outline=""
)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
canvas.create_image(219.0, 561.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
canvas.create_image(209.0, 101.0, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
canvas.create_image(219.0, 761.0, image=image_image_3)

def switch_to_page4():
    window.destroy()
    os.system("python3 /home/daniil/Human_project/fourth_page.py")

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=switch_to_page4,
    relief="flat",
    bg="#FFFFFF"
)
button_1.place(x=16.6695556640625, y=178.0, width=113.3304443359375, height=37.0)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
canvas.create_image(194.0, 539.0, image=entry_image_1)

entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="grey",
    highlightthickness=0
)
entry_1.place(x=30.0, y=520.0, width=325.0, height=37.0)
entry_1.insert(0, "Введите сообщение")

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))

def show_message():
    """Отображение дополнительного изображения на canvas."""
    canvas.create_image(363.0, 361.0, image=image_image_5)
    canvas.update()

def show_entry_data():
    """Функция, вызываемая при нажатии на кнопку отправки."""
    user_input = entry_1.get()
    print(user_input)
    entry_1.delete(0, END)  # Полностью очищаем поле ввода
    entry_1.config(fg="grey")  # Меняем цвет текста
    entry_1.insert(0, "Введите сообщение")  # Вставляем обратно плейсхолдер

def on_entry_click(event):
    """Удаление плейсхолдера при фокусировке."""
    if entry_1.get() == "Введите сообщение":
        entry_1.delete(0, END)
        entry_1.config(fg="black")

def on_focusout(event):
    """Возвращение плейсхолдера, если поле ввода пустое."""
    if entry_1.get() == "":
        entry_1.insert(0, "Введите сообщение")
        entry_1.config(fg="grey")

entry_1.bind("<FocusIn>", on_entry_click)
entry_1.bind("<FocusOut>", on_focusout)

def call_all():
    show_entry_data()
    show_message()

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=call_all,  # Передаем исправленную функцию
    relief="flat",
    bg="#FFFFFF"
)
button_2.place(x=384.0, y=518.0, width=42.0, height=42.0)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
canvas.create_image(176.0, 277.0, image=image_image_4)

window.resizable(False, False)
window.mainloop()
