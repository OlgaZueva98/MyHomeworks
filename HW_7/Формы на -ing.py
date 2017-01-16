#Программа с помощью отдельной функции принимает от пользователя название файла с английским текстом,
#читает этот файл и сообщает: 
#1. сколько в тексте форм на -ing (слова типа during и ring можно тоже считать) и
#сколько раз в тексте встречается форма на -ing, введенная пользователем.
#Весь код должен быть в функциях.
#Например, чтение файла — одна функция,
#поиск нужных слов — другая функция,
#подсчет частотности слова, которое ввел пользователь — третья функция, и т.д.
#Тестировать можно, например, на "Гордости и предубеждении"

def replace_marks(ch):
    marks = [',','.','!','?',';',':','-','*','"','(',')','\'','`','\n','\f','\r','\t','\v']
    for i in marks:
        if ch.find(i) > 0:
            ch = ch.replace(i,'') #убираем посторонние символы
    return ch

def search_ing(f):
    count_ing = 0
    for r in f:
        list_word = r.split(' ') #список слов в строке
        for w in list_word:
            w = replace_marks(w)
            if w.endswith('ing'): 
                count_ing = count_ing + 1
    print('Форм на -ing: ' + str(count_ing))     

def search_ing_user(f):
    wordUser = input('Введите слово на -ing: ')
    count_wordUser = 0
    for r in f:
        list_word = r.split(' ') #список слов в строке
        for w in list_word:
            w = replace_marks(w)
            if w.upper() == wordUser.upper(): 
                count_wordUser = count_wordUser + 1
    print('Слово пользователя: ' + str(count_wordUser))     

def close_file(f):
    f.close()
    
def read_file():
    filename = input('Введите имя файла: ')
    file = open(filename, 'r', encoding = 'utf-8')
    return file
    
def begin_program():
    fileSource = read_file()
    search_ing_user(fileSource)
    fileSource.seek(0) #переход к началу открытого файла
    search_ing(fileSource)
    close_file(fileSource)
    
#основной код
begin_program()
