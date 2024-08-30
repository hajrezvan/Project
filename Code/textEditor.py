import customtkinter as ctk
from tkinter import messagebox, simpledialog, Listbox, END
import os

# Ensure the files directory exists
os.makedirs("files", exist_ok=True)

# Initialize the application
app = ctk.CTk()
app.title("Text Editor Application")
app.geometry("900x600")

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")  # Modes: "system" (default), "light", "dark"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

# Function to create a new item and save the text editor content to a file
def create_new_item():
    # Prompt the user for a file name
    file_name = simpledialog.askstring("Input", "Enter the file name to save:")
    if file_name:
        # Save the content of the text editor to the file in the "files" directory
        file_path = os.path.join("files", file_name)
        content = text_editor.get("1.0", ctk.END).strip()
        with open(file_path, "w") as file:
            file.write(content)
        
        # Add the file name to the listbox
        listbox_left.insert(END, file_name)
        # Clear the text editor after saving
        text_editor.delete("1.0", ctk.END)

# Function to delete selected item and delete the file from the system
def delete_item():
    selected_item = listbox_left.curselection()
    if selected_item:
        file_name = listbox_left.get(selected_item)
        file_path = os.path.join("files", file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
        listbox_left.delete(selected_item)
    else:
        messagebox.showwarning("Warning", "No item selected to delete.")

# Function to draw selected item (for demo purposes, it just shows a message)
def draw_item():
    selected_item = listbox_left.curselection()
    if selected_item:
        item_text = listbox_left.get(selected_item)
        messagebox.showinfo("Draw Item", f"Drawn: {item_text}")
    else:
        messagebox.showwarning("Warning", "No item selected to draw.")

# Function to open the content of the selected file in the text editor
def open_file(event):
    selected_item = listbox_left.curselection()
    if selected_item:
        file_name = listbox_left.get(selected_item)
        file_path = os.path.join("files", file_name)
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                content = file.read()
            text_editor.delete("1.0", ctk.END)
            text_editor.insert(ctk.INSERT, content)

# Function to insert predefined text into text editor
def insert_predefined_text(event):
    selected_item = listbox_right.curselection()
    if selected_item:
        item_text = listbox_right.get(selected_item)
        text_editor.insert(ctk.INSERT, item_text)

# Left Frame
frame_left = ctk.CTkFrame(app, width=200, corner_radius=10)
frame_left.pack(side=ctk.LEFT, fill=ctk.Y, padx=10, pady=10)

listbox_left = Listbox(frame_left, relief="flat")
listbox_left.pack(pady=10, padx=10, fill=ctk.BOTH, expand=True)
listbox_left.bind('<Double-1>', open_file)

button_new = ctk.CTkButton(frame_left, text="New", command=create_new_item)
button_new.pack(pady=5, padx=10, fill=ctk.X)

button_delete = ctk.CTkButton(frame_left, text="Delete", command=delete_item)
button_delete.pack(pady=5, padx=10, fill=ctk.X)

button_draw = ctk.CTkButton(frame_left, text="Draw", command=draw_item)
button_draw.pack(pady=5, padx=10, fill=ctk.X)

# Center Frame
frame_center = ctk.CTkFrame(app, corner_radius=10)
frame_center.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=10, pady=10)

text_editor = ctk.CTkTextbox(frame_center, wrap=ctk.WORD)
text_editor.pack(pady=10, padx=10, fill=ctk.BOTH, expand=True)

# Right Frame
frame_right = ctk.CTkFrame(app, width=200, corner_radius=10)
frame_right.pack(side=ctk.LEFT, fill=ctk.Y, padx=10, pady=10)

listbox_right = Listbox(frame_right, relief="flat")
listbox_right.pack(pady=10, padx=10, fill=ctk.BOTH, expand=True)
listbox_right.bind('<Double-1>', insert_predefined_text)

# Predefined Texts
predefined_texts = ["Hello, World!", "CustomTkinter is great!", "Python is awesome!"]
for text in predefined_texts:
    listbox_right.insert(END, text)

# Run the application
app.mainloop()
