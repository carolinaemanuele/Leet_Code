'''
Question 11
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        x1 = 0
        x2 = n-1
        a = 0
        b = 0
        while (x1 < x2):
            if (height[x1]>=height[x2]):
                b = height[x2]*(x2-x1)
                x2-=1
            elif (height[x2]>height[x1]):
                b = height[x1]*(x2-x1)
                x1+=1
            else:
                continue
            if b>a:
                a=b
        return a