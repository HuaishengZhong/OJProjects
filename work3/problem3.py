def shell_sort(li, t):
    n = len(li)
    for gap in t:
        for i in range(gap, n):
            temp = li[i]
            j = i
            while j >= gap and li[j - gap] > temp:
                li[j] = li[j - gap]
                j -= gap
            li[j] = temp
    return li


num_cases = int(input())
for i in range(num_cases):
    arr = [int(x) for x in input().split()]
    brr = [int(x) for x in input().split()]
    print(" ".join(str(i) for i in shell_sort(arr, brr)))
