import os
from pprint import pprint

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from music_data import get_data

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
def main():
    # user_request = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    # get_data(user_request)

    scope = "user-library-read"

    sp_auth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://example.com", scope="playlist-modify-private")
    # sp.get_access_token()
    sp_client = spotipy.Spotify(auth_manager=sp_auth)
    # print(sp_client.id)
    current_user_id = sp_client.current_user()["id"]
    # print(current_user_id)
    query = {
        "artist":"Justin Bieber",
        "track":"Baby",
        "year":"2010"
    }
    result = sp_client.search(q=query, type="track")
    pprint(result)
if __name__ == '__main__':
    main()
