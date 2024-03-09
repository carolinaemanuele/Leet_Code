'''
Question 2540
'''

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = list(set(nums1) & set(nums2))
        try:
            return min(i)
        except:
            return -1