from pytubefix import YouTube,Playlist
import urllib.request
import music_tag
import os

def download_song(yt,location, filename):
        stream = yt.streams.get_audio_only()
        stream.download(output_path=location, filename=filename)

def get_thumbnail_img(url,filename):
    urllib.request.urlretrieve(url, f'thumbnails/{filename[:-4]}.png')

def set_attributes(filename, location, title):
    audiofile = music_tag.load_file(location + f'/{filename}')
    audiofile['title'] = title
    with open(f'thumbnails/{filename[:-4]}.png', 'rb') as img_in:
        audiofile['artwork'] = img_in.read()
    audiofile.save()
    os.remove(f'thumbnails/{filename[:-4]}.png')
    img_in.close()

def correct(title):
        title = title.replace('/', '-')
        title = title.replace('\\', '-')
        title = title.replace('?', '-')
        title = title.replace(':', '-')
        title = title.replace('<', '-')
        title = title.replace('>', '-')
        title = title.replace('*', '-')
        title = title.replace('"', '-')
        title = title.replace('|', '-')
        title += '.m4a'
        return title


class Downloader():
    def __init__(self):
         self.title = ""
         self.filename = ""
         self.thumbnail_url = ""
         self.playlist = {}
         self.solo_obj = None
         self.playList_obj = None

    def get_details_solo(self, link):
        self.solo_obj = YouTube(link)
        self.title = self.solo_obj.title
        self.thumbnail_url = self.solo_obj.thumbnail_url
        self.filename = correct(self.title)
        get_thumbnail_img(self.thumbnail_url,self.filename)

    def get_details_playlist(self, link):
        self.playList_obj = Playlist(link)
        for song in self.playList_obj.videos:
            url = song.thumbnail_url
            filename = correct(song.title)
            get_thumbnail_img(url, filename)
            self.playlist[song.title] = filename
        

    def download(self, location):

        download_song(self.solo_obj, location, self.filename)

        set_attributes(self.filename, location, self.title)

    def download_playlist(self, location):
        
        for song in self.playList_obj.videos:
        
            download_song(song, location, self.playlist[song.title])
            
            set_attributes(self.playlist[song.title], location, song.title)
        