'''
Question 260
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = list(filter(lambda x: nums.count(x)==1, nums))
        return s