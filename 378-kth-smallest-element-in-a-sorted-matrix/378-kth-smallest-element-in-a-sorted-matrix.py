class Solution:
    def rank(self,matrix,target):
        count=0
        n=len(matrix)
        i=n-1
        j=0
        
        while(i>=0 and j<n):
            if(matrix[i][j]>target):
                i-=1
            else:
                count+=(i+1)
                j+=1
        
        return count
    
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        low=matrix[0][0]
        high=matrix[n-1][n-1]
        
        while(low<high):
            mid=low+(high-low)//2
            count=self.rank(matrix,mid)
            if(count<k):
                low=mid+1
            else:
                high=mid
        
        return low
                
        
            