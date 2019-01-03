input_arr = input()
arr = [int(n) for n in input_arr.split()]
num = int(input())
count = 0

for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        temp = arr[i:j + 1]
        if max(temp) - min(temp) > num:
            count += len(arr) - j
            break

print(count)
