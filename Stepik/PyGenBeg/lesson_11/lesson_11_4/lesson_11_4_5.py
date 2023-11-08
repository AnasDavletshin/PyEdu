n = int(input())

strings = []
for _ in range(n):
    s = input()
    if s not in strings:
        strings.append(s)

print(*strings, sep='\n')
