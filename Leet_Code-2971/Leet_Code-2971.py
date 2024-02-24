'''
Question 2971
'''

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        perimeter = -1
        i = 0
        while i<len(nums):
            if (nums[i] >= sum(nums)-nums[i]):
                nums.remove(nums[i])
                continue
            else:
                break
            i += 1
        if len(nums)>=3:
            perimeter = sum(nums)
        return perimeter