num_cases = int(input())
n = int(input())
arrs = []
for i in range(0, num_cases):
    arrs.append(int(x) for x in input().split())

result = []

for arr in arrs:
    dic = {}
    for x in arr:
        if x not in dic.keys():
            dic[x] = 1
        else:
            dic[x] = dic[x] + 1

    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    result_list = []
    for key in dic:
        for i in range(0, key[1]):
            result_list.append(str(key[0]))
    result.append(result_list)
for r in result:
    print(' '.join(r))
