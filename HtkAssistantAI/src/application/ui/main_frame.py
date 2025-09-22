import tkinter as tk
from tkinter import ttk
from core.extensions.enviroments import getModelsAvailableInEnvironment
from core.extensions.enviroments import getImageProfileInEnvironment
from PIL import Image, ImageTk, ImageDraw


class MainFrame:
    def create_root(self):
        self.root.title(self.title)  # Set the title of the main window
        self.root.geometry("800x600")  # Set the size of the main window
        self.root.configure(bg='#1E1E1E')  # Set the background color of the main window
        self.root.resizable(False, False)  # Make the window non-resizable
        
        
    def create_circular_widget(self):
        # Create a canvas for the circular widget
        
        self.header_frame = tk.Frame(self.root, bg='#252526', height=100)
        self.header_frame.pack(fill='x')

        self.circle_canvas = tk.Canvas(self.root, width=100, height=100, bg='#252526', highlightthickness=0)
        self.circle_canvas.place(x=680, y=1)  # Position the widget in the top-right corner

        # Draw a circle
        self.circle_canvas.create_oval(5, 5, 95, 95, outline='', fill='#252526')  # Circle background

        # Load and resize the image
        try:
            image_path = Image.open(getImageProfileInEnvironment())  #  # Replace with your image path
            self.profile_image = image_path
            self.profile_image = self.profile_image.resize((90, 90))

            # Create a circular mask
            mask = Image.new('L', (90, 90), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, 90, 90), fill=255)

            # Apply the mask to the image
              # Apply the mask to the image
            self.profile_image = self.profile_image.convert('RGBA')  # Ensure the image has an alpha channel
            circular_image = Image.new('RGBA', (90, 90))
            circular_image.paste(self.profile_image, (0, 0), mask=mask)
            self.profile_image = circular_image
           
            self.profile_photo = ImageTk.PhotoImage(self.profile_image)

            # Place the circular image inside the circle
            self.circle_canvas.create_image(50, 50, image=self.profile_photo, anchor='center')
        except FileNotFoundError:
            print('Profile image not found. Please check the path.')
            
        
        # Add a title label
        self.title_label = tk.Label(self.header_frame, text='HTK Assistant AI', bg='#252526', fg='white', font=('Arial', 18, 'bold'))
        self.title_label.place(x=20, y=30)

    
    def create_input_area(self):
        # Create a label for the text input
        self.input_label = tk.Label(self.root, text="Enter your text:", bg="white", font=("Arial", 12))
        self.input_label.place(x=20, y=160)

        # Create a text box for user input
        self.text_input = tk.Text(self.root, height=10, width=60, font=("Arial", 12))
        self.text_input.place(x=20, y=180)

    def create_model_selection(self):
        # Create a label for the model selection
        self.model_label = tk.Label(self.root, text="Select Model:", bg="white", font=("Arial", 12))
        self.model_label.place(x=10, y=40)

        # Create a dropdown menu for model selection
        self.model_var = tk.StringVar(value="Select a model")
        self.model_dropdown = ttk.Combobox(self.root, textvariable=self.model_var, state="readonly", font=("Arial", 12))
        self.model_dropdown['values'] = self.setupModelsBasedInEnvironment()
        self.model_dropdown.place(x=10, y=120)
      
    def create_button(self): 
        # Create a submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit, bg="blue", fg="white", font=("Arial", 12))
        self.submit_button.place(x=400, y=500)
       
    def setupModelsBasedInEnvironment(self):
        avialiableModelsByEnv = getModelsAvailableInEnvironment()
        avialiableModels = []
        
        if len(avialiableModelsByEnv) == 0:
            avialiableModels.append('No models available')
            return avialiableModels
        
        for i in range(len(avialiableModelsByEnv)):
            if(avialiableModelsByEnv[i] == 'HTK_ASSISTANT_API_KEY_LLM_GROQ'):
                avialiableModels.append('Groq')
            elif(avialiableModelsByEnv[i] == 'HTK_ASSISTANT_API_KEY_LLM_CHATGPT'):
                avialiableModels.append('ChatGPT')
            elif(avialiableModelsByEnv[i] == 'HTK_ASSISTANT_API_KEY_LLM_GEMINI'):
                avialiableModels.append('Gemini')
        return avialiableModels
        
        
    def __init__(self, title="HTK Assistant AI"):
        self.title = title
        self.root = tk.Tk()  # Create the main window
        self.create_root()
        self.create_circular_widget()
        self.create_model_selection()
        self.create_input_area()
        self.create_button()

    def submit(self):
        # Get the text input and selected model
        user_input = self.text_input.get("1.0", tk.END).strip()
        selected_model = self.model_var.get()

        # Print the input and selected model (replace this with your processing logic)
        print(f"User Input: {user_input}")
        print(f"Selected Model: {selected_model}")

    def run(self):
        self.root.mainloop()