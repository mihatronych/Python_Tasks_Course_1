ar = []
i = 0
while i < 4:
    ar.append(int(input()))
    i += 1
if ar[0] <= ar[1] <= 10:
    if ar[2] <= ar[3] <= 10:
        for k in range(ar[0] - 1, ar[1] + 1):
            for g in range(ar[2] - 1, ar[3] + 1):
                if k == ar[0] - 1 and g == ar[2] - 1:
                    print(" ", end="\t")
                    continue
                if k == ar[0] - 1:
                    print(g, end="\t")
                    continue
                if g == ar[2] - 1:
                    print(k, end="\t")
                    continue
                print(g * k, end="\t")
            print()


