def count_sort(a):
    k = max(a)
    n = len(a)
    b = [0 for i in range(n)]
    c = [0 for i in range(k + 1)]
    for j in a:
        c[j] = c[j] + 1
    for i in range(1, len(c)):
        c[i] = c[i] + c[i - 1]
    for j in a:
        b[c[j] - 1] = j
        c[j] = c[j] - 1
    return b


try:
    while True:
        arr = [int(n) for n in input().split()][1:]
        print(" ".join(str(i) for i in count_sort(arr)))
except EOFError:
    pass
