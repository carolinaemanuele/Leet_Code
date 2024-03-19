'''
Question 860
'''

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        balance = []
        for x in bills:
            if x == 5:
                balance.append(5)
            elif x == 10 and 5 in balance:
                balance.remove(5)
                balance.append(10)
            elif x == 20 and 5 in balance and 10 in balance:
                balance.remove(5)
                balance.remove(10)
            elif x == 20 and balance.count(5) >=3:
                balance.remove(5)
                balance.remove(5)
                balance.remove(5)
            else:
                return False
        return True