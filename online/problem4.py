num_cases = int(input())
for x in range(num_cases):
    n_length = [int(n) for n in input().split()]
    arr1 = [int(n) for n in input().split()]
    arr2 = [int(n) for n in input().split()]
    brr1 = []
    brr2 = []
    flag = True
    for i in arr2:
        for j in arr1:
            if j == i:
                brr1.append(j)
            else:
                if j not in arr2 and flag:
                    brr2.append(j)

        flag = False

    temp = brr1 + sorted(brr2)

    print(" ".join(str(i) for i in temp))
