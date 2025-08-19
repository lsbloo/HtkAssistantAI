import tkinter as tk

class LabelFrame:
    def __init__(self, parent, text="Label Frame", **kwargs):
        self.frame = tk.LabelFrame(parent, text=text, **kwargs)
        self.frame.pack(padx=10, pady=10, fill="both", expand=True)

    def add_widget(self, widget):
        widget.pack(padx=5, pady=5)  # Add padding around the widget
        widget.configure(bg=self.frame.cget("bg"))  # Match the background color of the frame 