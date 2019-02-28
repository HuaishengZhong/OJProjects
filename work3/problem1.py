"""
Description
对给定的n个任务与n个人之间的成本矩阵完成成本最低的任务分配策略。


Input
输入：第一行为用例个数，之后为每一个用例；
用例的第一行为任务个数，即n；
用例的第二行为使用逗号隔开的人员完成任务的成本；
每一个成本描述包括人员序号、任务序号和成本，使用空格隔开。
人员序号和任务序号都是从1到n的整数，序号出现的次序没有固定规则。
1
4
2 1 6,1 2 2,1 3 7,1 4 8,1 1 9,2 2 4,2 3 3,2 4 7,3 1 5,3 2 8,3 3 1,3 4 8,4 1 7,4 2 6,4 3 9,4 4 4

Output
输出：每一个用例输出一行，从序号为1的人员开始，给出其分配的任务序号，
使用空格隔开；使用逗号将多个解隔开。结果按照人员分配的任务序号大小排，
第一个人员的任务序号大的放在前面，如果相同则看第二个人员的任务，以此类推。
2 1 3 4
"""


from scipy.optimize import linear_sum_assignment
import numpy as np

# 2 1 6,1 2 2,1 3 7,1 4 8,1 1 9,2 2 4,2 3 3,2 4 7,3 1 5,3 2 8,3 3 1,3 4 8,4 1 7,4 2 6,4 3 9,4 4 4
num_cases = int(input())
for i in range(num_cases):
    n = int(input())
    cost = np.zeros(shape=(n, n), dtype=int)
    s = input().split(',')
    for li in s:
        x = int(li[0])
        y = int(li[2])
        data = int(li[4])
        cost[x - 1][y - 1] = data
    row_ind, col_ind = linear_sum_assignment(cost)
    print(" ".join(str(i + 1) for i in col_ind))
