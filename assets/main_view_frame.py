import tkinter as tk
import assets.pages_factory as pf
from typing import Dict


class MainViewFrame(tk.Frame):
    """ This is main frame which contains all frames(pages) """

    def __init__(self, *args, **kwargs) -> None:
        tk.Frame.__init__(self, *args, **kwargs)

        self.pages_view: Dict[str, pf.BasePageInterface] = dict()
        for page_item in (pf.HomePageView, pf.SingInPageView, pf.SingUpPageView):
            page_name = page_item.__name__
            page = page_item(mainframe=self)
            self.pages_view[page_name] = page
            page.grid(row=0, column=0, sticky='nsew')
        
        self.page_show('HomePageView')

    def page_show(self, page_name: str) -> None:
        page = self.pages_view.get(page_name)
        page.tkraise()