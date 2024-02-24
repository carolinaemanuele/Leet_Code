'''
Question 287
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c = Counter(nums)
        f = filter(lambda x: c[x]>=2,c)
        return next(f)