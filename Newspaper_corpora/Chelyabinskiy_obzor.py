import urllib.request
import re
import os
import time

directory_output = 'D:' + os.sep + 'Chelyabinskiy obzor'

def download_sources(commonUrl, articleLink):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    req = urllib.request.Request(commonUrl, headers = {'User-Agent':user_agent})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')

    new_sources = []

    regex = '[^(<!--)]<li[^(nk)].* href="/[\w\s]*[^(png)]" '
    if articleLink != '':
        regex = '<div class="title-head"><a href="' + articleLink + '/.+[^(\.png)(\.jpg)(\.css)]"'  

    regPostSource = re.compile(regex)
            
    sources = regPostSource.findall(html)
        
    for idx, s in enumerate(sources):
        i = s.find('href="')
        if articleLink != '':
            sources[idx] = commonUrl + s[i + len(articleLink) + 7:len(s) - 1]
        else:
            sources[idx] = commonUrl + s[i + 7:len(s) - 2]
        
        try:
            page_url = urllib.request.urlopen(sources[idx])
            html = page_url.read().decode('utf-8')

            if sources[idx] not in new_sources:
                new_sources.append(sources[idx])
            
        except:
            print('Error at', sources[idx])

    return new_sources


def download_page(linkUrl):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    req = urllib.request.Request(linkUrl, headers = {'User-Agent':user_agent})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    return(html)


        
def clean_page(html):
    regTag = re.compile('<.*?>', flags = re.DOTALL)
    regScript = re.compile('<script[.*]?>.*?</script>', flags = re.DOTALL)
    regComment = re.compile('<!--.*?-->', flags = re.DOTALL)
    regSpace = re.compile('\s', flags = re.DOTALL)

    page = regScript.sub('', html)
    page = regComment.sub('', page)
    page = regTag.sub('', page)
    
    return page 
    


def download_date(html):
    monthes = {'января': 1, 'февраля': 2, 'марта': 3 , 'апреля': 4,
               'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,
               'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}
   
    regex = re.compile('itemprop="datePublished">.+</time>', flags = re.DOTALL)
    
    time_of_publ = re.search(regex, html)
    
    if time_of_publ:
        tSplit = time_of_publ.group(0).split(' ')
        date_num = tSplit[0][len('itemprop="datePublished">'):]
        month = tSplit[1]
        year = tSplit[2][:4]
  
        for m in monthes:
            if month == m:
                month = str(monthes[m])
  
    else:
        date_num = 'MissingDate'
        month = 'MissingMonth'
        year = 'MissingYear'

    return(date_num, month, year)


def download_author(html):
    regex = re.compile('<meta property="article:author" content=".+" />', flags = re.DOTALL)
    author_name = re.search(regex, html)
    
    if author_name:
        author = author_name.group(0)[len('<meta property="article:author" content="'):]
        i = author.find('"')
        author = author[:i]
    else:
        author = 'MissingAuthor'

    return(author)


def download_header(html):
    
    regex = re.compile('<meta property="og:title" content=".+" />', flags = re.DOTALL)
    head = re.search(regex, html)
    
    if head:
        header = head.group(0)[len('<meta property="og:title" content="'):]
        i = header.find('"')
        header = header[:i]
    else:
        header = 'MissingHeader'

    return(header)


def download_topic(html):
    regex = re.compile('<meta property="article:section" content=".+" />')
    top = re.search(regex, html)
    if top:
        topic = top.group(0)[len('<meta property="article:section" content="'):]
        i = topic.find('"')
        topic = topic[:i]
    else:
        topic = 'MissingTopic'

    print('*', end=' ')
    return(topic)
    

def metadata(path, author, header, created, topic, source, page):
    header = header.replace('?','').replace('/','')
    
    create_folders(path, author, header, created, topic, source, page)

    row = '%s\t%s\t\t\t%s\tпублицистика\t\t\t\tнейтральный\tн-возраст\tн-уровень\tгородская\t%s\tЧелябинский обзор\t\t%s\tгазета\tРоссия\tЧелябинская область\tru'
    path = path + os.sep + header + '.txt'
    file = open(directory_output + os.sep + 'metadata.csv', 'a', encoding = 'utf-8')
    file.write(row % (path, author, created, topic, source))
    file.close()

def create_folders(path, author, header, created, topic, source, page):
    row = '@au %s\n@da %s\n@topic %s\n@url %s\n%s'
    if not os.path.exists(path):
        os.makedirs(path)
    
    file2 = open(path + os.sep + header + '.txt', 'w', encoding = 'utf-8')
    file2.write(row % (author, created, topic, source, page))
    file2.close()


def mystem_xml(): 
    for root, dirs, files in os.walk(directory_output + os.sep + 'plain'): 
        for f in files: 
            pathway = root.replace('plain', 'mystem-xml') 
            if not os.path.exists(pathway): 
                os.makedirs(pathway) 
            inp = root + os.sep + f 
            outp = inp.replace('plain', 'mystem-xml').replace('.txt', '.xml')
            os.system(r'D:\mystem.exe -ncid —format xml ' + inp + ' ' + outp)                     

def mystem_txt():
    for root, dirs, files in os.walk(directory_output + os.sep + 'plain'):
        for f in files:
            pathway = root.replace('plain', 'mystem-plain')
            if not os.path.exists(pathway):
                os.makedirs(pathway)
            inp = root + os.sep + f
            outp = inp.replace('plain', 'mystem-plain')
            os.system(r'D:\mystem.exe -ncid ' + inp + ' ' + outp)

def main():
    if not os.path.exists(directory_output):
        os.makedirs(directory_output)
        
    source = download_sources('http://ob-zor.ru/', '')
    for s in source:

        sourceArticleUrl = download_sources(s + '/', s[len('http://ob-zor.ru/')-1:])
        for articleUrl in sourceArticleUrl:
            
            html = download_page(articleUrl)

            created = download_date(html)
            author = download_author(html)
            topic = download_topic(html)
            header = download_header(html)
        
            page = clean_page(html)
            
            path = directory_output + os.sep + 'plain' + os.sep + created[2] + os.sep + created[1]
            metadata(path, author, header, created, topic, articleUrl, page)
            time.sleep(2)
    mystem_xml()
    mystem_txt()

if __name__ == '__main__':
    main()
