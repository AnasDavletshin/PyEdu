n = int(input())
n1 = n // 10 ** 3
n2 = n // 10 ** 2 % 10
n3 = n // 10 ** 1 % 10
n4 = n % 10

print(f'Цифра в позиции тысяч равна {n1}')
print(f'Цифра в позиции сотен равна {n2}')
print(f'Цифра в позиции десятков равна {n3}')
print(f'Цифра в позиции единиц равна {n4}')
