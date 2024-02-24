'''
Question 2149
'''

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        x = 0
        positive = 0
        negative = 1
        output = [0]*len(nums)
        while (x<len(nums)) and (positive <= len(nums)+1/2):
            if (nums[x]<0):
                output[negative] = nums[x]
                negative+=2
            else:
                output[positive] = nums[x]
                positive+=2
            x+=1
        return output