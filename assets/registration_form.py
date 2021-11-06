import tkinter as tk


class RegistrationForm(tk.Frame):
    """ Sign up page will be contain Registration form """

    def __init__(self, mainframe, controller, *args, **kwargs) -> None:
        tk.Frame.__init__(self, mainframe, *args, **kwargs)
        self.controller = controller

        # String variables containes user info
        self.username = tk.StringVar()
        self.email = tk.StringVar()
        self.password = tk.StringVar()

        tk.Label(mainframe, text='Registration', font=('Helvetica', 15)).pack(side='top', fill='both', pady=30)
        
        tk.Label(mainframe, text='Username').pack(side='top')
        tk.Entry(mainframe, width=30, textvariable=self.username).pack(side='top')

        tk.Label(mainframe, text='Email').pack(side='top')
        tk.Entry(mainframe, width=30, textvariable=self.email).pack(side='top')

        tk.Label(mainframe, text='Password').pack(side='top')
        tk.Entry(mainframe, width=30, textvariable=self.password, show='*').pack(side='top')

        tk.Button(self, text='Submit', command=self.clicked).pack(side='top', pady=10)
    
    def clicked(self):
        if self.username.get() and self.email.get() and self.password.get():
            print(f"Registration\nusername: {self.username.get()}\nemail: {self.email.get()}\npassword: {self.password.get()}\n{'-'*30}\n")
            self.controller.page_show('AccountPageView')
            self.username.set('')
            self.email.set('')
            self.password.set('')
        else: 
            pass