input_arr = input()
arr = [int(n) for n in input_arr.split()]
w = int(input())
result = 0
queue = []

for i in range(len(arr)):
    if queue:
        if i >= queue[0] + w:
            queue.pop(0)

        while len(queue) != 0 and arr[i] >= arr[queue[-1]]:
            queue.pop()

    queue.append(i)

    if i + 1 >= w:
        result += arr[queue[0]]


print(result)
