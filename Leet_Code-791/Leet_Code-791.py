'''
Question 791
'''

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        output = ''
        for o in order:
            for l in s:
                if o == l:
                    output += o
                    j = s.find(o)
                    s = s[:j]+s[j+1:]
        output += s
        return output