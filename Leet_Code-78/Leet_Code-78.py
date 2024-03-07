'''
Question 78
'''

from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ss = []
        for i in range(len(nums)+1):
            c = combinations(nums,i)
            for x in c:
                ss.append(list(x))
        return ss