n = int(input())
n1 = n // 10 ** 2
n2 = n // 10 ** 1 % 10
n3 = n % 10

print(f'Сумма цифр = {n1 + n2 + n3}')
print(f'Произведение цифр = {n1 * n2 * n3}')
