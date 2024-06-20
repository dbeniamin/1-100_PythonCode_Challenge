import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# ## Spotify playlist with Musical Time Machine ## #

URL = "https://www.billboard.com/charts/hot-100/"
date = input("Get the Top 100 songs of the day you want!!\n Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"{URL}/{date}/")
music_top_page = response.text
soup_music = BeautifulSoup(music_top_page, "html.parser")
# print(soup_music)

# extract the "h3" that is nested in the "li" nested in "ul" nested in "li"

song_names_scrape = soup_music.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_scrape]

# print(song_names)  # print statement to check the list scraped

# >> add id / secret to environ variables

spotify_id = os.environ.get("SPOTIFY_ID")
# print(spotify_id)

spotify_secret = os.environ.get("SPOTIFY_SECRET")
# print(spotify_secret)

OAUTH_AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
OAUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"

# ### use below code with username="spotify username" as last entry in the api
# to generate token.txt needed to run the script ###

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=spotify_id,
        client_secret=spotify_secret,
        show_dialog=True,
        cache_path="token.txt",
    )
)

user_id = sp.current_user()["id"]
# print(user_id)


year = date.split("-")[0]
song_uris = []

# search the songs on spotify
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)  -> debug purposes
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# create a new playlist in Spotify
# https://spotipy.readthedocs.io/en/2.22.1/ - documentation used to create the playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

# add songs to playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
