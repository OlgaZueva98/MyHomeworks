#Программа должна открывать файл с русским текстом в кодировке UTF-8 и
#распечатывать из него по одному разу все встретившиеся в нём
#(в зависимости от варианта): 
#1. формы глагола "открыть"
#В формы глагола включаются деепричастия, причастия и формы на -ся и
#не включаются видовые пары (тем более что не у всех из перечисленных глаголов они имеются).
#И особое внимание стоит уделить тому, чтобы программа ничего, кроме форм этих глаголов, не распознавала. 
#Решить задание следует с помощью применения регулярных выражений.

#открыть, открою, откроем, откроешь, откроете, откроет, откроют, откроя, открыл, открыла, открыло, открыли, 
#открой, откройте, открывший, открывшая, открывшее, открывшие, открывшего, открывшей, 
#открывших, открывшему, открывшим, открывшую, открывшею, открывшими, 
#открывшем, открытый, открытая, открытое, открытые, открытого, 
#открытой, открытых, открытому, открытым, открытую, открытою, открытыми, 
#открытом, открыт, открыта, открыто, открыты

#суффиксы не используются -ыва-, -ива-, -ва-, -а-, -я-

#Оператор	Описание
#   .	        Один любой символ, кроме новой строки \n.
#   ?	        0 или 1 вхождение шаблона слева
#   +	        1 и более вхождений шаблона слева
#   *	        0 и более вхождений шаблона слева
#   \w	        Любая цифра или буква (\W — все, кроме буквы или цифры)
#   \d	        Любая цифра [0-9] (\D — все, кроме цифры)
#   \s	        Любой пробельный символ (\S — любой непробельнй символ)
#   \b	        Граница слова
#   [..]	Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)
#   \	        Экранирование специальных символов (\. означает точку или \+ — знак «плюс»)
#   ^ и $	Начало и конец строки соответственно
#   {n,m}	От n до m вхождений ({,m} — от 0 до m)
#   a|b	        Соответствует a или b
#   ()	        Группирует выражение и возвращает найденный текст
#   \t, \n, \r	Символ табуляции, новой строки и возврата каретки соответственно

import re

regex = u'откр(о|ы)(((т[^к])|(т$))|(в[^а]ш?)|й|л|е|ю|я)' 

fileName = input('Введите имя файла, в котором необходимо найти все формы глагола \'открыть\': ')
f = open(fileName, 'r', encoding = 'utf-8')

list_open = [] #список найденных форм глагола открыть

for r in f:
    r = r.lower()
    list_word = r.split(' ')
    for w in list_word:
        w = w.strip('.,:;-()?!%*\'\"\n\r\t\f\v')
        m = re.match(regex, w) #ищет по заданному шаблону в начале строки
        if m != None:
            if (w in list_open) == 0: #проверка наличия элемента в списки (1 - значение найдено, 0 - в списке такого значения нет)
                list_open.append(w)

f.close()
print('Формы глагола \'открыть\':')
c = 0 #количество найденных слов
for i in list_open:
    print(i)
    c = c + 1
print('Итого: ' + str(c))
