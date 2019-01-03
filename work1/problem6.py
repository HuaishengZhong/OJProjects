arr = [int(n) for n in input().split()]
summary = int(input())
result = 0
arr.sort()
behind = 0
ahead = len(arr) - 1
while ahead > behind:
    target = arr[behind] + arr[ahead]
    if summary == target:
        result += 1
        behind += 1
    elif target < summary:
        behind += 1
    else:
        ahead -= 1

print(result)
