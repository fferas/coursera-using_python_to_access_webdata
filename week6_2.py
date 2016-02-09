#Using Python to access web data course - Week 6 assignment - JSON + API

import urllib
import json

api_url = 'http://python-data.dr-chuck.net/geojson?'

while True:
    location = raw_input('Enter location:\n')
    if len(location) < 1 : break

    url = api_url + urllib.urlencode({'sensor':'false', 'address':location})
    print 'Retrieving', url

    input = urllib.urlopen(url).read()
    data = json.loads(input)

    print 'Place ID:', data['results'][0]['place_id']

