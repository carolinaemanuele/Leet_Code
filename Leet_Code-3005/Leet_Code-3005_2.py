'''
Question 3005
'''

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        max_fq = max(c.values())
        f = [x for x in c.values() if x == max_fq]
        output = len(f)*max_fq
        return output