'''
Question 169 - Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for x in set(nums):
            if nums.count(x)>len(nums)/2:
                majority = x
                break
        return majority