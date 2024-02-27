'''
Question 2652
'''
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        f = list(filter(lambda x:(x%3==0) or (x%5==0) or (x%7==0),range(1,n+1)))
        return sum(f)