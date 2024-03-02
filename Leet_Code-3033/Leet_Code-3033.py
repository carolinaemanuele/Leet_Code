'''
Question 3033
'''

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        max_c = 0
        for j in range(len(matrix[0])):
            max_c = max([matrix[x][j] for x in range(len(matrix))])
            for i in range(len(matrix)):
                if matrix[i][j] == -1:
                    matrix[i][j] = max_c
        return matrix