'''
Question 34 - Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        right = 0
        left = len(nums)-1
        if (target & target) in nums:
            while (right<left):
                if nums[right]!=target:
                    right+=1
                if nums[left]!=target:
                    left-=1
                if (nums[right]==target) and (nums[left]==target):
                    break
        else:
            return [-1,-1]
        return [right,left]