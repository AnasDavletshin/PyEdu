numbers = []
for c in input().split():
    numbers.append(int(c))

minimum_ind = numbers.index(min(numbers))
maximum_ind = numbers.index(max(numbers))
numbers[minimum_ind], numbers[maximum_ind] = (numbers[maximum_ind],
                                              numbers[minimum_ind])
print(*numbers)
