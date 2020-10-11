s = ""
ar = []
with open('file.txt', 'r') as inf:
    for line in inf:
        line = line.strip()
        ar += line.split(' ')
print(ar)
newar = [a.lower() for a in ar]
settedar = set(newar)
print(settedar)
k = 0
s = ""
for el in settedar:
    if newar.count(el) > k:
        k = newar.count(el)
        s = el
    if newar.count(el) == k and el < s:
        s = el
print(s, k)