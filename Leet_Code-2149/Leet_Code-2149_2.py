'''
Question 2149 - Rearrange Array Elements by Sign

You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

- Every consecutive pair of integers have opposite signs.
- For all integers with the same sign, the order in which they were present in nums is preserved.
- The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

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