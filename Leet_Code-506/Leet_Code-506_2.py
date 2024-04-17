'''
Question 506
'''

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        order = sorted(score, reverse = True)
        classification = []
        for x in score:
            c = order.index(x) + 1
            if c == 1:
                classification.append("Gold Medal")
            elif c == 2:
                classification.append("Silver Medal")
            elif c == 3:
                classification.append("Bronze Medal")
            else:
                classification.append(str(c))
        return classification
        