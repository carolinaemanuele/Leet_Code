'''
Question 551
'''

class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') >= 2 or 'LLL' in s:
            return False
        return True