n = int(input())

prev_digit = n % 10
n //= 10
while n != 0:
    cur_digit = n % 10
    if cur_digit < prev_digit:
        break
    prev_digit = cur_digit
    n //= 10

if n == 0:
    print('YES')
else:
    print('NO')
