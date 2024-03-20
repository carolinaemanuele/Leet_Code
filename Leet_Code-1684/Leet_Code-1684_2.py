'''
Question 1684
'''

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        f = list(filter(lambda w: not set(w).issubset(set(allowed)), words))
        consistent = len(words)-len(f)
        return consistent