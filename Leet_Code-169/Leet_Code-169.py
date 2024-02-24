'''
Question 169
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for x in set(nums):
            if nums.count(x)>len(nums)/2:
                majority = x
                break
        return majority