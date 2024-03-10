'''
Question 27
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        y = len(nums)
        while k<y:
            if nums[k] == val:
                nums.pop(k)
                y -= 1
            else:
                k+=1
        return k