'''
Question 1071
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not (str1+str2 == str2+str1):
            return ""
        divisor = gcd(len(str1), len(str2))
        return str1[:divisor]