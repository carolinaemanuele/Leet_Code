'''
Question 678
'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        c_open, c_close = 0, 0
        for c in s:
            if c == '(':
                c_open += 1
                c_close += 1
            else:
                c_open = max(c_open - 1, 0)
                c_close = c_close - 1 if c == ')' else c_close + 1
            if c_close < 0:
                return False
        return c_open == 0