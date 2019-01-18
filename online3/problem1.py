from itertools import permutations


def check(p):
    numb = 0
    flag = 0
    for i in range(len(p)):
        if p[i] == 0 and flag == 0:
            continue
        else:
            numb = numb * 10 + p[i]
            flag = 1
    if numb % 17 == 0:
        return numb
    else:
        return 0


num_cases = int(input())
for i in range(num_cases):
    arr = [int(x) for x in input()]
    brr = []
    for p in permutations(arr):
        result = check(p)
        if result != 0:
            brr.append(result)
    print(brr)
    if brr:
        print(max(brr))
    else:
        print('Not Possible')
