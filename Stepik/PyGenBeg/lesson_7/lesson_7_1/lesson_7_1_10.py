m = int(input())
p = 1 + 0.01 * int(input())
n = int(input())

for i in range(n):
    print(i + 1, m)
    m = m * p
