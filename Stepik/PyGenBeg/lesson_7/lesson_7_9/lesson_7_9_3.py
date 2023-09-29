# 10: 1 + 2 + 5 + 10 = 18

a = int(input())
b = int(input())

max_total = 0
max_total_num = 0
for n in range(a, b + 1):
    total = 0
    for m in range(1, n + 1):
        if n % m == 0:
            total += m
    if total >= max_total:
        max_total = total
        max_total_num = n

print(max_total_num, max_total)
