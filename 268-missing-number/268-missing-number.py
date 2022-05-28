class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        act_tot=(n*(n+1))//2
        
        tot=0
        for num in nums:
            tot+=num
        
        ans=act_tot-tot
        
        return ans