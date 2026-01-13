import customtkinter as ctk
from PIL import Image
from core.utils.os_env.os_env import HtkOsEnvironment
class Toast(ctk.CTkToplevel):
    def __init__(self, parent, message, duration=3000):
        super().__init__(parent)

        self.duration = duration
        self.alpha = 0.0
        self.title = "HtkAssistantAI - Warning"

        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.attributes("-alpha", self.alpha)
        self.configure(fg_color="#2B2B2B", )

        # Container principal
        container = ctk.CTkFrame(
            self,
            fg_color="#2B2B2B",
            bg_color="#2B2B2B",
            border_width=2,
            border_color="#3A3A3A"
        )
        container.pack(fill="both", expand=True, padx=1, pady=1)

        icon = ctk.CTkImage(
            Image.open(
                HtkOsEnvironment.get_absolute_path_for_resource_icon("warning.png")
            ),
            size=(20, 20),
        )

        content = ctk.CTkFrame(container, fg_color="transparent")
        content.pack(padx=12, pady=10)

        icon_label = ctk.CTkLabel(
            content,
            image=icon,
            text="",
            width=20
        )
        icon_label.pack(side="left", padx=(0, 10))

        text_label = ctk.CTkLabel(
            content,
            text=message,
            font=("Segoe UI", 15),
            text_color="#FFFFFF",
            wraplength=260,
            justify="left"
        )
        text_label.pack(side="left")

        self.update_idletasks()
        self._set_position(parent)
        
        self._fade_in()
        self.after(self.duration, self._fade_out)

    def _set_position(self, parent):
        x = parent.winfo_x() + parent.winfo_width() - self.winfo_reqwidth() - 260
        y = parent.winfo_y() + parent.winfo_height() - self.winfo_reqheight() - 360
        self.geometry(f"+{x}+{y}")

    def _fade_in(self):
        if self.alpha < 1.0:
            self.alpha += 0.08
            self.attributes("-alpha", self.alpha)
            self.after(15, self._fade_in)

    def _fade_out(self):
        if self.alpha > 0:
            self.alpha -= 0.08
            self.attributes("-alpha", self.alpha)
            self.after(15, self._fade_out)
        else:
            self.destroy()



def show_toast(parent, message, duration=2000):
    Toast(parent, message, duration)
