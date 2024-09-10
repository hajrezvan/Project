import customtkinter as ctk
from tkinter import simpledialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

class ChartDrawerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("3D Equation Grapher")
        self.root.geometry("800x600")

        # Set theme
        ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

        # Frame for the canvas
        self.canvas_frame = ctk.CTkFrame(self.root)
        self.canvas_frame.pack(fill=ctk.BOTH, expand=True)

        # Matplotlib Figure and Axis
        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.canvas_frame)
        self.canvas.get_tk_widget().pack(fill=ctk.BOTH, expand=True)

        # Input button
        self.input_button = ctk.CTkButton(self.root, text="Input Formula", command=self.input_formula)
        self.input_button.pack(side=ctk.LEFT, padx=10, pady=10)

        # Clear button
        self.clear_button = ctk.CTkButton(self.root, text="Clear Graph", command=self.clear_graph)
        self.clear_button.pack(side=ctk.LEFT, padx=10, pady=10)

        # Exit button
        self.exit_button = ctk.CTkButton(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack(side=ctk.RIGHT, padx=10, pady=10)

    def input_formula(self):
        """Prompts the user to input a formula with x, y, and z variables."""
        formula = simpledialog.askstring("Input", "Enter a formula (e.g., z = x**2 + y**2 - 16):")
        if formula:
            try:
                self.plot_formula(formula)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid formula: {e}")

    def plot_formula(self, formula):
        """Plots the 3D graph of the given formula."""
        self.clear_graph()

        # Generate x, y, and calculate z based on the formula
        x = np.linspace(-10, 10, 100)
        y = np.linspace(-10, 10, 100)
        X, Y = np.meshgrid(x, y)

        try:
            Z = eval(formula.replace("z", "X * 0"), {"np": np, "x": X, "y": Y})
        except Exception as e:
            messagebox.showerror("Error", f"Error evaluating formula: {e}")
            return

        # Create a surface plot
        self.ax.plot_surface(X, Y, Z, cmap="viridis")

        self.ax.set_xlabel('X axis')
        self.ax.set_ylabel('Y axis')
        self.ax.set_zlabel('Z axis')
        self.ax.grid(True)
        self.canvas.draw()

    def clear_graph(self):
        """Clear the current graph."""
        self.ax.clear()
        self.ax.set_xlabel('X axis')
        self.ax.set_ylabel('Y axis')
        self.ax.set_zlabel('Z axis')
        self.canvas.draw()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = ctk.CTk()
    app = ChartDrawerApp(root)
    app.run()
