s = ""
with open('file.txt', 'r') as inf:
    for line in inf:
        line = line.strip()
        for w in range(0, len(line), 1):
            if not line[w].isdigit():
                f = line[w]
                z = ""
                i = 1
                while w+i != len(line) and line[w + i].isdigit():
                    z = z + line[w + i]
                    i += 1
                s = s + line[w] * int(z)
        print(line)
print(s)
with open('newfile.txt', 'w') as inf:
    inf.write(s)