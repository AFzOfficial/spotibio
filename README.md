# SpotiBio
Shows Your Current Listening Music From Spotify in Your Telegram Bio.  

  
## How to Run?
It is recommended to run this bot on a server But you can also run it on your pc.  
To run this project, we have several steps that we need to do in order:

### Step 1: Get your Spotify `Client id` and `Client secret` 
Visit your [Spotify developers dashboard](https://developer.spotify.com/dashboard/applications) then select or create your app. Note down your Client ID, Client Secret, and Redirect URI in a convenient location to use in Step 2.

### Step 2: Get your access code
Visit the following URL after replacing `$CLIENT_ID`, `$SCOPE`, and `$REDIRECT_URI` with the information you noted in Step 1.

```bash
https://accounts.spotify.com/authorize?response_type=code&client_id=$CLIENT_ID&scope=$SCOPE&redirect_uri=$REDIRECT_URI
```

My url looked like this

```bash
https://accounts.spotify.com/authorize?response_type=code&client_id=$CLIENT_ID&scope=user-read-currently-playing&redirect_uri=http://localhost:4000
```

### Step 3: Get `Code` from the redirect URL
I was redirected to the following URL because my redirect URI was set to http://localhost:4000. In place of `$CODE` there was a very long string of characters. Copy that string and note it down for use in Step 4.

```bash
http://localhost:4000/?code=$CODE
```

### Step 4: Get the refresh token
Running the following CURL command will result in a JSON string that contains the refresh token, in addition to other useful data. Again, either replace or export the following variables in your shell `$CILENT_ID`, `$CLIENT_SECRET`, `$CODE`, and `$REDIRECT_URI`.

```bash
curl -X GET "https://accounts.spotify.com/authorize?response_type=code&client_id=$CLIENT_ID&client_secret=$CLIENT_SECRET&scope=user-read-currently-playing&redirect_uri=$REDIRECT_URI"
```

The result will be a JSON string similar to the following. Take the `refresh_token` and save that in a safe, private place. This token will last for a very long time and can be used to generate a fresh `access_token` whenever it is needed.

### Step 5: Get your Telegram account `api_id` and `api_hash`
Go to [my.telegram.org](https://my.telegram.org) and login to your account  
Create a App in [API Development Tools](https://my.telegram.org/apps) note down your `api_id` and `api_hash`.

### Step 6: Set your Spotify and Telegram Credentials in config.ini
```
cp config.ini.example config.ini
```
### Step 8: Setup venv
```bash
python3 -m venv .venv
```
### Step 9: Activate the venv
```bash
source .venv/bin/activate
```
### Step 10: Install Depends
```bash
pip install -r requirements.txt
```
### Step 11: Run the Bot and Login to your account
```bash
# start a tmux session
tmux

python3 main.py
```

## References

[SpotiBio](https://github.com/pooriaanv/spotibio)

## License

[MIT](https://choosealicense.com/licenses/mit/)
