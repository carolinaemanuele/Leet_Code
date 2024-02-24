'''
Question 2108
'''

class Solution:
    def firstPalindrome(self, words) -> str:
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