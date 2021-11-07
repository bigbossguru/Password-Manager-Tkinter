import tkinter as tk
import assets.pages as pf
from typing import Dict


class ManagerPagesView(tk.Frame):
    """ This is main frame which contains all frames(pages) """

    def __init__(self, *args, **kwargs) -> None:
        tk.Frame.__init__(self, *args, **kwargs)

        self.pack(side='top', fill='both', expand=True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.pages_view: Dict[str, pf.BasePageInterface] = dict()
        for page_item in (pf.HomePageView, pf.SignInPageView, pf.SignUpPageView, pf.AccountPageView):
            page_name = page_item.__name__
            page = page_item(master=self)
            self.pages_view[page_name] = page
            page.grid(row=0, column=0, sticky='nsew')
        
        self.page_show('HomePageView')

    def page_show(self, page_name: str) -> None:
        page = self.pages_view.get(page_name)
        if page.access:
            page.tkraise()