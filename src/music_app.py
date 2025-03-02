from tkinter import *
from tkinter import filedialog

class MusicApp():
    def gui(self, window, downloader):

        def get_filepath():
            filepath_content = filedialog.askdirectory()
            download_path.config(text=filepath_content)

        def download_button():
#            try:
            downloader.download(url.get(), download_path.cget('text'))
            url.delete(0,END)
            text_instructions = "Downloaded File"
            #except:
               #text_instructions = "Wrong Link"
            instructions.config(text=text_instructions)

        heading = Label(window,
                        text="Youtube Music Downloader",
                        font=('Arial', 40, 'bold'),
                        fg= 'white',
                        bg= 'red',
                        padx=20,
                        pady=30)
        heading.pack()

        instructions = Label(window,
                             text="Copy and Paste URL",
                             font=('Arial', 20),
                             pady=20,
                             padx=20)
        
        instructions.pack()

        url = Entry()
        url.config(font=('Arial', 20),
                bg='grey',
                width=45)
        url.pack()

        download_instructions = Label(window,
                             text="Select Download Location",
                             font=('Arial', 20),
                             pady=20,
                             padx=20)
        
        download_instructions.pack()

        download_path = Label(window,
                        text="",
                        font=('Arial', 20),
                        bg='grey',
                        width=45)
        download_path.pack()

        search_path = Button(window,
                            text="Download location")
        search_path.config( command=get_filepath,
                            font=('Arial', 20, 'bold'))
        search_path.pack()

        download = Button(window, text="Download")
        download.config(command=download_button,
                        font=('Arial', 20, 'bold'),
                        bg='white',
                        fg='red',
                        activebackground='black',
                        activeforeground='red')
        download.pack()