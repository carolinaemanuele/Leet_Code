'''
Question 47
'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        p = permutations(nums, len(nums))
        pu = set(p)
        return list(pu)