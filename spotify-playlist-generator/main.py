import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from music_data import get_data

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")


def main():
    user_request = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    music_titles = get_data(user_request)

    sp_auth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://example.com",
                           scope="playlist-modify-private")
    # sp.get_access_token()
    sp_client = spotipy.Spotify(auth_manager=sp_auth)
    current_user_id = sp_client.current_user()["id"]
    year = user_request[:4]
    playlist = []
    for title in music_titles:
        result = sp_client.search(q=f"track:{title} year:{year}", type="track")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            playlist.append(uri)
        except IndexError:
            print(f"{title} doesn't exist in Spotify. Skipped.")

    playlist_id = sp_client.user_playlist_create(user=current_user_id,
                                                 name=f'{user_request} Billboard 100', public=False, collaborative=False, description='')["id"]
    sp_client.playlist_add_items(playlist_id=playlist_id, items=playlist)


if __name__ == '__main__':
    main()
