import tkinter as tk
from tkinter import ttk


class MainFrame:
    def __init__(self, title="HTK Assistant AI"):
        self.title = title
        self.root = tk.Tk()  # Create the main window
        self.root.title(self.title)  # Set the title of the main window
        self.root.geometry("800x600")  # Set the size of the main window
        self.root.configure(bg="white")  # Set the background color of the main window

        # Create a label for the text input
        self.input_label = tk.Label(self.root, text="Enter your text:", bg="white", font=("Arial", 12))
        self.input_label.pack(pady=10)

        # Create a text box for user input
        self.text_input = tk.Text(self.root, height=10, width=60, font=("Arial", 12))
        self.text_input.pack(pady=10)

        # Create a label for the model selection
        self.model_label = tk.Label(self.root, text="Select Model:", bg="white", font=("Arial", 12))
        self.model_label.pack(pady=10)

        # Create a dropdown menu for model selection
        self.model_var = tk.StringVar(value="Select a model")
        self.model_dropdown = ttk.Combobox(self.root, textvariable=self.model_var, state="readonly", font=("Arial", 12))
        self.model_dropdown['values'] = ["ChatGPT", "Groq", "Gemini"]  # Add your models here
        self.model_dropdown.pack(pady=10)

        # Create a submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit, bg="blue", fg="white", font=("Arial", 12))
        self.submit_button.pack(pady=20)

    def submit(self):
        # Get the text input and selected model
        user_input = self.text_input.get("1.0", tk.END).strip()
        selected_model = self.model_var.get()

        # Print the input and selected model (replace this with your processing logic)
        print(f"User Input: {user_input}")
        print(f"Selected Model: {selected_model}")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = MainFrame()
    app.run()