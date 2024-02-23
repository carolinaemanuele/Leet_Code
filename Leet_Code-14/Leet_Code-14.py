'''
Question 14 - Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs:
            while prefix != word[:len(prefix)]:
                prefix = prefix[:-1]
        return prefix