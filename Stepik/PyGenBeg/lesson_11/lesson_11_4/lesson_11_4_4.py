n = int(input())

numbers = []
for i in range(n):
    numbers.append(int(input()))

max_number = max(numbers)
min_number = min(numbers)
for i in range(len(numbers)):
    if numbers[i] == min_number:
        del numbers[i]
        break
for i in range(len(numbers)):
    if numbers[i] == max_number:
        del numbers[i]
        break

print(*numbers, sep='\n')
