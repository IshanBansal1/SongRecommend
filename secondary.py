import spotipy
import API
from collections import Counter
from tkinter import *
cid = API.cid
secret = API.secret
from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def start(playlist_url, explicit):
    window2 = Tk()
    window2.geometry("700x500")
    canvas = Canvas(window2, width=700, height=500)
    canvas.pack()
    img = PhotoImage(file="background2.png")
    canvas.create_image(350, 250, image=img)
    window2.update()
    playlist_id = playlist_url.replace('https://open.spotify.com/playlist/', 'spotify:playlist:')
    results = sp.playlist(playlist_id)
    if explicit == 'yes':
        explicit = 1
    else:
        explicit = 0

    ids = []

    for item in results['tracks']['items']:
        track = item['track']['id']
        ids.append(track)

    song_meta = {'id': [], 'genre': [], 'artist': [], 'name': [], 'uri': []}

    for song in ids:
        i = 0
        song_meta['index'] = i
        track = sp.track(song)
        song_meta['id'].append(song)
        artist = sp.artist(track["artists"][0]["external_urls"]["spotify"])
        uri = artist["uri"]
        song_meta['uri']+=[uri]
        song_meta['artist']+=[artist]
        genre=artist['genres']
        song_meta['genre']+=[genre]
        name = artist['name']
        song_meta['name']+=[name]
        i++1

    uri_count = dict(Counter(song_meta['uri']))
    biggest_uri = max(uri_count, key=uri_count.get)
    top_tracks = sp.artist_top_tracks(biggest_uri)

    recommend_songs = []
    if explicit == 1:
        for track in top_tracks['tracks'][:10]:
            recommend_songs+=[track['name']]
    if explicit == 0:
        for track in top_tracks['tracks'][:10]:
            if track['explicit'] == False:
                recommend_songs+=[track['name']]
    window2.destroy()
    window3 = Tk()

    window3.geometry("700x500")
    window3.configure(bg="#ffffff")
    i = Label(padx=70, pady=30)
    i.pack()
    canvas = Canvas(
        window3,
        bg="#ffffff",
        height=500,
        width=700,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background3_img = PhotoImage(file=f"background3.png")
    background3 = canvas.create_image(
        350.0, 250.0,
        image=background3_img)

    for song in recommend_songs:
        l = Label(window3, bg='#2C2C2C', fg='#3ACC63',  text=song)
        l.config(font=("Roboto", 14))
        l.pack(pady=7)

    window3.resizable(False, False)
    window3.mainloop()





