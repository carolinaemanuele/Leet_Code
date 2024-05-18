'''
Question 1051
'''

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = sorted(heights)
        w = len(list(filter(lambda i: exp[i] != heights[i], range(len(exp)))))
        return w