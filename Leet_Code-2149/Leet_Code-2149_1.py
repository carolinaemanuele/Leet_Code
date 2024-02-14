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
        positive = []
        negative = []
        output = []
        for x in nums:
            if (x<0):
                negative.append(x)
            else:
                positive.append(x)
        for i in range(0,len(positive)):
            output.append(positive[i])
            output.append(negative[i])
        
        return output