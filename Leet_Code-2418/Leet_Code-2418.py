'''
Question 2418
'''

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = dict(zip(heights, names))
        h = sorted(d, reverse=True)
        names = [d.get(x) for x in h ]
        return names