'''
Question 2108 - Find First Palindromic String in the Array

Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.

'''

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        palindromic = ""
        for word in words:
            if word == "".join(reversed(word)):
                palindromic = word
                break

        return palindromic