import pathlib
import sqlite3
import tkinter as tk
import tkinter.ttk as ttk
import assets.login_form as login
import assets.registration_form as registration
import assets.data_base_connector as db
from PIL import ImageTk, Image

ROOT_PATH = pathlib.Path().absolute()
MEDIA_PATH = ROOT_PATH.joinpath('media')

class BasePageInterface(tk.Frame):
    """ This is base page Interface for all frames(pages) """

    def __init__(self, *args, **kwargs) -> None:
        tk.Frame.__init__(self, *args, **kwargs)


class HomePageView(BasePageInterface):
    """ This is Home page which shows two options choose sing-in or sing-up"""

    def __init__(self, master, *args, **kwargs) -> None:
        BasePageInterface.__init__(self, master, *args, **kwargs)
        self.access = True

        home_label = tk.Label(self, text='Password Manager'.upper(), font=('Helvetica', 15))
        home_label.pack(side='top', fill='both', expand=True)

        # I don't know how it works
        # logo = ImageTk.PhotoImage(Image.open(MEDIA_PATH.joinpath('passwd.png')))
        # show_logo = tk.Label(self, image=logo)
        # show_logo.pack(fill='both', expand=True)

        sing_in_btn = ttk.Button(self, text='Sign in', command=lambda: master.page_show('SignInPageView'))
        sing_up_btn = ttk.Button(self, text='Sign up', command=lambda: master.page_show('SignUpPageView'))
        sing_in_btn.pack(side='top', fill='both', padx=5, pady=5)
        sing_up_btn.pack(side='top', fill='both', padx=5, pady=5)


class SignInPageView(BasePageInterface):
    """ This is Sing In page which provides authentication user"""

    def __init__(self, master, *args, **kwargs) -> None:
        BasePageInterface.__init__(self, master, *args, **kwargs)
        self.access = True

        home_btn = ttk.Button(self, text='Home', command=lambda: master.page_show('HomePageView'))
        home_btn.pack(side='top', fill='both', padx=5, pady=5)
        sign_in_label = tk.Label(self, text='Sign in page'.upper(), font=('Helvetica', 15))
        sign_in_label.pack(side='top', fill='both', pady=50)

        self.login_form = login.LoginForm(mainframe=self, controller=master)
        self.login_form.pack(side='top')


class SignUpPageView(BasePageInterface):
    """ This is Sing Up page which provides registration user"""

    def __init__(self, master, *args, **kwargs) -> None:
        BasePageInterface.__init__(self, master, *args, **kwargs)
        self.access = True

        home_btn = ttk.Button(self, text='Home', command=lambda: master.page_show('HomePageView'))
        home_btn.pack(side='top', fill='both', padx=5, pady=5)
        sign_up_label = tk.Label(self, text='Sign up page'.upper(), font=('Helvetica', 15))
        sign_up_label.pack(side='top', fill='both', pady=50)

        self.registration_form = registration.RegistrationForm(mainframe=self, controller=master)
        self.registration_form.pack(side='top')


class AccountPageView(BasePageInterface):
    """ This is person account after login """

    def __init__(self, master, *args, **kwargs) -> None:
        BasePageInterface.__init__(self, master, *args, **kwargs)
        self.access = True

        logout_btn = ttk.Button(self, text='Logout', command=lambda: master.page_show('HomePageView'))
        logout_btn.pack(side='top', fill='both', padx=5, pady=5)

        account_label = tk.Label(self, text='Account'.upper(), font=('Helvetica', 15))
        account_label.pack(side='top', fill='both', pady=50)
        
        self.table = ttk.Treeview(self, columns=('id','username','password'), show='headings')
        self.table.heading('#1', text='ID')
        self.table.column('#1', width=10)
        self.table.heading('#2', text='Username')
        self.table.column('#2', width=50)
        self.table.heading('#3', text='Password')
        self.table.column('#3', width=50)

    def fill_info_from_db(self) -> None:
        rows = None
        try:
            with db.DataBaseConnector('user_data.db') as db_info:
                rows = db_info.fetch_info(f"{self.master.last_username}")
        except sqlite3.OperationalError:
            pass
        
        if rows:
            for row in rows:
                self.table.insert("", tk.END, values=row)

        self.table.pack(fill='x', padx=10)
