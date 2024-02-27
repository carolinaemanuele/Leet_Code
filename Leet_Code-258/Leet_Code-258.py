'''
Question 258
'''
class Solution:
    def addDigits(self, num: int) -> int:
        string = str(num)
        while len(string)>1:
            x = 0
            for n in string:
                n = int(n)
                x+=n
            string = str(x)
        return int(string)