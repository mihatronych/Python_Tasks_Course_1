def countRectangle():
    a = float(input())
    if a > 0:
        b = float(input())
        if b > 0:
            print(a * b)

def countTriangle():
    a = float(input())
    if a > 0:
        b = float(input())
        if b > 0:
            c = float(input())
            if c > 0:
                p = (a + b + c) / 2
                print((p * (p - a) * (p - b) * (p - c)) ** (1 / 2))

def conutRing():
    r = float(input())
    if r > 0:
        print(3.14 * r ** 2)

name = input()
if name == "прямоугольник":
    countRectangle()
elif name == "треугольник":
    countTriangle()
elif name == 'круг':
    conutRing()