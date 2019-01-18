from collections import defaultdict


def findManhattanEuclidPair(arr, n):
    X = defaultdict(lambda:0)
    Y = defaultdict(lambda:0)
    XY = defaultdict(lambda:0)

    for i in range(0, n):
        xi = arr[i][0]
        yi = arr[i][1]
        X[xi] += 1
        Y[yi] += 1
        XY[tuple(arr[i])] += 1

    xAns, yAns, xyAns = 0, 0, 0

    for xCoordinatePair in X:
        xFrequency = X[xCoordinatePair]
        sameXPairs = (xFrequency * (xFrequency - 1)) // 2
        xAns += sameXPairs

    for yCoordinatePair in Y:
        yFrequency = Y[yCoordinatePair]
        sameYPairs = (yFrequency * (yFrequency - 1)) // 2
        yAns += sameYPairs

    for XYPair in XY:
        xyFrequency = XY[XYPair]
        samePointPairs = (xyFrequency * (xyFrequency - 1)) // 2
        xyAns += samePointPairs

    return (xAns + yAns - xyAns)


num_cases = int(input())
for _ in range(num_cases):
    arr = []
    n = int(input())
    for i in range(n):
        arr.append([int(x) for x in input().split()])
    print(findManhattanEuclidPair(arr, n))
