import tkinter as tk


class RegistrationForm(tk.Frame):
    """ Sign up page will be contain Registration form """

    def __init__(self, mainframe, controller, *args, **kwargs) -> None:
        tk.Frame.__init__(self, mainframe, *args, **kwargs)
        self.controller = controller

        tk.Label(mainframe, text='Registration', font=('Helvetica', 15)).pack(side='top', fill='both', pady=30)
        
        tk.Label(mainframe, text='Username').pack()
        self.username = tk.Entry(mainframe, width=30)
        self.username.pack()

        tk.Label(mainframe, text='Email').pack()
        self.email = tk.Entry(mainframe, width=30)
        self.email.pack()

        tk.Label(mainframe, text='Password').pack()
        self.password = tk.Entry(mainframe, width=30, show='*')
        self.password.pack()

        tk.Button(self, text='Submit', command=self.clicked).pack(side='top', pady=10)
    
    def clicked(self):
        if self.username.get() and self.email.get() and self.password.get():
            print(f"Registration\nusername: {self.username.get()}\nemail: {self.email.get()}\npassword: {self.password.get()}\n{'-'*30}\n")
            self.controller.page_show('AccountPageView')
            self.username.delete(0, tk.END)
            self.email.delete(0, tk.END)
            self.password.delete(0, tk.END)
        else: 
            pass