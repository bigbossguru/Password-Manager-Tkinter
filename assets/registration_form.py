import tkinter as tk


class RegistrationForm(tk.Frame):
    """ Sign up page will be contain Registration form """

    def __init__(self, mainframe, *args, **kwargs) -> None:
        tk.Frame.__init__(self, mainframe, *args, **kwargs)

        self.username = tk.StringVar()
        self.email = tk.StringVar()
        self.password = tk.StringVar()

        reg_label = tk.Label(mainframe, text='Registration', font=('Helvetica', 15)).pack(side='top', fill='both', pady=30)
        
        login_label = tk.Label(mainframe, text='Username').pack(side='top')
        login_input = tk.Entry(mainframe, width=30, textvariable=self.username).pack(side='top')

        email_label = tk.Label(mainframe, text='Email').pack(side='top')
        email_input = tk.Entry(mainframe, width=30, textvariable=self.email).pack(side='top')

        passwd_label = tk.Label(mainframe, text='Password').pack(side='top')
        passwd_input = tk.Entry(mainframe, width=30, textvariable=self.password, show='*').pack(side='top')


        submit_btn = tk.Button(self, text='Submit').pack(side='top', pady=10)