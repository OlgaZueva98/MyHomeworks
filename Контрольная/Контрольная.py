
import urllib.request

data = urllib.request.urlopen('http://web-corpora.net/Test1_2016/quotes.txt').read().decode('utf-8')
f = open('quotes.txt', 'r')

for line in f.readlines():
    if len(line.split()) < 10:
        print(line)
f.close() 

