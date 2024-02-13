'''
Question 11 - Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
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