'''
Question 34
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        right = 0
        left = len(nums)-1
        if (target & target) in nums:
            while (right<left):
                if nums[right]!=target:
                    right+=1
                if nums[left]!=target:
                    left-=1
                if (nums[right]==target) and (nums[left]==target):
                    break
        else:
            return [-1,-1]
        return [right,left]