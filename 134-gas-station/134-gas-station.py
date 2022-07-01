class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        pos,tot,total=0,0,0
        
        for i in range(n):
            tot+=gas[i]-cost[i]
            if(tot<0):
                total+=tot
                tot=0
                pos=i+1
        
        total+=tot
        return pos if(total>=0) else -1