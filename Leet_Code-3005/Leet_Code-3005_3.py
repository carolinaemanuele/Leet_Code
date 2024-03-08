'''
Question 3005
'''

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        max_fq = max(c.values())
        f = set(filter(lambda x: c.get(x) == max_fq, nums))
        output = len(f)*max_fq
        return output