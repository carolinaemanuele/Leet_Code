'''
Question 914
'''

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        c = deck.count(deck[0])
        cx = [deck.count(x) for x in set(deck)]
        cgcd = [gcd(c,x) for x in cx]
        if c<1 or 1 in cgcd or gcd(*cgcd)==1:
            return False
        return True