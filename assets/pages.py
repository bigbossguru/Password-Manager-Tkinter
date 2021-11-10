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

        home_label = tk.Label(self, text='Password Manager'.upper(), font=('Helvetica', 15, 'bold'))
        home_label.pack(side='top', fill='both', expand=True)

        # Logo in home page
        image1 = Image.open(MEDIA_PATH.joinpath('passwd.png'))
        image1 = image1.resize((194, 115), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(image1)
        show_logo = tk.Label(self, image=logo)
        show_logo.image = logo
        show_logo.place(x=70, y=110)

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
        sign_in_label = tk.Label(self, text='Sign in page'.upper(), font=('Helvetica', 15, 'bold'))
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
        sign_up_label = tk.Label(self, text='Sign up page'.upper(), font=('Helvetica', 15, 'bold'))
        sign_up_label.pack(side='top', fill='both', pady=50)

        self.registration_form = registration.RegistrationForm(mainframe=self, controller=master)
        self.registration_form.pack(side='top')


class AccountPageView(BasePageInterface):
    """ This is person account after login """

    def __init__(self, master, *args, **kwargs) -> None:
        BasePageInterface.__init__(self, master, *args, **kwargs)
        self.access = True

        account_label = tk.Label(self, text='Account'.upper(), font=('Helvetica', 15, 'bold'))
        account_label.pack(fill='x', pady=30)
        
        self.table = ttk.Treeview(self, columns=('id','username','password'), show='headings', height=15)
        self.table.heading('#1', text='ID')
        self.table.column('#1', width=10)
        self.table.heading('#2', text='Username')
        self.table.column('#2', width=50)
        self.table.heading('#3', text='Password')
        self.table.column('#3', width=50)

        input_frame = tk.Frame(self)
        # input_frame.columnconfigure(0, weight=1)
        input_frame.pack(fill='both', padx=50)
        tk.Label(input_frame, text='username').grid(row=0, column=0, pady=2)
        self.entry_username = tk.Entry(input_frame, width=30)
        self.entry_username.grid(row=0, column=1, pady=2)

        tk.Label(input_frame, text='password').grid(row=1, column=0, pady=2)
        self.entry_passwd = tk.Entry(input_frame, width=30)
        self.entry_passwd.grid(row=1, column=1, pady=2)

        add_info_btn = ttk.Button(self, text='Add', command=self.clicked_add_info_to_db)
        add_info_btn.pack(pady=10)

        self.table.pack(fill='both', padx=5)

        logout_btn = ttk.Button(self, text='Logout', command=lambda: master.page_show('HomePageView'))
        logout_btn.pack(fill='x', padx=5, pady=5)
        
    def fill_info_from_db(self) -> None:
        rows = None
        try:
            with db.DataBaseConnector('user_data.db') as db_info:
                rows = db_info.fetch_info(f"{self.master.last_username}")
        except sqlite3.OperationalError:
            pass
        
        # clear treeview items
        for i in self.table.get_children():
            self.table.delete(i)

        if rows:
            for row in rows:
                self.table.insert("", tk.END, values=row)

        self.table.pack(fill='both', padx=5)
    
    def clicked_add_info_to_db(self) -> None:
        if self.entry_username.get() and self.entry_passwd.get():
            with db.DataBaseConnector('user_data.db') as db_add:
                db_add.insert_data(f""" INSERT INTO {self.master.last_username}(username, password) VALUES(?,?)""", (self.entry_username.get(), self.entry_passwd.get()))

        self.entry_username.delete(0, tk.END)
        self.entry_passwd.delete(0, tk.END)

        self.fill_info_from_db()


