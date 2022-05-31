class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        us=set()
        n=len(s)
        
        for i in range(n-k+1):
            us.add(s[i:i+k])
        
        return len(us) == 1<<k