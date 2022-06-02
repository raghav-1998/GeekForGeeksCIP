class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n=len(matrix)
        m=len(matrix[0])
        
        transpose=[[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                transpose[i][j]=matrix[j][i]
        
        return transpose