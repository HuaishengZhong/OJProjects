"""
Description:
Mike is a lawyer with the gift of photographic memory. He is so good with it that he can tell you all the numbers on a
sheet of paper by having a look at it without any mistake. Mike is also brilliant with subsets so he thought of giving a
challenge based on his skill and knowledge to Rachael. Mike knows how many subset are possible in an array of N
integers. The subsets may or may not have the different sum. The challenge is to find the maximum sum produced by any
subset under the condition:
The elements present in the subset should not have any digit in common.
Note: Subset {12, 36, 45} does not have any digit in common and Subset {12, 22, 35 } have digits in common.Rachael find
it difficult to win the challenge and is asking your help. Can you help her out in winning this challenge?


Input:
First Line of the input consist of an integer T denoting the number of test cases. Then T test cases follow. Each test
case consist of a numbe N denoting the length of the array. Second line of each test case consist of N space separated
integers denoting the array elements.
Constraints:
1 <= T <= 100
1 <= N <= 100
1 <= array elements <= 100000
1
3
12 22 35

Output:
Corresponding to each test case, print output in the new line.
57
"""


def is_same(str1, str2):
    for i in str1:
        for j in str2:
            if i == j:
                return 1
    return 0


def max_sum(arr):
    max = int(arr[len(arr) - 1])
    for i in range(len(arr) - 1):
        sum = int(arr[i])
        for j in range(i + 1, len(arr)):
            if is_same(arr[i], arr[j]) == 1:
                continue
            else:
                sum = sum + int(arr[j])
        if max < sum:
            max = sum
    return max


x = int(input())
myArray = {}
for i in range(0, x):
    n = int(input())
    myList = []
    inputLine = input().split(" ")
    for j in range(n):
        myList.append(inputLine[j])
    myArray[i] = myList
for i in range(0, x):
    print(max_sum(myArray[i]))
