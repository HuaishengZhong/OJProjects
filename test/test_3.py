arr = []
try:
    while True:
        str = input()
        if str == '0 0':
            break
        else:
            arr.append([int(n) for n in str.split()])
except EOFError:
    pass


for i in arr:
    print(i[0] + i[1])
