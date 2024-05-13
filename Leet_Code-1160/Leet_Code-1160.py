'''
Question 1160
'''

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for w in words:
            wc = 0
            n = len(w)
            for c in w:
                if chars.count(c) >= w.count(c):
                    wc += 1
            if wc == n:
                ans += wc
        return ans