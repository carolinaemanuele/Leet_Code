'''
Question 1041
'''

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        position = [0,0]
        directions = {0: [0,1], 1:[-1,0], 2:[0,-1], 3:[1,0]}
        i = 0
        for n in range(5):
            for l in instructions:
                if l == 'L' and i < 3:
                    i+=1
                elif l == 'L' and i == 3:
                    i = 0
                elif l == 'R' and i>0:
                    i -= 1
                elif l == 'R' and i == 0:
                    i = 3
                else:
                    position[0] += directions[i][0]
                    position[1] += directions[i][1]
            if position == [0,0]:
                return True
        return False