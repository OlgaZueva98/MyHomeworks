f = open('F.txt', 'r', encoding = 'utf-8')
count_lines = 0
for r in f:
     lines = r.split('\n')
for l in lines:
    if '<teiHeader>' in f:
        break
    else:
        count_lines = count_lines + 1
f.close()

f_1 = open('Lines_Number.txt', 'a+', encoding = 'utf-8')
s = str(count_lines)
f_1.write(s)
f_1.close()

