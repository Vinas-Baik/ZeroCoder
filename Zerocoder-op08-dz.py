import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

tasks = {}

def add_task():
    description = simpledialog.askstring("", "Новая задача:")
    if description:
        task_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tasks[task_time] = description
        update_task_listbox()

def edit_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_time = list(tasks.keys())[selected_index]
        new_description = simpledialog.askstring("Редактирование задачи",
                                                 "Напишите новое описание задачи:",
                                                 initialvalue=tasks[task_time])
        if new_description:
            tasks[task_time] = new_description
            update_task_listbox()
    except IndexError:
        messagebox.showwarning("Редактирование задачи", "Выберите задачу для редактирования.")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_time = list(tasks.keys())[selected_index]
        del tasks[task_time]
        update_task_listbox()
    except IndexError:
        messagebox.showwarning("Удалить задачу", "Выберите задачу для удаления.")

def clear_tasks():
    if messagebox.askyesno("Очистить список задач ", "Вы уверены что хотите очистить список задач?"):
        tasks.clear()
        update_task_listbox()

def update_task_listbox():
    task_listbox.delete(0, tk.END)
    for task_time, description in tasks.items():
        task_listbox.insert(tk.END, f"{task_time}: {description}")

def center_window(root, width=400, height=400):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

if __name__ == "__main__":
    root = tk.Tk()
    root.title("ДЗ по OP08 ZeroCoder")
    center_window(root)

    task_listbox = tk.Listbox(root, width=60, height=20)
    task_listbox.pack(pady=10)

    add_button = tk.Button(root, text="Добавить\nзадачу", command=add_task, bg="lightgreen")
    add_button.pack(side=tk.LEFT, padx=10)

    edit_button = tk.Button(root, text="Редактировать\nзадачу", command=edit_task, bg="lightcoral")
    edit_button.pack(side=tk.LEFT, padx=10)

    delete_button = tk.Button(root, text="Удалить\nзадачу", command=delete_task, bg="lightblue")
    delete_button.pack(side=tk.LEFT, padx=10)

    clear_button = tk.Button(root, text="Очистить все\nзадачи", command=clear_tasks, bg="lightyellow")
    clear_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()