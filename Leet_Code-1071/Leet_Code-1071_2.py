'''
Question 1071
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        p, divisor = "", ""
        prefix = []
        for x in min(str1,str2):
            p += x
            prefix.append(p)
        for pref in prefix:
            s1 = str1
            s2 = str2
            while s1 != "":
                if s1[:len(pref)] == pref:
                    s1 = s1[len(pref):]
                else:
                    break
            while s2 != "":
                if s2[:len(pref)] == pref:
                    s2 = s2[len(pref):]
                else:
                    break
            if s1 == "" and s2 == "":
                divisor = pref
        return divisor