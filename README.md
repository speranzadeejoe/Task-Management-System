# Task Management System

## 📌 Overview
The **Task Management System** is a simple yet effective desktop application built using **Tkinter** for managing daily tasks. It allows users to **add, view, and delete tasks**, making it a useful tool for productivity and organization.

## 🚀 Features
- **Add Task**: Users can add a new task with a title, due date, and description.
- **View Tasks**: Tasks are displayed in a tabular format using a `Treeview`.
- **Delete Task**: Users can delete a selected task from the list.
- **MySQL Database Integration**: Tasks are stored and managed in a MySQL database.

## 🛠 Tech Stack
- **Python**
- **Tkinter (GUI Framework)**
- **MySQL (Database)**

## 📂 Project Structure
```
📦 Task-Management-System
├── 📄 main.py        # Main application file
├── 📄 db.py          # Database functions (add, delete, fetch tasks)
├── 📄 README.md      # Project documentation
└── 📂 assets         # (If applicable) Icons, images, etc.
```

## 🔧 Setup Instructions
### 1️⃣ Prerequisites
- Install **Python (>=3.6)**
- Install MySQL and set up a database

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Task-Management-System.git
cd Task-Management-System
```

### 3️⃣ Install Required Libraries
```bash
pip install mysql-connector-python
```

### 4️⃣ Set Up MySQL Database
1. Create a database in MySQL:
```sql
CREATE DATABASE task_manager;
USE task_manager;
```
2. Create a `tasks` table:
```sql
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    due_date VARCHAR(50) NOT NULL,
    description TEXT NOT NULL
);
```
3. Update `db.py` with your MySQL credentials.

### 5️⃣ Run the Application
```bash
python main.py
```

## 🎯 Future Enhancements
- ✅ Edit Task functionality
- 📅 Task Sorting & Filtering
- 🔔 Task Notifications & Reminders
- 📊 Task Statistics & Progress Tracking

## 📜 License
This project is open-source and available under the **MIT License**.

## 🤝 Contributing
Feel free to fork this repository, submit issues, or make pull requests!

---
Made with ❤️ by Speranza Deejoe 

