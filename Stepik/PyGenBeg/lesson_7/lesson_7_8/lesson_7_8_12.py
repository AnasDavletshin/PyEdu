# 10 n + 5 k + 0.5 m = 100
for n in range(1, 10):
    for k in range(1, 20):
        for m in range(1, 200):
            if 10 * n + 5 * k + 0.5 * m == 100 and n + k + m == 100:
                print(n, k, m)
