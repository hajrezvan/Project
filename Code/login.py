import customtkinter as ctk
import tkinter.messagebox as tkmb
import sqlite3
import tkinter as tk
import os
import subprocess

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       username TEXT UNIQUE,
                       password TEXT,
                       role INTEGER)''')
    
    conn.commit()
    conn.close()

def clear_fields():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def login():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", 
                  (entered_username, entered_password))
    
    user = cursor.fetchone()
    
    conn.close()

    if user:
        # Login successful
        success_window(user[0], user[3])
    else:
        # Incorrect credentials
        error_message = "Incorrect username or password."
        tkmb.showerror("Error", error_message)

def success_window(user_id, user_role):
    new_window = ctk.CTkToplevel(app)
    new_window.title(f"Login Successful - User {user_id}")
    new_window.geometry("350x200")

    label = ctk.CTkLabel(new_window, text=f"Welcome, User {user_id}!")
    label.pack(pady=20)

    role_label = ctk.CTkLabel(new_window, text="Your Role:")
    role_label.pack(pady=5)

    role_value = ["Student", "Teacher", "Scientist"][user_role - 1]
    role_display = ctk.CTkLabel(new_window, text=f"{role_value}")
    role_display.pack(pady=5)

    close_button = ctk.CTkButton(new_window, text="Close", command=lambda: [new_window.destroy(), open_text_editor()])
    close_button.pack(pady=10)

def open_text_editor():
    os.system(f"python {os.path.join(os.getcwd(), 'TextEditor.py')}")

def register():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if not entered_username or not entered_password:
        error_message = "Please enter both username, password, and select a role."
        tkmb.showerror("Error", error_message)
        return

    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", 
                  (entered_username, entered_password, 1))
    
    conn.commit()
    conn.close()

    success_message = f"User '{entered_username}' registered successfully!"
    tkmb.showinfo("Success", success_message)
    clear_fields()


# Initialize the database
init_db()

# Create the main application window
app = ctk.CTk()
app.geometry("400x350")
app.title("Login / Register Page")

# Create a frame for the login/register elements
frame = ctk.CTkFrame(master=app, corner_radius=15)
frame.pack(pady=50, padx=40, fill="both", expand=True)

# Create labels and entry fields
username_label = ctk.CTkLabel(master=frame, text="Username:")
username_label.pack(pady=10)

username_entry = ctk.CTkEntry(master=frame, placeholder_text="Enter username")
username_entry.pack(pady=10)

password_label = ctk.CTkLabel(master=frame, text="Password:")
password_label.pack(pady=10)

password_entry = ctk.CTkEntry(master=frame, placeholder_text="Enter password", show="*")
password_entry.pack(pady=10)

# Create buttons for login and register
login_button = ctk.CTkButton(master=frame, text="Login", command=lambda: login())
login_button.pack(side=tk.LEFT, pady=10, padx=5)

register_button = ctk.CTkButton(master=frame, text="Register", command=register)
register_button.pack(side=tk.RIGHT, pady=10, padx=5)

app.mainloop()
