'''
Question 349
'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set(nums1) & set(nums2)
        return ans