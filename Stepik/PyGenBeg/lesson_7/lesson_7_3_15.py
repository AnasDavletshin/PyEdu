n = int(input())

f1 = f2 = None
for i in range(n):
    if i == 0 or i == 1:
        f1 = 1
        f2 = 1
    else:
        f1, f2 = f2, f1 + f2
    print(f2, end=' ')
