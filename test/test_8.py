n = int(input())
arr = [[] for i in range(n)]

try:
    for i in range(n):
        arr[i] += [int(n) for n in input().split()]
except EOFError:
    pass

for i in arr:
    res = 0
    for n in i[1:]:
        res += n
    print(res)
    print()
