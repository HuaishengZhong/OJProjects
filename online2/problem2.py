def bin(magnets, left, right):
    limit = 0.0000000000001
    m = (left + right) / 2
    flag = 0
    for i in range(len(magnets)):
        flag += 1 / (m - magnets[i])
    if right-left < limit:
        return m
    if abs(flag) < limit:
        return m
    if flag > 0:
        return bin(magnets, m, right)
    elif flag < 0:
        return bin(magnets, left, m)


num_cases = int(input())
for i in range(num_cases):
    n = int(input())
    arr = [int(x) for x in input().split()]
    res = []
    for j in range(n - 1):
        r = bin(arr, arr[j], arr[j + 1])
        res.append(r)
    print(" ".join(str('%.2f' % k) for k in res))
