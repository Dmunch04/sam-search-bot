import sys
import os
import json
if sys.version < '3':
    from urllib2 import urlopen
    from urllib import quote as urlquote
else:
    from urllib.request import urlopen
    from urllib.parse import quote as urlquote

URL = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={0}&key={0}'

channelName = 'Make Indies'
apiKey = os.environ['apiToken']

class Channel (self, name, link, subs):
    self.name = name
    self.link = link
    self.subs = subs

def getChannel ():
    rawData = urlopen(URL.format(channelName, apiKey)).read()

    jsonData = json.loads(rawData)

    channelName = jsonData['items'][0][]
    channelLink = jsonData['items'][0][]
    subsAmount = jsonData['items'][0]['statistics']['subscriberCount']

    result = Channel(channelName, channelLink, subsAmount)

    return result
