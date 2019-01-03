def insert_sort(li):
    lens = len(li)
    for i in range(1, lens):
        if li[i - 1] > li[i]:
            temp = li[i]
            index = i
            while index > 0 and li[index - 1] > temp:
                li[index] = li[index - 1]
                index -= 1
            li[index] = temp
    return li


try:
    while True:
        arr = [int(n) for n in input().split()][1:]
        print(" ".join(str(i) for i in insert_sort(arr)))
except EOFError:
    pass
