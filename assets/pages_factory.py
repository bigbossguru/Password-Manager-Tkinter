import tkinter as tk
import assets.login_form as login
import assets.registration_form as registration

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

        sing_in_btn = tk.Button(self, text='Sign in', command=lambda: master.page_show('SignInPageView'))
        sing_up_btn = tk.Button(self, text='Sign up', command=lambda: master.page_show('SignUpPageView'))
        sing_in_btn.pack(side='top', fill='both', padx=5, pady=5)
        sing_up_btn.pack(side='top', fill='both', padx=5, pady=5)


class SignInPageView(BasePageInterface):
    """ This is Sing In page which provides authentication user"""

    def __init__(self, master, *args, **kwargs) -> None:
        BasePageInterface.__init__(self, master, *args, **kwargs)
        self.access = True

        home_btn = tk.Button(self, text='Home', command=lambda: master.page_show('HomePageView'))
        home_btn.pack(side='top', fill='both', padx=5, pady=5)
        sign_in_label = tk.Label(self, text='Sign in page'.upper(), font=('Helvetica', 15))
        sign_in_label.pack(side='top', fill='both', pady=50)

        login_form = login.LoginForm(mainframe=self, controller=master)
        login_form.pack(side='top')


class SignUpPageView(BasePageInterface):
    """ This is Sing Up page which provides registration user"""

    def __init__(self, master, *args, **kwargs) -> None:
        BasePageInterface.__init__(self, master, *args, **kwargs)
        self.access = True

        home_btn = tk.Button(self, text='Home', command=lambda: master.page_show('HomePageView'))
        home_btn.pack(side='top', fill='both', padx=5, pady=5)
        sign_up_label = tk.Label(self, text='Sign up page'.upper(), font=('Helvetica', 15))
        sign_up_label.pack(side='top', fill='both', pady=50)

        registration_form = registration.RegistrationForm(mainframe=self, controller=master)
        registration_form.pack(side='top')


class AccountPageView(BasePageInterface):
    """ This is person account after login """

    def __init__(self, master, *args, **kwargs) -> None:
        BasePageInterface.__init__(self, master, *args, **kwargs)
        self.access = True

        logout_btn = tk.Button(self, text='Logout', command=lambda: master.page_show('HomePageView'))
        logout_btn.pack(side='top', fill='both', padx=5, pady=5)

        account_label = tk.Label(self, text='Account'.upper(), font=('Helvetica', 15))
        account_label.pack(side='top', fill='both', pady=50)
        