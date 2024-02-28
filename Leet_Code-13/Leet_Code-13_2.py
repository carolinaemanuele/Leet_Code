'''
Question 13
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        z=[]
        x=0
        conversion = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)):
            z.append(conversion.get(s[i]))

        for j in range(len(z)):
            if (j==len(z)-1):
                x+=z[j]
            elif (z[j]>=z[j+1]):
                x+=z[j]
            else:
                x+=-z[j]
        return x