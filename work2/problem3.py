def reverse(li):
    n = int(li[0])
    x = int(li[-1])
    brr = li[1:-1]
    for i in range(1, n // x + 1):
        brr[x * (i - 1):x * i] = list(reversed(brr[x * (i - 1):x * i]))
    return brr


try:
    while True:
        arr = input().split()
        print(" ".join(str(i) for i in reverse(arr)))
except EOFError:
    pass
