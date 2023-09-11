n = int(input())

digit_sum = 0
digit_count = 0
digit_product = 1
last_digit = n % 10
cur_digit = 0
while n != 0:
    cur_digit = n % 10
    digit_sum += cur_digit
    digit_count += 1
    digit_product *= cur_digit
    n //= 10

print(
    digit_sum, digit_count, digit_product, digit_sum / digit_count,
    cur_digit, cur_digit + last_digit, sep='\n'
)
