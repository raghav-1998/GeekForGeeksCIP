class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0 for i in range(n)]
        
        res[0]=nums[0]
        
        for i in range(1,n):
            res[i]=res[i-1]+nums[i]
        
        return res