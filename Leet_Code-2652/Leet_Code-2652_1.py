'''
Question 2652
'''
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        nums = [x for x in range(1,n+1) if (x%3==0) or (x%5==0) or (x%7==0)]
        return sum(nums)