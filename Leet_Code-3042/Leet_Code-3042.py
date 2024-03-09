'''
Question 3042
'''

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(word1, word2):
            return word1 == word2[:len(word1)] and word1 == word2[-len(word1):]
        ans = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                ps = isPrefixAndSuffix(words[i], words[j])
                if ps:
                    ans+=1
        return ans