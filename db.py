import mysql.connector

# 🔹 Connect to MySQL Database with error handling
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost", 
            user="root",   # Change if you have a different username
            password="mini",  # Use your actual MySQL password
            database="task_manager",  # Ensure the database exists
            port=3306  # Ensure correct MySQL port
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None  # Return None if connection fails

# 🔹 Function to Ensure Table Exists
def ensure_table():
    conn = connect_db()
    if conn is None:
        print("Database connection failed.")
        return
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            due_date DATE,
            description TEXT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

# 🔹 Function to Add Task
def add_task(title, due_date, description):
    conn = connect_db()
    if conn is None:
        print("Failed to connect to database.")
        return
    cursor = conn.cursor()
    query = "INSERT INTO tasks (title, due_date, description) VALUES (%s, %s, %s)"
    try:
        cursor.execute(query, (title, due_date, description))
        conn.commit()
        print("Task added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    cursor.close()
    conn.close()

# 🔹 Function to Retrieve All Tasks
def get_tasks():
    conn = connect_db()
    if conn is None:
        print("Failed to connect to database.")
        return []
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, title, due_date, description FROM tasks")
        tasks = cursor.fetchall()
        return tasks
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        cursor.close()
        conn.close()

# 🔹 Function to Delete Task
def delete_task(task_id):
    conn = connect_db()
    if conn is None:
        print("Failed to connect to database.")
        return
    cursor = conn.cursor()
    query = "DELETE FROM tasks WHERE id = %s"
    try:
        cursor.execute(query, (task_id,))
        conn.commit()
        print(f"Task with ID {task_id} deleted successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    cursor.close()
    conn.close()

# 🔹 Run Table Check at Startup
ensure_table()
