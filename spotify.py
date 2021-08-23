import requests
from time import time


class SpotifyClient:
    CLIENT_ID       = "5d391859c36d4d7c9fb57967e6ea6b65"
    CLIENT_SECRET   = "1df449c2d13d435da980a2aa8fc3f1c9"
    CLIENT_AUTH     = None
    ACCESS_TOKEN    = None
    LAST_ACCESS     = None

    # ^^ Move to environment variable with dotenv and only save the encoding for usage.

    def __init__(self):
        self.ACCESS_TOKEN = self._request_token()

    def _request_token(self):
        payload = {
            "grant_type" : "client_credentials"
        }
        response = requests.post('https://accounts.spotify.com/api/token',
                                 auth=(self.CLIENT_ID, self.CLIENT_SECRET), data=payload)
        self.LAST_ACCESS = time()
        return response.json()['access_token']

    def get_spotify(self, query: str, limit:int=10): # Song to search for, number of songs to return
        if self.LAST_ACCESS >= self.LAST_ACCESS + 3600:
            self._request_token()

        result_list = list()
        query = query.replace(" ", "%20")
        header = {
            "type": "Accept: application/json",
            "Authorization": "Authorization Bearer {}".format(self.ACCESS_TOKEN)
        }
        response = requests.get('https://api.spotify.com/v1/search?q={}&type=track&market=US&limit={}'\
                                .format(query, limit), headers=header)

        for i in response.json()['tracks']['items']:
            result_list.append({
                "Link"      :   i['external_urls']['spotify'],
                "Name"      :   i['name'],
                "Artist"    :   i['album']['artists'][0]['name']
            })

        return result_list

