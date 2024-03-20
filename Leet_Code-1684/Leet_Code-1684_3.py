'''
Question 1684
'''

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        f = list(filter(lambda w: set(w).issubset(set(allowed)), words))
        consistent = len(f)
        return consistent