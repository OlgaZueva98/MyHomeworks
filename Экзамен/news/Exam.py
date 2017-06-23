import re
import os


regexF = '_.*?\.xhtml'
regexW = '<w>.*?'

#1

def Count_words():
    listWordsCount = []
    file_tree = os.walk('.')
    for root, dirs, files in file_tree:
        for d in dirs:
            file_name = d.find(regexF)
            for f in files:
                f = open(file_name, 'r', encoding = 'utf-8')
                for r in f:
                    r = r[0:-1]
                    m = re.match(regexW, r)
                    if m != None:
                        listWords = r.split('<ana')
                        listWordsCount.append(len(listWords) - 1)
                 
def New_textfile():
    new_file = open('Количество слов.txt', 'w')
    new_file.write('{}\t{}\n'.format(new_file, str(sum(listWordsCount))))
    new_file.close()

def main():
    Count_words()
    New_textfile()
    
if __name__ == "__main__":
    main()

#2

f.seek(0)

regexInf = '<title>.*?'

Table = {}

file_tree = os.walk('.')
for root, dirs, files in file_tree:
    f = open(file_name, 'r', encoding = 'utf-8')
    for r in f:
        r = r[0:-1]
        m = re.match(regexInf, r)
        if m != None:
            s = m.group(0)
            title = s[6:len(s)-1]
            if title not in Table:
                Table[title] = 1
            else:
                Table[title] += 1

fileTable = open('Таблица.csv','w')
for key in sorted(Table.keys()):
##    fileTable.write('{}\t{} {}\t{}\n'.format(key, ), sep = '---')


    



