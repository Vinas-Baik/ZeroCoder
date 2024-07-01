import tkinter as tk
from tkinter import messagebox

def greet():
    name = entry.get()
    if name:
        messagebox.showinfo("Приветствие", f"Привет, {name}!")
    else:
        messagebox.showinfo("Ошибка", "Пожалуйста, введите свое имя")

def center_window(root, width, height):
    # Получаем размеры экрана
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Вычисляем координаты для размещения окна по центру
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Устанавливаем размеры и позицию окна
    root.geometry(f'{width}x{height}+{x}+{y}')

# Создаем главное окно
root = tk.Tk()
root.title("ДЗ по OP07 ZeroCoder")
# размещаем его по центру
center_window(root, 400, 200)

# Создаем и размещаем метку
label = tk.Label(root, text="Введите ваше имя:")
label.pack(pady=10)

# Создаем и размещаем поле ввода
entry = tk.Entry(root)
entry.pack(pady=5)

# Создаем и размещаем кнопку
button = tk.Button(root, text="Поздороваться", command=greet)
button.pack(pady=20)

# Запускаем главный цикл обработки событий
root.mainloop()