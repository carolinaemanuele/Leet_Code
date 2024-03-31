'''
Question 137
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = filter(lambda x: nums.count(x)!=3,nums)
        return next(s)