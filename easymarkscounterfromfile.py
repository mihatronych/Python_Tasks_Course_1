ar = []
with open('file.txt', 'r', encoding='utf-8') as inf:
    for line in inf:
        ar.append(line.strip().split(';'))
print(ar)
s = ""
first = 0.0
second = 0.0
third = 0.0
for el in ar:
    s += str((float(el[3]) + float(el[1]) + float(el[2])) / 3) + '\n'
    first += float(el[1])
    second += float(el[2])
    third += float(el[3])
extra_s = str(first / len(ar))+ " " + str(second / len(ar)) + " " + str(third / len(ar))
print(s + extra_s)
with open('newfile.txt', 'w', encoding='utf-8') as inf:
    inf.write(s + extra_s)
