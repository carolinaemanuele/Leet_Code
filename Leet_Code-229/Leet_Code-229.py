'''
Question 229
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        n = len(nums)
        f = filter(lambda x: c.get(x)>n/3,c.keys())
        return list(f)