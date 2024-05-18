'''
Question 1408
'''

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        substrings = []
        for i in range(n):
            for j in (range(i+1, n)):
                if words[j] in words[i] and words[j] not in substrings:
                    substrings.append(words[j])
                elif words[i] in words[j] and words[i] not in substrings:
                    substrings.append(words[i])
        return substrings