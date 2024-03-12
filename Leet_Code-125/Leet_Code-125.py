'''
Question 125
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        invalid = set([x for x in s if not x.isalnum()])
        invalid.add(' ')
        for x in invalid:
            s = s.replace(x, '')
        s = s.lower()
        return s == s[::-1]