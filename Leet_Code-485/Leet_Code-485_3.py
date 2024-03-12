'''
Question 485
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        consecutive = 0
        if 1 in nums:
            for i in range(1, len(nums)):
                if nums[i-1] == nums[i] and nums[i] == 1:
                    consecutive += 1
                if nums[i] == 0 or (i == len(nums)-1):
                    if consecutive > max_consecutive:
                        max_consecutive = consecutive
                    consecutive = 0
            max_consecutive += 1
        return max_consecutive