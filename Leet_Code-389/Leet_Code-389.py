'''
Question 389
'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dif = ""
        for l in t:
            if l in s:
                i = s.index(l)
                s = s[:i]+s[i+1:]
            else:
                dif += l
        return dif