"""
Description:
There are two parallel roads, each containing N and M buckets, respectively. Each bucket may contain some balls.
The buckets on both roads are kept in such a way that they are sorted according to the number of balls in
them. Geek starts from the end of the road which has the bucket with a lower number of balls(i.e. if buckets are
sorted in increasing order, then geek will start from the left side of the road). The geek can change the road only
at the point of intersection(which means, buckets with the same number of balls on two roads). Now you need to help
Geek to collect the maximum number of balls.

Input:
The first line of input contains T denoting the number of test cases. The first line of each test case contains two
integers N and M, denoting the number of buckets on road1 and road2 respectively. 2nd line of each test case contains N
integers, number of balls in buckets on the first road. 3rd line of each test case contains M integers, number of balls
in buckets on the second road.
Constraints:1<= T <= 1000，1<= N <= 10^3，1<= M <=10^3，0<= A[i],B[i]<=10^6

1
5 5
1 4 5 6 8
2 3 4 6 9

Output:
For each test case output a single line containing the maximum possible balls that Geek can collect.

29
"""

T = int(input())
for _ in range(T):
    [n, m] = list(map(int, input().split()))
    r1 = list(map(int, input().split()))
    r2 = list(map(int, input().split()))
    common = []
    i, j, s = 0, 0, 0
    while i < n and j < m:
        if r1[i] < r2[j]:
            i += 1
        elif r1[i] > r2[j]:
            j += 1
        else:
            common.append(r1[i])
            i += 1
            j += 1
    i, j = 0, 0
    for x in common:
        a, b = 0, 0
        while i < n:
            a += r1[i]
            i += 1
            if i == n or x < r1[i]:
                break
        while j < m:
            b += r2[j]
            j += 1
            if j == m or x < r2[j]:
                break
        s += max(a, b)
    a = sum(r1[i:])
    b = sum(r2[j:])
    s += max(a, b)
    print(s)
