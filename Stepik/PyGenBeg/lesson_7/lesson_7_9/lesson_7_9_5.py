n = int(input())

while n // 10 > 0:
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    n = total

print(n)
