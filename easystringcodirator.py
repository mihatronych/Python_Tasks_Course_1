s = input()
new_s = ""
length = len(s)
i = 1
c = 0
while c < length:
    i = 1
    for k in range(c + 1, len(s)):
        if s[c] == s[k]:
            i += 1
        else:
            break
    new_s += s[c] + str(i)
    c += i
print(new_s)
