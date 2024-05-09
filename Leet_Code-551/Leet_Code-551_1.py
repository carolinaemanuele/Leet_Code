'''
Question 551
'''

class Solution:
    def checkRecord(self, s: str) -> bool:
        a, l, p = 0, 0, 0
        for c in s:
            if c == 'A':
                a += 1
                l = 0
                if a>=2:
                    return False
            elif c == 'L':
                l += 1
                if l >=3:
                    return False
            else:
                l = 0
                p += 1
        return True