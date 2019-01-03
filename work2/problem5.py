def bubble_sort(li):
    for i in range(0, len(li) - 1, 1):
        for j in range(0, len(li) - i - 1, 1):
            if li[j] > li[j + 1]:
                tmp = li[j + 1]
                li[j + 1] = li[j]
                li[j] = tmp
    return li


try:
    while True:
        arr = [int(n) for n in input().split()][1:]
        print(" ".join(str(i) for i in bubble_sort(arr)))
except EOFError:
    pass
