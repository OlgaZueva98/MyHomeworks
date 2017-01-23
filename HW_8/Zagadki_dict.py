#Написать программу, которая загадывает слова.
#Загадав существительное, программа показывает подсказку
#в виде распространённого словосочетания с этим существительным,
#в котором существительное заменено многоточием,
#и ждёт ответа пользователя, после чего сообщает, выиграл он или проиграл.
#Например, если загадано слово "снег", можно показать подсказку "белый ...".
#Словосочетание можно подсмотреть в корпусе: http://ruscorpora.ru/beta/search-ngrams_2.html или довериться интуиции. 
#В задании обязательно использовать словарь.
#Программа должна уметь загадывать как минимум 5 разных слов (с разными подсказками).
#Кроме того, желательно, чтобы слова и подсказки хранились в отдельном csv-файле,
#который загружался бы при запуске программы. 
#Пользователю даётся столько попыток угадать слово, сколько букв в слове.

#С csv-файлами можно работать так же, как и с обычными файлами.
#Если данные в вашем файле разделены при помощи запятых, то: 
#1. открываете файл 
#2. читаете его по строкам 
#3. каждую строку делите по запятым при помощи .split(',') 
#4. получаете массив с данными, содержащимися в конкретной строке. 
#5. делаете с ними что хотите

dict_riddle = {} #словарь загадок

def read_file():
    f = open("Загадки_задания_отгадки_dict.csv", 'r')
    for r in f:
        r = r[0:-1] #убираем символ конца строки
        list_word = r.split(';') #загадка, отгадка
        dict_riddle[list_word[0]] = list_word[1] # добавляем новый элемент словаря
    f.close()


#основной код
read_file()

for n in range(5):
    selected_riddle_key, selected_riddle_value = dict_riddle.popitem() #случайный выбор загадки

    print('Угадай ' + str(n + 1) + '-е слово: ' + selected_riddle_key)
    count_letters = len(selected_riddle_value) 
    for i in range(count_letters):
        strAgain = 'Попробуйте еще раз: '
        if i == count_letters - 1:
            strAgain = ''
        
        user_word = input('Ваш ответ: ')
    
        if user_word.upper() == selected_riddle_value.upper():
            print('Вы угадали!')
            break
        else:
            print('Неверно. ' + strAgain)
    else:
        print('Вам не удалось отгадать. Загаданное слово: ' + selected_riddle_value)
        
