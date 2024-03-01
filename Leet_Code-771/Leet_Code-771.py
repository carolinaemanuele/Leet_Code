'''
Question 771
'''

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        output = 0
        for x in jewels:
            for y in stones:
                if x==y:
                    output+=1
        return output