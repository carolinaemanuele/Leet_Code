'''
Question 2154
'''
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        x = original
        while x in nums:
            x=2*x
        return x