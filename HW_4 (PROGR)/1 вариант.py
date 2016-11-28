word = input('Введите слово: ')
n = -1
for i in word:
    if abs(n) != len(word):
        i = word[:n] 
        print(i) 
        n = n - 1
 
