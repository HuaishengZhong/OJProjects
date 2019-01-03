arr = []
try:
    while True:
        arr.append([int(n) for n in input().split()])
except EOFError:
    pass


for i in arr:
    if len(i) == 2:
        print(i[0] + i[1])
        print()
    else:
        pass
