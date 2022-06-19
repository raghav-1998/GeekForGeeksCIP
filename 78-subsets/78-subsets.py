class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        size=pow(2,n)
        
        ans=[]
        
        for i in range(size):
            sub_ans=[]
            for j in range(n):
                if(i & (1<<j) >0):
                    sub_ans.append(nums[j])
            
            ans.append(sub_ans)
        
        return ans