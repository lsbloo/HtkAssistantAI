import tkinter as tk
from tkinter import ttk
from core.utils.design.observer.observer import Subject
from core.LLMs.groq.options import input_groq_options
from core.log.htk_logger import HtkApplicationLogger
from .utils import show_toast
from PIL import Image, ImageTk, ImageDraw
from core.utils.os_env.os_env import HtkOsEnvironment
import customtkinter as ctk


class MainFrame(Subject):
    def create_root(self):
        self.root.title(self.title)  # Set the title of the main window
        self.root.geometry("800x600")  # Set the size of the main window
        self.root.configure(bg='#1E1E1E')  # Set the background color of the main window
        self.root.resizable(False, False)  # Make the window non-resizable
        self.root.iconbitmap(HtkOsEnvironment.get_absolute_path_for_resource(resource_file="no-face.ico"))  # Set the window icon
        
        
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
            image_path = Image.open(HtkOsEnvironment.getImageProfileInEnvironment())  #  # Replace with your image path
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

    def draw_rounded_rectangle(self, canvas, x1, y1, x2, y2, radius=25, fill='white'):
        points = [
            (x1 + radius, y1),
            (x2 - radius, y1),
            (x2 - radius, y1),
            (x2, y1),
            (x2, y1 + radius),
            (x2, y2 - radius),
            (x2, y2 - radius),
            (x2, y2),
            (x2 - radius, y2),
            (x1 + radius, y2),
            (x1 + radius, y2),
            (x1, y2),
            (x1, y2 - radius),
            (x1, y1 + radius),
            (x1, y1 + radius),
            (x1, y1),
        ]
        return canvas.create_polygon(points, smooth=True, fill=fill)
    
    def create_input_area(self):
        # Create a label for the text input
        self.input_label = tk.Label(self.root, text="No que você está pensando hoje?", bg="#1E1E1E", fg='white', font=("Arial", 12))
        self.input_label.place(x=300, y=210)
                
        # Create a text box for user input
        self.text_input = ctk.CTkTextbox(self.root, height=75, width=700, font=('Arial', 12), fg_color='#252526', text_color='white', corner_radius=10)
        self.text_input.place(x=30, y=240)
    
    def create_output_area(self):
        # Create a text box for user input
        self.text_input_output = ctk.CTkTextbox(self.root, height=120, 
                                                width=700, font=('Arial', 12), 
                                                fg_color='#252526', 
                                                text_color='white', 
                                                corner_radius=10,
                                                )
        self.text_input_output.place(x=30, y=330)
        self.text_input_output.configure(state='disabled')
        

    def create_model_selection(self):
        # Create a label for the model selection
        #self.model_label = tk.Label(self.root, text="Modelos Disponiveis", bg='#1E1E1E', fg='white', font=("Arial", 12))
        #self.model_label.place(x=30, y=40)

        # Create a dropdown menu for model selection
        self.model_var = tk.StringVar(value="Selecione um modelo")
        self.model_dropdown = ttk.Combobox(self.root, textvariable=self.model_var, state="readonly", font=("Arial", 12))
        self.model_dropdown['values'] = self.setupModelsBasedInEnvironment()
        self.model_dropdown.place(x=10, y=120)
        
        self.model_dropdown.bind("<<ComboboxSelected>>", self.on_model_change)
    
    def on_model_change(self, event):
        selected_model = self.model_var.get()
        
        input_options = {}
        if selected_model == "Groq":
            input_options = input_groq_options()
        
        
        self.logger.log(f"Selected Model: {selected_model} with Input Options: {input_options}")
        
        if input_options is not None:
            self.create_options_area(input_options)
            
        
    
    def setupOptionsBasedInModelOptions(self, input_options):
        values = []
        for key, value in input_options.items():
            if value:
                values.append(key)
        
        self.logger.log(f"Input Options Values: {values}")
        return values
            
        
    def create_options_area(self, input_options):
        self.model_label = tk.Label(self.root, text="Opções do modelo:", bg='#1E1E1E', fg='white', font=("Arial", 12))
        self.model_label.place(x=570, y=120)
        
        self.model_input_option_var = tk.StringVar(value="Chats")
        self.model_input_option_dropdown = ttk.Combobox(self.root, textvariable=self.model_input_option_var, state="readonly", font=("Arial", 12))
        self.model_input_option_dropdown['values'] = self.setupOptionsBasedInModelOptions(input_options=input_options)
        self.model_input_option_dropdown.place(x=575, y=150)
        self.model_input_option_dropdown.bind("<<ComboboxSelected>>", self.on_model_change_options_area)
        
    
    def on_model_change_options_area(self, event):
        selected_option = self.model_input_option_var.get()
        self.logger.log(f"Selected Model Option: {selected_option}")

        if selected_option == "chat_with_roles":
            self.option_role_menu = ctk.CTkOptionMenu(self.root, values=["assistant", "user", "system"], 
                              command=lambda choice: self.set_option_role_choice(choice))
            
            self.option_role_menu.place(x=575, y=180) 
        else:
            self.option_role_menu.pack_forget()
            self.option_role_menu.destroy()
            self.root.update()
            
    def set_option_role_choice(self, choice):
        self.option_role_choice = choice
        self.logger.log(f"Selected Role: {self.option_role_choice}")
      
    def create_button(self): 
        # Create a submit button
        self.submit_button = ctk.CTkButton(self.root, text='Submeter', command=self.submit)
        self.submit_button.place(x=400, y=500)
       
    def setupModelsBasedInEnvironment(self):
        avialiableModelsByEnv = HtkOsEnvironment.getModelsAvailableInEnvironment()
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
        self._observers = []
        self.title = title
        self.root = tk.Tk()  # Create the main window
        self.create_root()
        self.create_circular_widget()
        self.create_model_selection()
        self.create_input_area()
        self.create_output_area()
        self.create_button()
        self.option_role_menu = None
        self.option_role_choice = None
        self.logger = HtkApplicationLogger()
       

    def submit(self):
        # Get the text input and selected model
        user_input = self.text_input.get("1.0", tk.END).strip()
        selected_model = self.model_var.get()
        selected_option = self.model_input_option_var.get() if hasattr(self, 'model_input_option_var') else None

        # Print the input and selected model (replace this with your processing logic)
        #print(f"User Input: {user_input}")
        #print(f"Selected Model: {selected_model}")
        
        if(selected_model == "Selecione um modelo" or selected_model == "No models available"):
            show_toast("Por favor, selecione um modelo válido.", duration=3000)
            return
        
        self.notify_observers({
            'user_input': user_input,
            'selected_model': selected_model,
            'selected_option': selected_option,
            'option_role_choice': self.option_role_choice
        })
        
    def update_chat(self, response):
        self.text_input_output.configure(state='normal')
        self.text_input_output.delete("1.0", tk.END)
        self.text_input_output.insert(tk.END, response)
        self.text_input_output.configure(state='disabled')

    def run(self):
        self.root.mainloop()