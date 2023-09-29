n = int(input())

last_digit = n % 10
n //= 10
while n != 0:
    if n % 10 != last_digit:
        break
    n //= 10

if n == 0:
    print('YES')
else:
    print('NO')
