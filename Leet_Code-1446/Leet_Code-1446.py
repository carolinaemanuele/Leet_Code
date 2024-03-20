'''
Question 1446
'''

class Solution:
    def maxPower(self, s: str) -> int:
        count_max = 1
        count = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count +=1
            else:
                count = 1
            if count > count_max:
                count_max = count
        return count_max