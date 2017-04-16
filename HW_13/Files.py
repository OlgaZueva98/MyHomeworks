import os

list_f = os.listdir('.') 
    
list_f_without_repetition = []
for f in list_f:
    for c in f: #проверяем символы в названии файлов
        if c.isdigit():
            count_f += 1
            break

    partition_f = f.partition('.')[0] #Возвращает кортеж, содержащий часть перед шаблоном, сам шаблон и часть после шаблона
    if (partition_f in list_f_without_repetition) == 0: #проверка наличия элемента в списке
        list_f_without_repetition.append(partition_f)
        
print('Количество файлов и папок, в названии которых содержатся цифры: ' + str(count_f))

n = 0
for s in list_f_without_repetition:
    n += 1
    print('{}: {}'.format(n,s)) #вывести на экран названия всех файлов без повторов
