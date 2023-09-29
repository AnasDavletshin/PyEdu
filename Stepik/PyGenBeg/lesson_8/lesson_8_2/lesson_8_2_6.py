n = int(input())

count_three = 0
n_last_digit = n % 10
count_n_last_digit = 0
count_even_digit = 0
total_sum = 0
total_pr = 1
count_zero_or_five = 0
while n > 0:
    last_digit = n % 10
    if last_digit == 3:
        count_three += 1
    if last_digit == n_last_digit:
        count_n_last_digit += 1
    if last_digit % 2 == 0:
        count_even_digit += 1
    if last_digit > 5:
        total_sum += last_digit
    if last_digit > 7:
        total_pr *= last_digit
    if last_digit in (0, 5):
        count_zero_or_five += 1
    n //= 10

print(count_three)
print(count_n_last_digit)
print(count_even_digit)
print(total_sum)
print(total_pr)
print(count_zero_or_five)
