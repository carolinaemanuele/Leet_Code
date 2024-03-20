'''
Question 1748
'''

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum_u = 0
        c = Counter(nums)
        for x in c:
            if c.get(x) == 1:
                sum_u += x
        return sum_u