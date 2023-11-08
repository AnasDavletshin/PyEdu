n = int(input())

strings = []
for _ in range(n):
    strings.append(input())

string = input().lower()

for s in strings:
    if string in s.lower():
        print(s)
