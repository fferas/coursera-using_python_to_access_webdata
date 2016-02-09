# Assignment 2 - uses Fikret.html and Prince.html
import urllib
import json
import ssl
from bs4 import BeautifulSoup
import re

url_input = raw_input("Enter the url, or 1 or 2:\n>")
if url_input == '1':
    url_input = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
elif url_input == '2':
    url_input = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Prince.html'

count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: '))
names = []

for i in range(count):
    print "Opening:", url_input
    scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    uh = urllib.urlopen(url_input, context=scontext)

    data = uh.read()
    soup = BeautifulSoup(data, 'html.parser')

    tags = soup('a')

    pos_count = 0

    for tag in tags:
        pos_count += 1
        if pos_count == position:
            url_input = tag.get('href', None)

    name = str(re.findall('by_(\S+).html', url_input))
    names.append(name)

print '\nLast url:', url_input
print "Names:", names, "\nLast name:", names[len(names)-1]

