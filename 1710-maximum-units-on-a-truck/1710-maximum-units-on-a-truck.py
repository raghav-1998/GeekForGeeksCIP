class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda row:row[1],reverse=True)
        #print(boxTypes)
        n=len(boxTypes)
        ans=0
        i=0
        while(truckSize>0 and i<n):
            if(truckSize>=boxTypes[i][0]):
                ans+=(boxTypes[i][0]*boxTypes[i][1])
            else:
                ans+=(truckSize*boxTypes[i][1])
            truckSize-=boxTypes[i][0]
            i+=1
        
        return ans