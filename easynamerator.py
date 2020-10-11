n = int(input())
if 0 <= n <= 1000:
    if n % 10 == 0:
        print(n, "программистов")
    elif n % 100 == 11 or n % 100 == 12 or n % 100 == 13 or n % 100 == 14 or n % 100 == 16 or n % 100 == 17 or n % 100 == 18 or n % 100 == 19:
        print(n, "программистов")
    elif n % 10 == 1:
        print(n, "программист")
    elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
        print(n, "программиста")
    elif n % 10 == 5 or n % 10 == 6 or n % 10 == 7 or n % 10 == 8 or n % 10 == 9:
        print(n, "программистов")