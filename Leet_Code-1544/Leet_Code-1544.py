'''
Question 1544
'''

class Solution:
    def makeGood(self, s: str) -> str:
        ls = []
        for l in s:
            if ls and ls[-1].swapcase() == l:
                ls.pop()
            else:
                ls.append(l)
        s = "".join(ls)
        return s