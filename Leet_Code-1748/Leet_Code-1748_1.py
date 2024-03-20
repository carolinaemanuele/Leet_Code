'''
Question 1748
'''

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        f = list(filter(lambda x: nums.count(x)==1, nums))
        s = sum(f)
        return s