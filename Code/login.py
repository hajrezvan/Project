import customtkinter as ctk
import tkinter.messagebox as tkmb

# Set the appearance mode and color theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Create the main application window
app = ctk.CTk()
app.geometry("400x400")
app.title("Login Page")

# Create a frame for the login elements
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

# Create a login button
login_button = ctk.CTkButton(master=frame, text="Login", command=lambda: login())
login_button.pack(pady=10)

def login():
    # Replace these with actual database credentials
    valid_username = "admin"
    valid_password = "password123"

    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if entered_username == valid_username and entered_password == valid_password:
        # Login successful
        success_window()
    else:
        # Incorrect credentials
        error_message = "Incorrect username or password."
        tkmb.showerror("Error", error_message)

def success_window():
    new_window = ctk.CTkToplevel(app)
    new_window.title("Login Successful")
    new_window.geometry("250x150")

    label = ctk.CTkLabel(new_window, text="Welcome!")
    label.pack(pady=20)

    close_button = ctk.CTkButton(new_window, text="Close", command=new_window.destroy)
    close_button.pack(pady=10)

app.mainloop()
