class Solution:
    def firstIndex(self,nums,target):
        n=len(nums)
        beg=0
        end=n-1
        mid=beg+(end-beg)//2
        
        result=-1
        while(beg<=end):
            if(nums[mid]==target):
                result=mid
                end=mid-1
            elif(nums[mid]>target):
                end=mid-1
            else:
                beg=mid+1
            
            mid=beg+(end-beg)//2
        
        return result
    
    def lastIndex(self,nums,target):
        n=len(nums)
        beg=0
        end=n-1
        mid=beg+(end-beg)//2
        
        result=-1
        while(beg<=end):
            if(nums[mid]==target):
                result=mid
                beg=mid+1
            elif(nums[mid]>target):
                end=mid-1
            else:
                beg=mid+1
            
            mid=beg+(end-beg)//2
        
        return result
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[]
        res.append(self.firstIndex(nums,target))
        res.append(self.lastIndex(nums,target))
        return res