from tkinter import *
from tkinter import filedialog

class MusicApp():

    def __init__(self, window):
        self.status_text = StringVar(window, "Copy and Paste Video URL")
        self.download_path = StringVar(window)
        self.link = StringVar(window)
        self.window = window
        self.mode_button = BooleanVar(window, True)

    def heading(self):
        heading = Label(self.window,
                        text="Youtube Music Downloader",
                        font=('Arial', 40, 'bold'),
                        fg= 'white',
                        bg= 'red',
                        padx=20,
                        pady=30)
        heading.pack()

    def mode(self):

        mode_frame = Frame(self.window)
        mode_frame.pack()

        def soloButton():
            self.mode_button.set(True)
            solo_button.config(bg='black', fg='red')
            playlist_button.config(bg='white', fg='black')
        def playlistButton():
            self.mode_button.set(False)
            solo_button.config(bg='white', fg='black')
            playlist_button.config(bg='black', fg='red')


        solo_button = Button(mode_frame,
                             text="Solo")
        solo_button.config(command=soloButton,
                           font=('Arial',20, 'bold'),
                           width=10,
                           bg='black',
                           fg='red')
        
        playlist_button = Button(mode_frame,
                                text="Playlist")
        playlist_button.config(command=playlistButton,
                               font=('Arial', 20, 'bold'),
                               width=10)
                
        solo_button.grid(row=0,column=0, padx=15)
        playlist_button.grid(row=0,column=2,padx=15)

    def inputs(self):
        instructions = Label(self.window,
                             textvariable=self.status_text ,
                             font=('Arial', 20),
                             pady=20,
                             padx=20)
        instructions.pack()

        url = Entry(self.window, textvariable=self.link)
        url.config(font=('Arial', 20),
                bg='grey',
                width=45,
                cursor="arrow")
        url.pack()

        download_instructions = Label(self.window,
                             text="Select Download Location",
                             font=('Arial', 20),
                             pady=20,
                             padx=20)
        
        download_instructions.pack()

        download_path = Label(self.window,
                        textvariable=self.download_path,
                        font=('Arial', 20),
                        bg='grey',
                        width=45)
        download_path.pack()

    def gui(self, downloader):

        def get_filepath():
            filepath_content = filedialog.askdirectory()
            self.download_path.set(filepath_content)

        def download_button():
            if self.mode_button.get() == True:
                try:
                    downloader.get_details_solo(self.link.get())
                    downloader.download(self.download_path.get())
                    self.link.set("")
                    text_instructions = "Downloaded File"
                except:
                    text_instructions = "Wrong Link"
                self.status_text.set(text_instructions)
            else:
                #try:
                downloader.get_details_playlist(self.link.get())
                downloader.download_playlist(self.download_path.get())
                self.link.set("")
                text_instructions = "Downloaded File"
                #except:
                    #text_instructions = "Wrong Link"
                self.status_text.set(text_instructions)

       

        search_path = Button(self.window,
                            text="Download location")
        search_path.config( command=get_filepath,
                            font=('Arial', 20, 'bold'))
        search_path.pack()

        download = Button(self.window, text="Download")
        download.config(command=download_button,
                        font=('Arial', 20, 'bold'),
                        bg='white',
                        fg='red',
                        activebackground='black',
                        activeforeground='red')
        download.pack()