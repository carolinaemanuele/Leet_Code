'''
Question 4
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