'''
Question 3038
'''
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        score = nums[0]+nums[1]
        x = score
        operations = 0
        while (x==score):
            del nums[0:2]
            operations+=1
            if len(nums)<2:
                break
            x = nums[0]+nums[1]
        return operations