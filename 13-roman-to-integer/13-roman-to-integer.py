class Solution:
    def romanToInt(self, s: str) -> int:
        mapp={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n=len(s)
        ans=0
        i=0
        while(i<n):
            if(i+1<n):
                if(mapp[s[i]]<mapp[s[i+1]]):
                    ans+=(mapp[s[i+1]]-mapp[s[i]])
                    i+=2
                else:
                    ans+=mapp[s[i]]
                    i+=1
            else:
                ans+=mapp[s[i]]
                i+=1
            
            #print(ans)
        return ans
                