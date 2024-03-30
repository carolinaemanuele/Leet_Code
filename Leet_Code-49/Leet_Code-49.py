'''
Question 49
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_dict[sorted_word].append(word)
        return list(anagram_dict.values())