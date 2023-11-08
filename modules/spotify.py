import base64
import requests
from configparser import ConfigParser


conf = ConfigParser()
conf.read('config.ini')


SPOTIFY_CLIENT_ID = conf.get("spotify", "SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = conf.get("spotify", "SPOTIFY_CLIENT_SECRET")
SPOTIFY_AUTH_CODE = conf.get("spotify", "SPOTIFY_AUTH_CODE")
REDIRECT_URI = conf.get("spotify", "REDIRECT_URI")
SPOTIFY_REFRESH_TOKEN = conf.get("spotify", "SPOTIFY_REFRESH_TOKEN")


# def get_refresh_token() -> dict:
#     data = {
#         'client_id': SPOTIFY_CLIENT_ID,
#         'client_secret': SPOTIFY_CLIENT_SECRET,
#         'grant_type': 'authorization_code',
#         'code': SPOTIFY_AUTH_CODE,
#         'redirect_uri': REDIRECT_URI
#     }

#     resp = requests.post('https://accounts.spotify.com/api/token', data=data)

#     return resp.json()


def get_access_token() -> str:

    credentials = f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "refresh_token",
        "refresh_token": SPOTIFY_REFRESH_TOKEN,
    }

    resp = requests.post(
        'https://accounts.spotify.com/api/token', headers=headers, data=data)
    if resp.status_code == 200:
        return resp.json().get("access_token")

    return None


def get_now_playing() -> dict | None:
    access_token = get_access_token()

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    resp = requests.get(
        'https://api.spotify.com/v1/me/player/currently-playing', headers=headers)
    
    if resp.status_code == 200:
        return resp.json()
    
    return None
