'''
Question 645
'''

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        output = []
        for x in range(1,len(nums)+1):
            if x not in nums:
                output.append(x)
            if nums.count(x) == 2:
                output.insert(0,x)
            if len(output) == 2:
                break
        return output
            
                