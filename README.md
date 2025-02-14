import tkinter as tk
from tkinter import ttk
from db import add_task, get_tasks, delete_task  # Import database functions

# Function to Add Task
def add_task_action():
    title = task_entry.get()
    due_date = due_entry.get()
    description = desc_text.get("1.0", tk.END).strip()

    if title and due_date and description:
        add_task(title, due_date, description)  # Add to MySQL
        update_task_list()  # Refresh task list
        task_entry.delete(0, tk.END)
        due_entry.delete(0, tk.END)
        desc_text.delete("1.0", tk.END)

# Function to Update Task List from DB
def update_task_list():
    for row in task_list.get_children():
        task_list.delete(row)

    tasks = get_tasks()  # Fetch tasks from DB
    for task in tasks:
        task_list.insert("", "end", values=task)

# Function to Delete Selected Task
def delete_task_action():
    selected_item = task_list.selection()
    if selected_item:
        task_id = task_list.item(selected_item[0])["values"][0]  # Get correct task_id
        delete_task(task_id)  # Delete from MySQL
        update_task_list()  # Refresh UI

# 🔹 GUI Code Starts
root = tk.Tk()
root.title("TASK MANAGEMENT SYSTEM")
root.geometry("800x500")

# 🔹 Frame 1: Title Frame
frame1 = tk.Frame(root, bg="black", padx=10, pady=10)
frame1.pack(fill="x")

# 🔹 Frame 2: Input Frame
frame2 = tk.Frame(root, bg="black", padx=10, pady=10)
frame2.pack(fill="x")

# 🔹 Frame 3: Task List Frame
frame3 = tk.Frame(root, bg="black", padx=10, pady=10)
frame3.pack(fill="both", expand=True)

# 🔹 Frame 4: Action Buttons Frame
frame4 = tk.Frame(root, bg="black", padx=10, pady=10)
frame4.pack(fill="x")

# 🔹 Title Label
mainlabel = tk.Label(frame1, text="TASK MANAGEMENT SYSTEM", font=("Arial", 16, "bold"), fg="white", bg="black")
mainlabel.pack()

# 🔹 Task Title
task_label = tk.Label(frame2, text="TASK TITLE", font=("Arial", 12, "bold"), fg="white", bg="black")
task_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
task_entry = tk.Entry(frame2, width=40, font=("Arial", 12))
task_entry.grid(row=0, column=1, sticky="w", padx=5, pady=5, ipady=3)

# 🔹 Due Date
due_label = tk.Label(frame2, text="DUE DATE", font=("Arial", 12, "bold"), fg="white", bg="black")
due_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
due_entry = tk.Entry(frame2, width=40, font=("Arial", 12))
due_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5, ipady=3)

# 🔹 Description
desc_label = tk.Label(frame2, text="DESCRIPTION", font=("Arial", 12, "bold"), fg="white", bg="black")
desc_label.grid(row=2, column=0, sticky="nw", padx=5, pady=5)

desc_frame = tk.Frame(frame2)
desc_frame.grid(row=2, column=1, sticky="w", padx=5, pady=5)

desc_text = tk.Text(desc_frame, width=40, height=4, font=("Arial", 12))
desc_text.pack()

# 🔹 Add Task Button
add_task_btn = tk.Button(frame2, text="➕ Add Task", bg="white", fg="black", font=("Arial", 10, "bold"), command=add_task_action)
add_task_btn.grid(row=3, column=1, pady=10, sticky="w")

# 🔹 Task List Display
task_list = ttk.Treeview(frame3, columns=("ID", "Title", "Due Date", "Description"), show="headings")

# Define column headings
task_list.heading("ID", text="ID")
task_list.heading("Title", text="Task Title")
task_list.heading("Due Date", text="Due Date")
task_list.heading("Description", text="Description")

# Set column widths
task_list.column("ID", width=30)
task_list.column("Title", width=150)
task_list.column("Due Date", width=100)
task_list.column("Description", width=250)

# Place the Treeview
task_list.pack(fill="both", expand=True)

# 🔹 Delete Button
delete_task_btn = tk.Button(frame4, text="🗑 Delete Task", bg="red", fg="white", font=("Arial", 10, "bold"), command=delete_task_action)
delete_task_btn.pack(pady=10)

# Load tasks at start
update_task_list()

# Start the Tkinter event loop
root.mainloop()# Task-Management-System
