'''
Question 90
'''

from itertools import combinations
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = set()
        nums.sort()
        for i in range(len(nums)+1):
            for c in combinations(nums,i):
                subsets.add(c)
        ss = [list(s) for s in subsets]
        return ss