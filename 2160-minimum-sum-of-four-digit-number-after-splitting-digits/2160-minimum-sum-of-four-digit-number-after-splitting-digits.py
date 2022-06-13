class Solution:
    def minimumSum(self, num: int) -> int:
        lis=[0]*4
        
        for i in range(4):
            lis[i]=num%10
            num//=10
        
        lis.sort()
        
        num1=(10*lis[0])+lis[3]
        num2=(10*lis[1])+lis[2]
        
        return num1+num2