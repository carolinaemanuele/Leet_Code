'''
Question 645
'''

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        f_d = filter(lambda x: nums.count(x)==2, nums)
        f_n = filter(lambda x: x not in nums, range(1,len(nums)+1))
        output = [next(f_d), next(f_n)]
        return output