"""
Description: Given arrival and departure times of all trains that reach a railway station. Your task is to find
the minimum number of platforms required for the railway station so that no train waits. Note: Consider that all the
trains arrive on the same day and leave on the same day. Also, arrival and departure times must not be same for a
train.


Input: The first line of input contains T, the number of test cases. For each test case, first line will contain an
integer N, the number of trains. Next two lines will consist of N space separated time intervals denoting arrival and
departure times respectively. Note: Time intervals are in the 24-hourformat(hhmm), preceding zeros are insignificant.
200 means 2:00. Consider the example for better understanding of input. Constraints:1 <= T <= 100，1 <= N <= 1000，1 <=
A[i] < D[i] <= 2359

1
6
900  940 950  1100 1500 1800
910 1200 1120 1130 1900 2000

Output:
For each test case, print the minimum number of platforms required for the trains to arrive and depart safely.

3
"""


def findPlatform(arr, dep, n):
    arr.sort()
    dep.sort()

    plat_needed = 1
    result = 1
    i = 1
    j = 0

    while i < n and j < n:
        if arr[i] < dep[j]:
            plat_needed += 1
            i += 1

            if plat_needed > result:
                result = plat_needed

        else:

            plat_needed -= 1
            j += 1

    return result


T = int(input())
for _ in range(T):
    n = int(input())
    arr = [int(x) for x in input().split()]
    dep = [int(x) for x in input().split()]
    print(findPlatform(arr, dep, n))
