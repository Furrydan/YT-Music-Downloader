from pytubefix import YouTube
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
        location = location.replace('/','\\')
        title = title.replace('/', '-')
        title = title.replace('\\', '-')
        title = title.replace('?', '-')
        title = title.replace(':', '-')
        title = title.replace('<', '-')
        title = title.replace('>', '-')
        title = title.replace('*', '-')
        title = title.replace('"', '-')
        title = title.replace('|', '-')
        os.replace(location + '\\song.m4a', f'{location}\\{title}.m4a')   
        os.remove('thumbnail.png')

        