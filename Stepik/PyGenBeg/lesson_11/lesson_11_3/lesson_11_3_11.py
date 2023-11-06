n = int(input())
sums = []
a0 = int(input())
for i in range(n - 1):
    a1 = int(input())
    sums.append(a0 + a1)
    a0 = a1

print(sums)
