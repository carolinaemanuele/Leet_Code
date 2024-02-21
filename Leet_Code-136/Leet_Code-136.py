'''

Question 136 - Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        return list(c.keys())[list(c.values()).index(1)]