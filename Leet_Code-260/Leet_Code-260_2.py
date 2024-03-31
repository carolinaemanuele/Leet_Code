'''
Question 260
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        s = []
        for k, v in c.items():
            if v == 1:
                s.append(k)
        return s