class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        max_val=nums[0]+nums[n-1]
        
        for i in range(1,n//2):
            val=nums[i]+nums[n-1-i]
            max_val=max(max_val,val)
        
        return max_val