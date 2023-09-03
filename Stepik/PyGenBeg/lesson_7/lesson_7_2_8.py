m = int(input())
n = int(input())

if m < n:
    r = range(m, n + 1)
else:
    r = range(m, n - 1, -1)

for i in r:
    print(i)
