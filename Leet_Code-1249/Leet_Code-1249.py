'''
Question 1249
'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        c_open = []
        c_close = []
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '(':
                c_open.append(i)
            elif s[i] == ')':
                c_close.append(i)
                if len(c_close) > len(c_open):
                    s = s[:i]+s[i+1:]
                    c_close.pop()
                    n -=1
                    i -= 1
            i += 1
        while len(c_open) > len(c_close):
            c = c_open[-1]
            s = s[:c]+s[c+1:]
            c_open.pop()
        return s