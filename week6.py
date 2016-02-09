#Using Python to access web data course - week 6 assignment - JSON

import urllib
import json

url = raw_input('Enter the url:\n')
if url == '1':
    url = 'http://python-data.dr-chuck.net/comments_42.json'
elif url == '2':
    url = 'http://python-data.dr-chuck.net/comments_214938.json'

input = urllib.urlopen(url).read()
print 'Retrieving', url

data = json.loads(input)

comment_sum = 0
counter = 0
print 'Retrieved', len(data['comments']), "comment items"

for item in data:
    while counter < len(data['comments']):
        comment_sum += int(data['comments'][counter]['count'])
        counter += 1

print 'Sum:', comment_sum
