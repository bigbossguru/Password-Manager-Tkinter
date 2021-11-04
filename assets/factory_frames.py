from abc import ABC, abstractmethod
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont


class AbstractBaseFrame(ABC, tk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        tk.Frame.__init__(self, master)
        self.title_font = tkFont.Font(family='Helvetica', size=20, weight=tkFont.BOLD)
        self.pack(side='top', fill='both', expand=True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
    
    @abstractmethod
    def label_create(self) -> None:
        pass

    @abstractmethod
    def button_create(self) -> None:
        pass


class MainFrame(AbstractBaseFrame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.label_create()
        self.button_create()

    def label_create(self) -> None:
        tk.Label(self, text='Password Manager', font=self.title_font).grid(column=0, row=0, sticky='ew', padx=5, pady=5)

    def button_create(self) -> None:
        ttk.Button(self, text='Sing up').grid(column=0, row=1, sticky='ew', padx=5, pady=5)
        ttk.Button(self, text='Sing in').grid(column=0, row=2, sticky='ew', padx=5, pady=5)


class AuthSignUpFrame(AbstractBaseFrame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.label_create()
        self.button_create()
    
    def label_create(self) -> None:
        tk.Label(self, text='Sing up', font=self.title_font).grid(column=0, row=0, sticky='ew', padx=5, pady=5)
    
    def button_create(self) -> None:
        ttk.Button(self, text='Home').grid(column=0, row=1, sticky='ew', padx=5, pady=5)


class AuthSignInFrame(AbstractBaseFrame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.label_create()
        self.button_create()
    
    def label_create(self) -> None:
        tk.Label(self, text='Sing in', font=self.title_font).grid(column=0, row=0, sticky='ew', padx=5, pady=5)
    
    def button_create(self) -> None:
        ttk.Button(self, text='Home').grid(column=0, row=1, sticky='ew', padx=5, pady=5)