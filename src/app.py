from tkinter import *
from downloader import Downloader
from music_app import MusicApp

class Downloader_GUI:
    def __init__(self):
        self.download = Downloader()
        self.window = Tk()
        self.music = MusicApp(self.window)

    def create_gui(self):

        self.window.geometry("840x840")
        self.window.title("Youtube Music Downloader")

        self.music.heading()

        self.music.mode()

        self.music.inputs()

        self.music.gui(downloader=self.download)

        self.window.mainloop()


