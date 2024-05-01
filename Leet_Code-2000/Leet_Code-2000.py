'''
Question 2000
'''

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)
        word = word[:i+1][::-1] + word[i+1:]
        return word