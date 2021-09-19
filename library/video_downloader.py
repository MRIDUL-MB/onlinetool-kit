import youtube_dl


def downloader(link, genre):
    if genre == "video":
        genre = -1
    elif genre == "audio":
        genre = 0
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': './%(title)s.webm',
        'noplaylist': True,
        'extractaudio': True,
        'audioformat': 'webm',
        'default_search': 'ytsearch1',
        'quite': True,
        'verbose': True,
        'version': True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as y:
        try:
            r = y.extract_info(link, download=False)
            return r['formats'][genre]['url']

        except:
            return {'error': 'An error has occured'}
