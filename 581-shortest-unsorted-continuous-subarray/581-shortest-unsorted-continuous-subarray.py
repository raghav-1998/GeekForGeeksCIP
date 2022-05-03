class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = n, 0
        
        cur_max = float('-inf')
        cur_min = float('inf')
        
        for i in range(n):
            if cur_max > nums[i]:
                right = i
            if nums[n-i-1] > cur_min:
                left = n-i-1
            cur_max = max(cur_max, nums[i])
            cur_min = min(cur_min, nums[n-i-1])
        
        return max(0, right-left+1)