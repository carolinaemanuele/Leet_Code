'''
Question 1748
'''

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        s = sum(x for x in c if c.get(x)==1)
        return s