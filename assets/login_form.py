import tkinter as tk
import assets.data_base_connector as db


class LoginForm(tk.Frame):
    """ Sign in page will be contain Login form """

    def __init__(self, mainframe, controller, *args, **kwargs) -> None:
        self.last_username = ''
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

        self.lbl_passwd_err = tk.Label(mainframe, text='Password error')
        self.lbl_notexist_user = tk.Label(mainframe, text="Does not exist user")

    def clicked(self):
        if self.username.get() and self.password.get():
            # print(f"Login\nusername: {self.username.get()}\npassword: {self.password.get()}\n{'-'*30}\n")
            self.controller.set_last_username(self.username.get())
            with db.DataBaseConnector('registration_user.db') as db_log:
                rows = db_log.fetch_info('registration')

            flag_switch_page = False
            flag_passwd_error = False
            for row in rows:
                if (self.username.get() == row[1]) and (self.password.get() == row[3]):
                    flag_switch_page = True
                    self.controller.page_show('AccountPageView')
                elif (self.username.get() == row[1]) and (self.password.get() != row[3]):
                    flag_passwd_error = True
            
            self.lbl_passwd_err.pack_forget()
            self.lbl_notexist_user.pack_forget()
            if flag_passwd_error:
                self.lbl_passwd_err.pack()
            elif not flag_switch_page:
                self.lbl_notexist_user.pack()
                

            
            self.username.delete(0, tk.END)
            self.password.delete(0, tk.END)
        else:
            pass
    