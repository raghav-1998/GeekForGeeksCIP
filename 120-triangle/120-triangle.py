class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        memo = [None] * n
        k= n - 1
     
    # For the bottom row
        for i in range(len(triangle[k])):
            memo[i] = triangle[k][i]
 
    # Calculation of the
    # remaining rows,
    # in bottom up manner.
        for i in range(n- 2, -1,-1):
            for j in range(len(triangle[i])):
                memo[j] = triangle[i][j] + min(memo[j],
                                    memo[j + 1]);
 
    # return the top element
        return memo[0]