'''
Question 231
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power_two = [(2**x) for x in range(31)]
        if n not in power_two:
            return False
        return True