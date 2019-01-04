import sys

num_cases = int(input())
for i in range(num_cases):
    P = int(input())
    result = 0
    for j in range(1, sys.maxsize):
        result += j * j
        if P < result:
            print(j - 1)
            break
