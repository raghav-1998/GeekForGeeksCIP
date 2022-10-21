class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mydict={}
        
        for index, val in enumerate(nums):
            if val in mydict and index-mydict[val]<=k:
                return True
            mydict[val]=index
        
        return False