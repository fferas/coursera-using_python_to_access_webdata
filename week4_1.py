# Using Python to access web data course - Week 4 assignment 1

import urllib
from bs4 import BeautifulSoup

url_input = raw_input("Enter the url, or 1 or 2:\n>")
if url_input == '1':
    url_input = 'http://python-data.dr-chuck.net/comments_42.html'
elif url_input == '2':
    url_input = 'http://python-data.dr-chuck.net/comments_214937.html'


data = urllib.urlopen(url_input).read()
soup = BeautifulSoup(data, 'html.parser')
#The second Assignment uses the code till here

tags = soup('span')
sum_of_content = 0

for tag in tags:
    sum_of_content += int(tag.contents[0])

print 'Sum', sum_of_content
