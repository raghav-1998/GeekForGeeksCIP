class Solution:
    def firstUniqChar(self, s: str) -> int:
        occur={}
        n=len(s)
        for ch in s:
            if ch not in occur:
                occur[ch]=1
            else:
                occur[ch]+=1
                
        for i in range(n):
            if(occur[s[i]]==1):
                return i
        
        return -1