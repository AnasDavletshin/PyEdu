n = int(input())
s = input()

for ch in s:
    code = (ord(ch) - n)
    if code < 97:
        code += 26
    print(chr(code), end='')
