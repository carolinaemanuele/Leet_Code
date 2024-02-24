'''

Question 136
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        return list(c.keys())[list(c.values()).index(1)]