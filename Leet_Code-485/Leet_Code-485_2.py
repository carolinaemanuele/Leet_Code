'''
Question 485
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        consecutive = 0
        i = 0
        if 1 in nums:
            while i < len(nums):
                if nums[i] == 1:
                    consecutive += 1
                else:
                    consecutive = 0
                if consecutive > max_consecutive:
                    max_consecutive = consecutive
                i += 1
        return max_consecutive