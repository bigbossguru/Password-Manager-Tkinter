import assets.general_window as master

if __name__ == '__main__':
    mw = master.GeneralWindow(title='Password Manager', size=master.ScreenSize(width=350, height=550))
    mw.mainloop()
