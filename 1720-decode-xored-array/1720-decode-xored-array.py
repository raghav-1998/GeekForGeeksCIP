class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        n=len(encoded)+1
        ans=[0]*n
        
        ans[0]=first
        
        for i in range(1,n):
            ans[i]=ans[i-1]^encoded[i-1]
        
        return ans