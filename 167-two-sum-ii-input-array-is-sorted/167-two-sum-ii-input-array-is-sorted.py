class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[]
        
        beg=0
        end=len(numbers)-1
        
        while(beg<end):
            if(numbers[beg]+numbers[end]<target):
                beg+=1
            elif(numbers[beg]+numbers[end]>target):
                end-=1
            else:
                res.append(beg+1)
                res.append(end+1)
                break
        
        return res