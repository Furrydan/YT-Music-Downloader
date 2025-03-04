from tkinter import *
from tkinter import filedialog

class MusicApp():

    def __init__(self, window):
        self.status_text = StringVar(window, "Copy and Paste Video URL")
        self.download_path = StringVar(window)
        self.link = StringVar(window)
        self.window = window
        self.mode_button = BooleanVar(window)

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

        def soloButton():
            self.mode_button.set(False)

        solo_button = Button(self.window,
                             text="Solo")
        solo_button.config(command=soloButton,
                           font=('Arial',20))
        solo_button.pack()

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
            try:
                downloader.download(self.link.get(), self.download_path.get())
                self.link.set("")
                text_instructions = "Downloaded File"
            except:
               text_instructions = "Wrong Link"
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