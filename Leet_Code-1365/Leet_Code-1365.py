'''
Question 1365
'''

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            n = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    n += 1
            output.append(n)
        return output