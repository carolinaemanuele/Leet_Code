'''
Question 326
'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while (n>=3):
            n = n/3
        if n==1:
            return True
        return False