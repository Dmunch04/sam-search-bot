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

channelName = 'name'
apiKey = os.environ['apiToken']

def getSubs ():
    rawData = urlopen(URL.format(channelName, apiKey)).read()

    jsonData = json.loads(rawData)

    subsAmount = jsonData['items'][0]['statistics']['subscriberCount']

    return subsAmount
