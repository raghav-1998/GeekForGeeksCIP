class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans=0
        right=0
        left=0
        
        for c in s:
            if(c=='L'):
                left+=1
            else:
                right+=1
            
            if(left==right):
                ans+=1
                left=0
                right=0
        
        return ans