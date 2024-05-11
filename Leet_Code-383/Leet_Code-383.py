'''
Question 383
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        i = -1
        for c in ransomNote:
            i = magazine.find(c)
            if i == -1:
                return False
            else:
                magazine = magazine[:i] + magazine[i+1:]
        return True