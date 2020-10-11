a = 0
big_string = ""
while True:
    a = int(input())
    if a < 10:
        continue
    elif a > 100:
        break
    big_string += str(a) + "\n"
print(big_string)
