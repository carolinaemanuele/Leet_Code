'''
Question 977
'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        x = sorted([(abs(x))**2 for x in nums])
        return x