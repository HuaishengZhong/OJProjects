arr = [int(n) for n in input().split()]
interval = [int(n) for n in input().split()]
low = interval[0] - 1
high = interval[1]
k = int(input())
result = arr[low:high]
result.sort()
print(result[k - 1])
