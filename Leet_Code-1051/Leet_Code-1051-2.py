'''
Question 1051
'''

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        w = 0
        for i in range(len(expected)):
            if expected[i] != heights[i]:
                w += 1
        return w