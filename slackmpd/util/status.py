def build_status(config, current_song):
    artist = current_song.get('artist') if current_song.get('artist') else "Unknown"
    song = current_song.get('title') if current_song.get('title') else "Unknown"
    album = current_song.get('album') if current_song.get('album') else "Unknown"
    status = config.getFormatting()
    status = status.replace("artist", artist).replace("song", song).replace("album", album)
    return "Listening to: \n" + status