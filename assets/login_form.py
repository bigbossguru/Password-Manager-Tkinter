import tkinter as tk


class LoginForm(tk.Frame):
    """ Sign in page will be contain Login form """

    def __init__(self, mainframe, *args, **kwargs) -> None:
        tk.Frame.__init__(self, mainframe, *args, **kwargs)

        # String variables containes user info
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        login_label = tk.Label(mainframe, text='Login', font=('Helvetica', 15)).pack(side='top', fill='both', pady=30)

        username_label = tk.Label(mainframe, text='Username').pack(side='top')
        username_input = tk.Entry(mainframe, width=30, textvariable=self.username).pack(side='top')


        passwd_label = tk.Label(mainframe, text='Password').pack(side='top')
        passwd_input = tk.Entry(mainframe, width=30, textvariable=self.password, show='*').pack(side='top')


        login_btn = tk.Button(self, text='Login').pack(side='top', pady=10)
