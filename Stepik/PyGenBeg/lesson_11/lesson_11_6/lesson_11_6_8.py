text = []
for _ in range(int(input()[1:])):
    line = input()
    if '#' in line:
        line = line[:line.find('#')]
    print(line.rstrip())
