"""
Description: Given the list of coins of distinct denominations and total amount of money. Output the minimum
number of coins required to make up that amount. Output -1 if that money cannot be made up using given coins. You may
assume that there are infinite numbers of coins of each type.


Input: The first line contains 'T' denoting the number of test cases. Then follows description of test cases. Each
cases begins with the two space separated integers 'n' and 'amount' denoting the total number of distinct coins and
total amount of money respectively. The second line contains N space-separated integers A1, A2, ..., AN denoting the
values of coins. Constraints:1<=T<=30，1<=n<=100，1<=Ai<=1000，1<=amount<=10000

Output: Print the minimum number of coins required to make up that amount or return -1 if it is impossible to make
that amount using given coins.
"""

import sys


def minCoin(coins, money):
    changes = [sys.maxsize] * (money + 1)
    for coin in coins:
        changes[coin] = 1

    for i in range(1, money + 1):
        for coin in coins:
            if i - coin > 0:
                changes[i] = min(changes[i], changes[i - coin] + 1)

    return -1 if changes[money] == sys.maxsize else changes[money]


T = int(input().strip())
for _ in range(T):
    n, money = [int(num) for num in input().strip().split(' ')]
    coins = {int(num): n for num in input().strip().split(' ')}
    print(minCoin(coins, money))
