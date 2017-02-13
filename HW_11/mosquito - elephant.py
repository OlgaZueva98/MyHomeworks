import re

def dashrepl(obj):
    text = obj.group(0)
    
    bTitle = False
    if text.istitle() == True:
        bTitle = True

    text = text.lower()
    text = text.partition('комар') #Возвращает кортеж, содержащий часть перед первым шаблоном, сам шаблон, и часть после шаблона. Если шаблон не найден, возвращается кортеж, содержащий саму строку, а затем две пустых строки

    result = 'слон'+text[2]

    if bTitle == True:
        result = result.capitalize()

    return result

source_data = open('Комар обыкновенный — Википедия.html', 'r', encoding = 'utf-8').read()
output_file = open('Слон обыкновенный - Википедия.html', 'w', encoding = 'utf-8')

regex = '[К|к]омар([^и]|[а|ы|у|ов])'
output_file.write(re.sub(regex, dashrepl, source_data))
output_file.close()
