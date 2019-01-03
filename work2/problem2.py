def distinguish(li):
    s = list(reversed(li))
    if li == s:
        return True
    else:
        return False


try:
    while True:
        arr = input().split()[1:]
        if distinguish(arr):
            print('true')
        else:
            print('false')
except EOFError:
    pass
