n = int(input())

largest = 0
smallest = 9
while n != 0:
    last = n % 10
    if last > largest:
        largest = last
    if last < smallest:
        smallest = last
    n //= 10

print('Максимальная цифра равна', largest)
print('Минимальная цифра равна', smallest)
