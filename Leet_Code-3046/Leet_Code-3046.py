'''
Question 3046
'''
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        f = list(filter(lambda x:x>=3,Counter(nums).values()))
        if len(f)>=1:
            return False
        return True