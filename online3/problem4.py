from collections import Counter

num_cases = int(input())

for i in range(num_cases):
    n = int(input())
    firsts = Counter()
    lasts = Counter()
    doubles = Counter()

    for first, last in map(lambda x: (x[0], x[-1]), input().split()):
        if first == last:
            doubles[first] += 1
        else:
            firsts[first] += 1
            lasts[last] += 1

    if len(doubles) == 1 and len(firsts) == 0:
        print(1)
        continue
    if len(doubles) > 0 and len(firsts) == 0:
        print(0)
        continue

    cantDo = False
    for key in firsts.keys() | set(lasts.keys()) | set(doubles.keys()):
        if doubles[key] > 0:
            firsts[key] -= 1
            lasts[key] -= 1
        if firsts[key] < 0 or lasts[key] < 0 or firsts[key] != lasts[key]:
            cantDo = True
            break

    print(0 if cantDo else 1)
