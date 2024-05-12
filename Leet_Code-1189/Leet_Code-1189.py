'''
Question 1189
'''

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = text.count('b')
        a = text.count('a')
        l = text.count('l')//2
        o = text.count('o')//2
        n = text.count('n')
        if b == 0 or a == 0 or l == 0 or o == 0 or n == 0:
            return 0
        return min(b,a,l,o,n)