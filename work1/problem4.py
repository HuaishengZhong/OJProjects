n = int(input())

'''
def process(num):
    if num == 1:
        return 2
    else:
        part1 = process(num - 1)
        part2 = 1
        part3 = process(num - 1)
        part4 = 1
        part5 = process(num - 1)
        return part1 + part2 + part3 + part4 + part5


print(process(n))
'''


def process(num):
    if num == 1:
        return 2
    else:
        return 3 * process(num - 1) + 2


print(process(n))
