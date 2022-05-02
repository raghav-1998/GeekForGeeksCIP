class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i=0
        j=n-1
        
        while(i<j):
            if(nums[i]%2!=0):
                if(nums[j]%2==0):
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
                    i+=1
                    j-=1
                else:
                    j-=1
            else:
                i+=1
        
        return nums
                
            
        