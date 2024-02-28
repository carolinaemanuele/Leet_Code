'''
Question 2109
'''

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output = ""
        x = 0
        for i in range(len(spaces)):
            output += s[x:spaces[i]]
            output += " "
            x = spaces[i]
            if i == len(spaces)-1:
                output += s[x:]
        return output