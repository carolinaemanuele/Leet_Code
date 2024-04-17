'''
Question 506
'''

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        order = sorted(score, reverse = True)
        medals = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
        classification = []
        for x in score:
            c = order.index(x) + 1
            c = medals.get(c) if c <= 3 else str(c)
            classification.append(c)
        return classification
        