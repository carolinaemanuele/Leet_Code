'''
Question 448
'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        i = len(nums)+1
        f = list(filter(lambda x: x not in s, range(1,i)))
        return f