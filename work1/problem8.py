arr1 = [int(n) for n in input().split()]
arr2 = [int(n) for n in input().split()]

if sum(arr1) < sum(arr2):
    arr1, arr2 = arr2, arr1
a = sum(arr1) - sum(arr2)
min = a
tag = True
while tag:
    index1, index2 = 0, 0
    tag = False
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if min > a - 2 * (arr1[i] - arr2[j]) > 0:
                index1, index2 = i, j
                min = a - 2 * (arr1[i] - arr2[j])
    if min < a:
        arr1[index1], arr2[index2] = arr2[index2], arr1[index1]
        tag = True
        if sum(arr1) < sum(arr2):
            arr1, arr2 = arr2, arr1
        a = sum(arr1) - sum(arr2)
        min = a
    else:
        print(min)
