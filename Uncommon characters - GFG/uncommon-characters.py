#User function Template for python3

class Solution:
    def UncommonChars(self,A, B):
        #code here
        ch=list(set(A+B))
        ch.sort()
        res=''
        for c in ch:
            if not(c in A and c in B):
                res+=c
        
        return res if len(res)>=1 else "-1"

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.UncommonChars(A, B))

# } Driver Code Ends