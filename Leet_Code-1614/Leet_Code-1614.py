'''
Question 1614
'''

class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        for i in range(len(s)):
            depth = s[:i].count('(') - s[:i].count(')')
            if depth > max_depth:
                max_depth = depth
        return max_depth