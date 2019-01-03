arr = []
try:
    while True:
        input_str = input()
        if input_str[0:1] == '0':
            continue
        else:
            arr.append([int(n) for n in input_str.split()])
except EOFError:
    pass


for i in arr:
    res = 0
    for n in i[1:]:
        res += n
    print(res)
