num_cases = int(input().strip())
for _ in range(num_cases):
    s = sorted(set(map(ord, input())))
    n = len(s)
    t, rl, rd = "", 1, 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            d, c = s[j] - s[i], s[j]
            while c in s:
                c += d
            l = (c - s[i]) // d
            if l > rl or (l == rl and d <= rd):
                rl, t, rd = l, c, d
    for i in range(rl):
        t -= rd
        print(chr(t), end="")
    print()
