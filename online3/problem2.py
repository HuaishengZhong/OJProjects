def SieveOfEratosthenes(n, isPrime):
    isPrime[0] = isPrime[1] = False
    for i in range(2, n + 1):
        isPrime[i] = True
    p = 2
    while (p * p <= n):
        if (isPrime[p] == True):

            # Update all multiples of p
            i = p * 2
            while (i <= n):
                isPrime[i] = False
                i += p
        p += 1


def findPrimePair(n):
    isPrime = [0] * (n + 1)
    SieveOfEratosthenes(n, isPrime)
    for i in range(0, n):
        if (isPrime[i] and isPrime[n - i]):
            print(i, (n - i))
            return


num_cases = int(input())
for i in range(num_cases):
    findPrimePair(int(input()))
