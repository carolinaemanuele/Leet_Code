'''
Question 350
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        for x in nums1:
            if x in nums2:
                intersection.append(x)
                nums2.remove(x)
        return intersection