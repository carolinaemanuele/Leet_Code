class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        return len(list(c.values())) == len(list(set(c.values())))
