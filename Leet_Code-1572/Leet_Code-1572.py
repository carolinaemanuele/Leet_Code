'''
Question 1572
'''

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum_d = 0
        for i in range(len(mat[0])):
            sum_d += mat[i][i]
            sum_d += mat[i][-i-1]
        if len(mat[0]) %2 == 1:
            sum_d -= mat[len(mat[0])//2][len(mat[0])//2]
        return sum_d