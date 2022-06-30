class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        ans,median=0,nums[n//2]
        
        for i in range(n):
            ans+=abs(median-nums[i])
        
        return ans