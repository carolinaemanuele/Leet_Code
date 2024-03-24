'''
Question 3083
'''

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        sr = s[::-1]
        for i in range(len(s)-1):
            if s[i:i+2] in sr:
                return True
        return False