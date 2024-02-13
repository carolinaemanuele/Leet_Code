'''
Question 2108 - Find First Palindromic String in the Array

Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.

'''

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        palindromic = ""
        
        for word in words:
            left = 0
            right = len(word)-1
            palindromic += word
            
            while (left < right):
                if (word[left]!=word[right]):
                    palindromic = ""
                    break
                left+=1
                right-=1
  
            if (palindromic!=""):
                break

        return palindromic