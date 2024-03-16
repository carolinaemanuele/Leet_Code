'''
Question 342
'''

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        return log(n,4) == int(log(n,4))