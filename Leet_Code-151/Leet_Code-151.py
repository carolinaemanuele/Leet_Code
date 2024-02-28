'''
Question 151
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""
        output = ""
        s = s.strip()
        for i in range(len(s)):
            if s[i]!=" ":
                word+=s[i]
            elif (s[i]==" ") and (word!=""):
                words.append(word)
                word = ""
            if (i == len(s)-1):
                words.append(word)
        for j in range(-1,-len(words)-1,-1):
            output+=words[j]
            if j != -len(words):
                output+=" "
        return output