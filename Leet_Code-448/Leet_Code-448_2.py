'''
Question 448
'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        i = len(nums)+1
        d = [x for x in range(1,i) if x not in s]
        return d