numbers = []
for _ in range(int(input())):
    numbers.append(int(input()))

del numbers[1::2]

print(numbers)
