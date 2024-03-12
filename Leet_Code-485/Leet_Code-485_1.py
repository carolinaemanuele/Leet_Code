'''
Question 485
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        if 1 in nums:
            consecutive = 0
            for x in nums:
                if x == 1:
                    consecutive += 1
                else:
                    consecutive = 0
                if consecutive > max_consecutive:
                    max_consecutive = consecutive
        return max_consecutive