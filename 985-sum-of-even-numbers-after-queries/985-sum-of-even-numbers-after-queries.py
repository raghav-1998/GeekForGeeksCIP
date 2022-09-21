class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = sum(a for a in nums if a % 2 == 0)
        ans = []
        for val, idx in queries: 
            if nums[idx] % 2 == 0:
                s -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0:
                s += nums[idx] 
            ans.append(s)
        return ans