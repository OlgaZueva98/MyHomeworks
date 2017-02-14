import re

f = open('F.txt', 'r', encoding = 'utf-8')

dict_words = {}

f.seek(0)
text = f.read()
     
p = re.compile('(type=".+">)')
result = p.findall(text)

for key in result:
    key = key.lower()
    if key in dict_words:
        value = dict_words[key]
        dict_words[key] = value + 1
    else:
        dict_words[key] = 1

sorted_keys = sorted(dict_words)

f_2 = open('Dict.csv', 'a+', encoding ='utf-8')
for key in sorted_keys:
    S = str(key) + ';' + str(dict_words[key]) + '\n'
    f_2.write(S)

f_2.close()














    
