'''
Question 28
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            index = haystack.index(needle)
            return index
        return -1