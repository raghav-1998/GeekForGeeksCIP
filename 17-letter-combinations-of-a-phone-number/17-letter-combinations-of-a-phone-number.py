class Solution:
    def fun(self,digits,digit_map_letter,ans,n,i,temp):
        if(i>n):
            return
        if(i==n):
            ans.append(temp)
            return
        for s in digit_map_letter[digits[i]]:
            self.fun(digits,digit_map_letter,ans,n,i+1,temp+s)
            
    def letterCombinations(self, digits: str) -> List[str]:
        if(digits==""):
            return []
        digit_map_letter={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':                                    ['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':                                  ['t','u','v'],'9':['w','x','y','z']}
        ans=[]
        n=len(digits)
        self.fun(digits,digit_map_letter,ans,n,0,"")
        return ans
        
                
        
        