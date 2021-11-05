import tkinter as tk


class RegistrationForm(tk.Frame):
    """ Sign up page will be contain Registration form """

    def __init__(self, mainframe, *args, **kwargs) -> None:
        tk.Frame.__init__(self, mainframe, *args, **kwargs)