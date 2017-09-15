import urllib.request
import re

url = 'http://ob-zor.ru/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
req = urllib.request.Request('http://ob-zor.ru/', headers = {'User-Agent':user_agent})
with urllib.request.urlopen(req) as response:
    html = response.read().decode('utf-8')

regPostTitle = re.compile('<h2 class="block-title">.*?</h2>', flags = re.DOTALL)
titles = regPostTitle.findall(html)
new_titles = []
regTag = re.compile('<.*?>', re.DOTALL)
regSpace = re.compile('\s{2,}', re.DOTALL)
for t in titles:
    clean_t = regSpace.sub("", t)
    clean_t = regTag.sub("", t)
    new_titles.append(clean_t)

f = open('Titles.txt', 'w')
f.write(str(new_titles))
f.close()
