'''
https://leetcode.com/problems/unique-paths/
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def matrix_get(i,j, matrix):
            if i >= len(matrix) or j >= len(matrix[0]):
                return 0
            
            return matrix[i][j]

        matrix = [[0 for _ in range(n)] for _ in range(m)]
        matrix[m-1][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                matrix[i][j] = max(matrix[i][j], 
                    matrix_get(i, j+1, matrix) + matrix_get(i+1, j, matrix))

        return matrix[0][0]