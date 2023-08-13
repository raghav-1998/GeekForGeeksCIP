
class Solution:
    def nthFibonacci(self, n : int) -> int:
        # code here
        
        A=1
        B=1
        if(n==1):
            return A
        
        elif(n==2):
            return B
        
        else:
            for i in range(n-2):
                C=(A+B)%1000000007
                A=B
                B=C
            
            return C


#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends