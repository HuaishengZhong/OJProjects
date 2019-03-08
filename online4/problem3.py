"""
Description:
Let's define a Series Whose recurrence formula is as follows :
C(n)= 3C(i-1) + 4C(i-2) + 5C(i-3) + 6C(i-4)
C(0)= 2
C(1)= 0
C(2)= 1
C(3)= 7
Now based on this Series a Matrix Mi,j of size nn is to be formed.The top left cell is(1,1) and the bottom right corner
is (n,n). Each cell (i,j) of the Matrix contains either 1 or 0. If C( (i*j)^3 ) is odd, Mi,j is 1, otherwise, it's 0.
Count the total number of ones in the Matrix.


Input: First Line Of the input will contain an integer 'T'- the number of test cases . Each of the next 'T' lines
consists of an integer 'n'.-denoting the size of the matrix.
Constraints :
1 ≤ T ≤ 1000
1 ≤ n ≤ 1000
1
2

Output:
For each test case, output a single Integer -the taste value fo the dish of size-n*n.
0
"""


def calculate(x):
    if x < 4:
        l = [2, 0, 1, 7]
        return l[x]
    else:
        l = [0] * (x + 1)
        l[0] = 2
        l[2] = 1
        l[3] = 7
        for x in range(4, x + 1):
            l[x] = 3 * l[x - 1] + 4 * l[x - 2] + 5 * l[x - 3] + 6 * l[x - 4]
        return l[x]


def count_ones(n):
    count = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if calculate((i * j) ** 3) % 2 == 1:
                count += 1
    return count


case_num = int(input())
for i in range(case_num):
    n = int(input())
    print(count_ones(n))
