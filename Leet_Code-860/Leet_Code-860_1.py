'''
Question 860
'''

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5 = 0
        count10 = 0
        for x in bills:
            if x == 5:
                count5 +=1
            elif x == 10 and count5 >=1:
                count5 -= 1
                count10 += 1
            elif x == 20 and count5>=1 and count10>=1:
                count5 -= 1
                count10 -=1
            elif x == 20 and count5 >=3:
                count5 -= 3
            else:
                return False
        return True