arr = [int(n) for n in input().split()]


def maxseqRemoveNum(array):
    b = [1] * len(array)
    prevb = [-1] * len(array)

    for i in range(1, len(array)):
        for j in range(0, i):
            if array[j] < array[i] and b[i] < b[j] + 1:
                b[i] = b[j] + 1
                prevb[i] = j

    c = [1] * len(array)
    prevc = [-1] * len(array)
    for i in range(len(array) - 2, -1, -1):
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[i] and c[i] < c[j] + 1:
                c[i] = c[j] + 1
                prevc[i] = j

    maxv = 0
    point = 0
    for i in range(len(array)):
        if b[i] + c[i] > maxv:
            maxv = b[i] + c[i]
            point = i

    result = []
    ppoint = point

    while (prevb[point] != -1):
        result.append(array[point])
        point = prevb[point]
    result.append(array[point])
    result.reverse()
    result.remove(array[ppoint])

    while prevc[ppoint] != -1:
        result.append(array[ppoint])
        ppoint = prevc[ppoint]
    result.append(array[ppoint])
    return result


temp = maxseqRemoveNum(arr)
for i in temp:
    print(i, end=' ')
