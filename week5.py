#Using Python to access web data course - week 5 Assignment - XML

import urllib
import xml.etree.ElementTree as ET

url = raw_input('Please enter url:\n')
if url == '1':
    url = 'http://python-data.dr-chuck.net/comments_42.xml'
elif url == '2':
    url = 'http://python-data.dr-chuck.net/comments_214934.xml'

fhand = urllib.urlopen(url)
print 'Retrieving: ', url

input = fhand.read()
data = ET.fromstring(input)
counts = data.findall('.//count')  #Using XPath here to retrieve the count tags
print 'Count', len(counts)

sum = 0
for item in data.findall('comments/comment'):   #using findall to retrieve count tags and iterate
    sum += int(item.find('count').text)

print 'Sum:', sum


