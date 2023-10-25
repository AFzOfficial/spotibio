import aiocron
from pyrogram import Client
from configparser import ConfigParser

from modules import spotify


conf = ConfigParser()
conf.read('config.ini')


API_ID = conf.get('account', 'API_ID')
API_HASH = conf.get('account', 'API_HASH')
PHONE_NUMBER = conf.get('account', 'PHONE_NUMBER')


app = Client(
    'spotify-bot',
    api_id=API_ID,
    api_hash=API_HASH,
    phone_number=PHONE_NUMBER,
)


async def update_bio():
    song = spotify.get_now_playing()

    if song["item"] != None:
        name = song["item"]["name"]
        artists = ", ".join(artist['name']
                            for artist in song['item']['artists'])

        await app.update_profile(bio=f"Now Listening {name} - {artists} on Spotify! 🎧")
    await app.update_profile(bio="Not Listening Music Now! 🎧")




@aiocron.crontab('*/2 * * * *')
async def profile_updater():
    await update_bio()



if __name__ == '__main__':
    profile_updater.start()
    profile_updater.stop()



app.run()
