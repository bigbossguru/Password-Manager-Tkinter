import tkinter as tk
import assets.factory_frames as ff
from typing import Dict, NamedTuple

class ScreenSize(NamedTuple):
    width: int
    height: int

class MainWindow(tk.Tk):
    def __init__(self, title: str, screen_size: ScreenSize) -> None:
        super().__init__()
        self.title(title)
        self.geometry(f"{screen_size.width}x{screen_size.height}")
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        #self.mainframe = ff.MainFrame(self)
        self.switching_frames()

    def switching_frames(self):
        self.frames: Dict[str, ff.AbstractBaseFrame] = {}
        for frame_item in (ff.MainFrame, ff.AuthSignInFrame, ff.AuthSignUpFrame):
            frame_name = frame_item.__name__
            frame = frame_item(self)
            self.frames[frame_name] = frame

        self.show_frame()
    
    def show_frame(self):
        frame = self.frames.get('MainFrame')
        frame.tkraise()

if __name__ == '__main__':
    mw = MainWindow(title='Password Manager', screen_size=ScreenSize(width=350, height=550))
    mw.mainloop()
