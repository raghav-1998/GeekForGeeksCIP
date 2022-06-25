class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt=0
        n=len(nums)
        for i in range(1,n):
            if(nums[i-1]>nums[i]):
                if(i<2 or nums[i-2]<=nums[i]):
                    nums[i-1]=nums[i]
                else:
                    nums[i]=nums[i-1]
                
                cnt+=1
        
        return cnt<=1