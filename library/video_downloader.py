from pytube import YouTube
import youtube_dl
from youtube_dl import options
from flask import jsonify


def downloader(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': './%(title)s.webm',
        'noplaylist': True,
        'extractaudio': True,
        'audioformat': 'webm',
        'default_search': 'ytsearch1',
        'quite': True,
        'verbose': True,
        'version': True
    }
    with youtube_dl.YoutubeDL(ydl_opts) as y:
        try:
            r = y.extract_info(link, download=False)
            return r['formats'][-1]['url']
        except:
            return {'error': 'An error has occured'}
