'''
Question 387
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        f = filter(lambda x: c.get(x)==1, c.keys())
        try:
            i = s.index(next(f))
        except:
            i = -1
        return i