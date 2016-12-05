fileName = input('Введите имя файла: ')
f = open(fileName, 'r', encoding = 'utf-8')
l_count = [] 
for r in f:
    l_row = r.split(' ')
    l_count.append(len(l_row))

print('Среднее количество слов в строке = ' + str(sum(l_count) / len(l_count)))
f.close()
