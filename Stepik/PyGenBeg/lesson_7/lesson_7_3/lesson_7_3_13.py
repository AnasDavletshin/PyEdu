n = int(input())

largest1 = 0
largest2 = 0
for _ in range(n):
    x = int(input())
    if x > largest1:
        largest2 = largest1
        largest1 = x
    elif x > largest2:
        largest2 = x

print(largest1, largest2, sep='\n')
