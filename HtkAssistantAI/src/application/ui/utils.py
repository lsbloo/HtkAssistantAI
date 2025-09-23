def show_toast(message, duration=2000):
        from ttkbootstrap.toast import ToastNotification
        toast = ToastNotification(title="Htk Assistant AI",
        message=message,
        duration=duration,
        bootstyle = "dark",
        alert=True,
        position=(300, 300, 'sw'))
        toast.show_toast()