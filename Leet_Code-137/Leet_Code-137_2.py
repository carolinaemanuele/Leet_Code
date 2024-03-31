'''
Question 137
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for k,v in c.items():
            if v!=3:
                return k