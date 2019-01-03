num_cases = int(input())
for x in range(num_cases):
    length = int(input())
    count = 0
    arr = [int(n) for n in input().split()]
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                count += 1
    print(count)
