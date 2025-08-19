import tkinter as tk


class MainFrame:
    def __init__(self, title="HTK Assistant AI"): 
        self.title = title
        self.root = tk.Tk() # Create the main window
        self.root.title(self.title)  # Set the title of the main window
        self.root.geometry("800x600")  # Set the size of the main window
        self.root.configure(bg="white")  # Set the background color of the main window
    
    def run(self):
        self.root.mainloop()
    