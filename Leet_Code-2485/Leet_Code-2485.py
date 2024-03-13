'''
Question 2485
'''

class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return 1
        pivot = -1
        for i in range(1,n):
            if sum(range(1,i+1)) == sum(range(i,n+1)):
                pivot = i
                break
        return pivot