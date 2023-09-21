import tkinter as tk
from tkinter import messagebox, Toplevel

def create_task_window(title, on_confirm):
    task_window = Toplevel(root)
    task_window.title(title)
    task_window.geometry("300x150")

    entry = tk.Text(task_window, width=80, height=4)
    entry.pack(pady=20, padx=20)

    def confirm_action():
        task_text = entry.get("1.0", "end-1c")
        if task_text:
            on_confirm(task_text)
            task_window.destroy()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    confirm_button = tk.Button(task_window, text=f"Confirm {title}", command=confirm_action, bg="lightblue", width=12, height=2)
    confirm_button.pack(pady=10)

def add_task(task):
    tasks.append(task)
    listbox.insert(tk.END, task)

def update_selected_task(updated_task):
    try:
        selected_task_index = listbox.curselection()[0]
        tasks[selected_task_index] = updated_task
        listbox.delete(selected_task_index)
        listbox.insert(selected_task_index, updated_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

def delete_selected_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
        tasks.pop(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def track_lists():
    track_window = Toplevel(root)
    track_window.title("Saved To-Do Lists")
    track_window.geometry("300x150")

    listbox_saved_lists = tk.Listbox(track_window)
    for task_list in tasks:
        listbox_saved_lists.insert(tk.END, task_list)

    listbox_saved_lists.pack(padx=30, pady=30, fill=tk.BOTH, expand=True)

def create_button(text, command, bg, width=12, height=2):
    button = tk.Button(button_frame, text=text, command=command, bg=bg, width=width, height=height)
    button.pack(side=tk.LEFT, padx=5)
    return button

def add_task_window():
    create_task_window("Add Task", add_task)

def update_task_window():
    create_task_window("Update Task", update_selected_task)

# main application window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x150")  # window size
root.configure(bg="lightgray")  # background color

# store tasks
tasks = []

# listbox to display tasks
listbox = tk.Listbox(root)
listbox.pack(pady=30, padx=30, fill=tk.BOTH, expand=True)

# frame to hold buttons
button_frame = tk.Frame(root)
button_frame.pack(padx=4, pady=4)

# buttons for adding, updating, tracking, and deleting tasks
add_button = create_button("Add Task", add_task_window, "lightblue")
update_button = create_button("Update Task", update_task_window, "lightgreen")
delete_button = create_button("Delete Task", delete_selected_task, "lightcoral")
track_button = create_button("Track Lists", track_lists, "lightyellow")

# Tkinter main loop
root.mainloop()
