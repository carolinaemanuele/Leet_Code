'''
Question 128
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        consts = [1 if len(nums)>=1 else 0]
        cons = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                cons += 1
            else:
                consts.append(cons)
                cons = 1
            consts.append(cons)
        return max(consts)