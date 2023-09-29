n = int(input())

for i in range(n):
    for j in range(i + 1):
        print(j + 1, end='')
    for j in range(i + 1, 2 * i + 1):
        print(2 * i + 1 - j, end='')
    print()
