import tkinter as tk
import assets.login_form as login

class BasePageInterface(tk.Frame):
    """ This is base page Interface for all frames(pages) """

    def __init__(self, *args, **kwargs) -> None:
        tk.Frame.__init__(self, *args, **kwargs)


class HomePageView(BasePageInterface):
    """ This is Home page which shows two options choose sing-in or sing-up"""

    def __init__(self, mainframe, *args, **kwargs) -> None:
        BasePageInterface.__init__(self, mainframe, *args, **kwargs)

        home_label = tk.Label(self, text='Password Manager', font=('Helvetica', 15))
        home_label.pack(side='top', fill='both', expand=True)

        sing_in_btn = tk.Button(self, text='Sign in', command=lambda: mainframe.page_show('SignInPageView'))
        sing_up_btn = tk.Button(self, text='Sign up', command=lambda: mainframe.page_show('SignUpPageView'))
        sing_in_btn.pack(side='top', fill='both', padx=5, pady=5)
        sing_up_btn.pack(side='top', fill='both', padx=5, pady=5)


class SignInPageView(BasePageInterface):
    """ This is Sing In page which provides authentication user"""

    def __init__(self, mainframe, *args, **kwargs) -> None:
        BasePageInterface.__init__(self, mainframe, *args, **kwargs)

        home_btn = tk.Button(self, text='Home', command=lambda: mainframe.page_show('HomePageView'))
        home_btn.pack(side='top', fill='both', padx=5, pady=5)
        sign_in_label = tk.Label(self, text='Sign in page', font=('Helvetica', 15))
        sign_in_label.pack(side='top', fill='both', pady=100)

        login_form = login.LoginForm(mainframe=self)
        login_form.pack(side='top')


class SignUpPageView(BasePageInterface):
    """ This is Sing Up page which provides registration user"""

    def __init__(self, mainframe, *args, **kwargs) -> None:
        BasePageInterface.__init__(self, mainframe, *args, **kwargs)

        home_btn = tk.Button(self, text='Home', command=lambda: mainframe.page_show('HomePageView'))
        home_btn.pack(side='top', fill='both', padx=5, pady=5)
        sign_up_label = tk.Label(self, text='Sign up page', font=('Helvetica', 15))
        sign_up_label.pack(side='top', fill='both', expand=True)
        