import tkinter as tk
import assets.data_base_connector as db


class LoginForm(tk.Frame):
    """ Sign in page will be contain Login form """

    def __init__(self, mainframe, controller, *args, **kwargs) -> None:
        tk.Frame.__init__(self, mainframe, *args, **kwargs)
        self.controller = controller

        tk.Label(mainframe, text='Login', font=('Helvetica', 15)).pack(side='top', fill='both', pady=30)

        tk.Label(mainframe, text='Username').pack()
        self.username = tk.Entry(mainframe, width=30)
        self.username.pack()

        tk.Label(mainframe, text='Password').pack()
        self.password = tk.Entry(mainframe, width=30, show='*')
        self.password.pack()

        tk.Button(self, text='Login', command=self.clicked).pack(side='top', pady=10)

    def clicked(self):
        if self.username.get() and self.password.get():
            print(f"Login\nusername: {self.username.get()}\npassword: {self.password.get()}\n{'-'*30}\n")
            with db.DataBaseConnector('registration_user') as db_log:
                pass
            self.controller.page_show('AccountPageView')
            self.username.delete(0, tk.END)
            self.password.delete(0, tk.END)
        else:
            pass