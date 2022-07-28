class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s=len(s)
        len_t=len(t)
        
        if(len_s!=len_t):
            return False
        
        set_w=set(s)
        
        for char in set_w:
            if(char not in t):
                return False
            elif(s.count(char)!=t.count(char)):
                return False
            
        return True