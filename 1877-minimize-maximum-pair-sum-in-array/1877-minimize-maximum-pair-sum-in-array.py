class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        lis=[0]*(n//2)
        
        for i in range(n//2):
            lis[i]=nums[i]+nums[n-1-i]
        
        return max(lis)