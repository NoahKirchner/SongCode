## NOT WORKING BECAUSE OF YOUTUBE'S DRACONIAN API RESTRICTIONS
## MAY GOD HAVE MERCY UPON MY POOR SOUL


import requests
from time import time
from bs4 import BeautifulSoup

class YoutubeClient:
    AUTH_TOKEN  =   None

    #^^ Move this to a configuration file.

    def __init__(self):
        self.AUTH_TOKEN = "AIzaSyAgBnfLDrmMGrHlvJtGafrR0w9uheZBvME"

    def get_youtube(self, query:str, limit:int=10):
        response_list   = list()
        return_list     = list()
        if limit > 50:
            sanitized_limit = 50
        elif limit < 1:
            sanitized_limit = 1
        else:
            sanitized_limit = limit

        params = {
            "q"                 :   query,
            "key"               :   self.AUTH_TOKEN,
            "maxResults"        :   sanitized_limit,
            "type"              :   "video",
            "order"             :   "relevance",
            "relevanceLanguage" :   "en"

        }


        #response = requests.get('https://www.googleapis.com/youtube/v3/search', params=params).json()
        #print(response)
        #for url in [item['id']['videoId'] for item in response['items']]: # for url in response.json()'s return values
        #    response_list.append("https://www.youtube.com/watch?v={}".format(url))
        test_list = ["https://www.youtube.com/watch?v=MV_3Dpw-BRY","https://www.youtube.com/watch?v=DYYkJ0kwNss"]
        self._extract_title(test_list)


    def _extract_title(self, url_input:list):
        url_list = list()

        for item in url_input:
            url_list.append(requests.get(item))

        for item in url_list: #REMEMBER TO CHANGE BACK
            soup = BeautifulSoup(item, "html.parser")
            print(soup.head.title.text)
            print(soup.find('div').findChildren())

print(YoutubeClient().get_youtube("Little Dark Age", 2))

