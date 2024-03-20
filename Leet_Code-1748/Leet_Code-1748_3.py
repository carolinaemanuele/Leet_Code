'''
Question 1748
'''

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        u = [x for x in nums if nums.count(x)==1]
        s = sum(u)
        return s