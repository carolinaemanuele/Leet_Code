'''
Question 90
'''

from itertools import combinations
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ss = []
        nums.sort()
        for i in range(len(nums)+1):
            c = combinations(nums,i)
            for x in c:
                if list(x) not in ss:
                 ss.append(list(x))
        return ss