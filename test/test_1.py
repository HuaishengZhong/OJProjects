arr = []
try:
    while True:
        arr.append([int(n) for n in input().split()])
except EOFError:
    pass


for i in arr:
    print(i[0] + i[1])
