'''
Created on Oct 30, 2017

@author: chiragm
'''
'''
ReadMe :: I extracted fb expedia page and analyzed content of site.
          Using beautiful soup I found tags which contains posts and extrated top 8 posts of it and printed
'''

from bs4 import BeautifulSoup
from six.moves.urllib.request import urlopen


output = open('fbposts_file.txt', 'w')
link = "https://www.facebook.com/expedia/"
response = urlopen(link)
content = response.read()

posts = {}

soup = BeautifulSoup(content, 'lxml')
count = 0
for ele in soup.findAll(attrs={'class' : '_5pbx userContent'})[:8]:
    count+=1
#     print(ele.p.text)
    posts['post'+str(count)] = ele.p.text

pst = {'posts' : posts}
    

output.write(str(str(pst).encode('utf-8')))