s = input()
i = s.upper().count('g'.upper())
i += s.upper().count('c'.upper())
print(i / len(s) * 100)
