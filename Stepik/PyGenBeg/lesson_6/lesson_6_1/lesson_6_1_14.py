a = int(input())
n1 = a // 100
n2 = a // 10 % 10
n3 = a % 10

if 2 * max(n1, n2, n3) == n1 + n2 + n3:
    print('Число интересное')
else:
    print('Число неинтересное')
