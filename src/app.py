from tkinter import *
from downloader import Downloader
from music_app import MusicApp

class Downloader_GUI:
    def __init__(self):
        self.download = Downloader()
        self.music = MusicApp()

    def create_gui(self):

        window = Tk()
        window.geometry("840x840")
        window.title("Youtube Music Downloader")

        self.music.gui(window=window, downloader=self.download)

        window.mainloop()


