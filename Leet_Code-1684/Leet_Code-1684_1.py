'''
Question 1684
'''

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent = 0
        for word in words:
            for i in range(len(word)):
                if word[i] not in allowed:
                    break
                elif i == len(word)-1 and word[i] in allowed:
                    consistent += 1
        return consistent