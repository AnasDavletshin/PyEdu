n = int(input())

for m in range(1, n + 1):
    count = 0
    for d in range(1, m + 1):
        if m % d == 0:
            count += 1
    print(m, '+' * count, sep='')
