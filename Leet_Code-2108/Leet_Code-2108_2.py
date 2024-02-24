'''
Question 2108
'''

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        palindromic = ""
        for word in words:
            if word == "".join(reversed(word)):
                palindromic = word
                break

        return palindromic