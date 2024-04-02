'''
Question 205
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cs = []
        ct = []
        c = 0
        for ls in range(1,len(s)):
            if s[ls] == s[ls-1]:
                c += 1
            else:
                c = 0
            cs.append(c)
        c = 0
        for lt in range(1,len(t)):
            if t[lt] == t[lt-1]:
                c += 1
            else:
                c= 0
            ct.append(c)
        a = ct == cs
        counter_s = Counter(s)
        counter_t = Counter(t)
        b = list(counter_s.values()) == list(counter_t.values())
        return a and b