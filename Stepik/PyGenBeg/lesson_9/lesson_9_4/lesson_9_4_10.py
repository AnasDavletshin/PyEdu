n = int(input())

total = 0
for _ in range(n):
    if input().count('11') > 2:
        total += 1
print(total)
