'''
Question 204
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        p = 2
        prime = [True for x in range(n+1)]
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        if n>1:
            prime.pop(1)
            prime.pop()
        elif n==1:
            prime.pop(1)
        prime.pop(0)
        result = prime.count(True)
        return result