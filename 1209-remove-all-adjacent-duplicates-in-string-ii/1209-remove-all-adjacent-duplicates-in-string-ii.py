class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stck = []    
        
        for c in s:                            
            if stck and stck[-1][0] == c: # check if stack is not empty
                stck[-1][1]+=1
                if stck[-1][1] == k:
                    stck.pop()
            else:
                stck.append([c, 1])            
        
        return ''.join(c * cnt for c, cnt in stck)  