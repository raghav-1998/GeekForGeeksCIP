class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l=len(s)
        ans=0
        right=0
        left=0
        
        for i in range(l):
            if(s[i]=='L'):
                left+=1
            else:
                right+=1
            
            if(left==right):
                ans+=1
                left=0
                right=0
        
        return ans