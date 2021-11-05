import tkinter as tk
import assets.main_view_frame as mv
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
        self.resizable(False, False)

        self.mainview = mv.MainViewFrame(self)
        self.mainview.pack(side='top', fill='both', expand=True)