'''
Question 3005
'''

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        max_fq = max(c.values())
        f = list(filter(lambda x: x == max_fq, c.values()))
        output = len(f)*max_fq
        return output