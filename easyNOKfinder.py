a = int(input())
b = int(input())
A = a
B = b
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print(int(A * B / (a + b)))