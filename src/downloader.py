from pytubefix import YouTube,Playlist
from aux_func import correct
import urllib.request
import music_tag
import os


class Downloader():

    def download(self, link, location):
        yt = YouTube(link)
        stream = yt.streams.get_audio_only()
        stream.download(output_path=location, filename='song.m4a')
        url = yt.thumbnail_url
        title = yt.title
        urllib.request.urlretrieve(url, 'thumbnail.png')
        audiofile = music_tag.load_file(location + '/song.m4a')
        audiofile['title'] = title
        with open('thumbnail.png', 'rb') as img_in:
            audiofile['artwork'] = img_in.read()
        audiofile.save()
        img_in.close()   
        title = correct(title)
        os.replace(location + '/song.m4a', f'{location}/{title}.m4a')   
        os.remove('thumbnail.png')

    def download_playlist(self, link, location):
        playList = Playlist(link)
        for song in playList:
            stream = song.song.get_audio_only()
            stream.download(output_path=location, filename='song.m4a')
            url = song.thumbnail_url
            title = song.title
            urllib.request.urlretrieve(url, 'thumbnail.png')
            audiofile = music_tag.load_file(location + '/song.m4a')
            audiofile['title'] = title
            with open('thumbnail.png', 'rb') as img_in:
                audiofile['artwork'] = img_in.read()
            audiofile.save()
            img_in.close()   
            title = correct(title)
            os.replace(location + '/song.m4a', f'{location}/{title}.m4a')   
            os.remove('thumbnail.png')
        