'''

Question 4 - Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        nums.extend(nums1)
        nums.extend(nums2)
        nums.sort()
        if (len(nums) % 2 == 0):
            return (nums[len(nums)//2]+nums[(len(nums)//2)-1])/2
        return nums[len(nums)//2]