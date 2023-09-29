a = int(input())
b = int(input())

for n in range(max(2, a), b + 1):
    is_prime = True
    for m in range(2, int(n ** 0.5 + 1)):
        if n % m == 0:
            is_prime = False
            break
    if is_prime:
        print(n)
