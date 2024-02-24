'''
Question 14
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs:
            while prefix != word[:len(prefix)]:
                prefix = prefix[:-1]
        return prefix