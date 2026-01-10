from tkinterweb import HtmlFrame
import customtkinter as ctk
from core.utils.design.observer.observer import Subject
from core.utils.os_env.os_env import HtkOsEnvironment
import json

class WebViewFrame(Subject):
    def __init__(self, app_root, title="HTK Assistant AI - WebMode"):
        self._root = app_root
        self._app = ctk.CTkToplevel(self._root)
        self._app.title(title)
        self._app.geometry("800x750")
        self._app.iconbitmap(HtkOsEnvironment.get_absolute_path_for_resource(resource_file="no-face.ico"))  # Set the window icon
        self._web_frame = HtmlFrame(self._app, horizontal_scrollbar="auto", vertical_scrollbar="auto")
        self._web_frame.load_file(HtkOsEnvironment.get_absoloute_path_for_resource_page_html("webview_page.html"))
        self._web_frame.pack(expand=True, fill="both")
        ctk.set_appearance_mode("dark")
        
    
    def add_llm_response(self, text: str):
        try:
            div_responseArea = self._web_frame.document.getElementById("responseArea")
            div_responseArea.style.visibility = "visible"
            oldElement = div_responseArea.getElementsByTagName("p")
            if oldElement.length > 0:
                oldElement[0].remove()
            newElement = self._web_frame.document.createElement("p")
            newElement.textContent = text
            div_responseArea.appendChild(newElement)
        except Exception as e:
            print(f"Error adding LLM response to WebViewFrame: {e}")
    
    def destroy(self):
        self._web_frame.destroy()
        self._app.destroy()