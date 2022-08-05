class Solution:
    def helper(self,nums,target,dp):
        if(target==0):
            return 1
        if(dp[target]!=-1):
            return dp[target]
        dp[target]=0
        
        for num in nums:
            if(num<=target):
                dp[target]+=self.helper(nums,target-num,dp)
        
        return dp[target]
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[-1]*(target+1)
        return self.helper(nums,target,dp)