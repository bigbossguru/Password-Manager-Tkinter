import sys
import tkinter as tk
import assets.manager_pages as mp
from assets.pages import MEDIA_PATH
from typing import NamedTuple


class ScreenSize(NamedTuple):
    width: int
    height: int


class GeneralWindow(tk.Tk):
    """ This is based window for whole software """

    def __init__(self, title: str, size: ScreenSize, *args, **kwargs) -> None:
        tk.Tk.__init__(self, *args, **kwargs)

        self.title(title)
        self.geometry(f"{size.width}x{size.height}")
        if sys.platform == 'win32':
            self.iconbitmap(MEDIA_PATH.joinpath('lock.ico'))
        else:
            pass
        self.resizable(False, False)

        self.mainview = mp.ManagerPagesView(self)
        self.mainview.pack(side='top', fill='both', expand=True)