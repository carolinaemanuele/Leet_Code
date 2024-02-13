'''
Question 13 - Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        z=[]
        x=0
        a=0
        for i in range(0,len(s)):
            if (s[i]=='I'):
                a=1
            elif (s[i]=='V'):
                a=5
            elif (s[i]=='X'):
                a=10
            elif (s[i]=='L'):
                a=50
            elif (s[i]=='C'):
                a=100
            elif (s[i]=='D'):
                a=500
            elif (s[i]=='M'):
                a=1000
            z.append(a)

        for j in range(0,len(z)):
            if (j==len(z)-1):
                x+=z[j]
            elif (z[j]>=z[j+1]):
                x+=z[j]
            else:
                x+=-z[j]
        return x
        