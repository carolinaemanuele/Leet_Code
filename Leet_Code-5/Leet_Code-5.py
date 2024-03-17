'''
Question 5
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        sub = ''
        if len(s) == 1:
            return s
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                ss = s[i:j]
                if ss == ss[::-1] and len(ss) > len(sub):
                    sub = ss
        return sub