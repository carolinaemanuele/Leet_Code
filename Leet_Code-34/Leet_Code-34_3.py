'''
Question 34 - Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if (target & target) in nums:
            x = [i for i,num in enumerate(nums) if num==target]
            return [min(x),max(x)]
        return [-1,-1]