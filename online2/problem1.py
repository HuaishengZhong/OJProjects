import sys


def ispossible(arr, n, m, curr_min):
    studentsRequired = 1
    curr_sum = 0

    for i in range(n):
        if arr[i] > curr_min:
            return False
        if curr_sum + arr[i] > curr_min:
            studentsRequired += 1
            curr_sum = arr[i]
            if studentsRequired > m:
                return False
        else:
            curr_sum += arr[i]

    return True


def findpages(arr, n, m):
    sum = 0

    if n < m:
        return -1

    for i in range(n):
        sum += arr[i]

    start = 0
    end = int(sum)
    result = sys.maxsize

    while start <= end:
        mid = (start + end) // 2
        if ispossible(arr, n, m, mid):
            result = min(result, mid)
            end = mid - 1

        else:
            start = mid + 1

    return result


num_cases = int(input())
for i in range(0, num_cases):
    n = int(input())
    arr = [int(x) for x in input().split()]
    m = int(input())
    print(findpages(arr, n, m))
