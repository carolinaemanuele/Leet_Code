'''
Question 704
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            i = nums.index(target)
            return i
        return -1