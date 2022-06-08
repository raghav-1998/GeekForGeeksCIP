class Solution:
    def isPalindrome(self,s):
        beg=0
        end=len(s)-1
        
        while(beg<end):
            if(s[beg]!=s[end]):
                return 0
            beg+=1
            end-=1
        
        return 1
    def removePalindromeSub(self, s: str) -> int:
        if(self.isPalindrome(s)):
            return 1
        
        return 2