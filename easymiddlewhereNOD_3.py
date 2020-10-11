a = int(input())
b = int(input())
i = 0
s = 0
while a % 3 !=0:
    a += 1
if a <= b:
    for k in range(a, b + 1, 3):
        s += k
        i += 1
    print(s/i)
