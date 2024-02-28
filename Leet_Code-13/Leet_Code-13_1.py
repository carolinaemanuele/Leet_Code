'''
Question 13
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
        