n = int(input())
n1 = n // 10 ** 2
n2 = n // 10 ** 1 % 10
n3 = n % 10

print(100 * n1 + 10 * n2 + n3)
print(100 * n1 + 10 * n3 + n2)
print(100 * n2 + 10 * n1 + n3)
print(100 * n2 + 10 * n3 + n1)
print(100 * n3 + 10 * n1 + n2)
print(100 * n3 + 10 * n2 + n1)
