def quick_sort(arr):
    if len(arr) < 2:
        return arr
    stack = []
    stack.append(len(arr) - 1)
    stack.append(0)
    while stack:
        l = stack.pop()
        r = stack.pop()
        index = partition(arr, l, r)
        if l < index - 1:
            stack.append(index - 1)
            stack.append(l)
        if r > index + 1:
            stack.append(r)
            stack.append(index + 1)
    return arr


def partition(arr, start, end):
    # 分区操作，返回基准线下标
    pivot = arr[start]
    while start < end:
        while start < end and arr[end] >= pivot:
            end -= 1
        arr[start] = arr[end]
        while start < end and arr[start] <= pivot:
            start += 1
        arr[end] = arr[start]
    # 此时start = end
    arr[start] = pivot
    return start


try:
    while True:
        li = [int(n) for n in input().split()][1:]
        print(" ".join(str(i) for i in quick_sort(li)))
except EOFError:
    pass
