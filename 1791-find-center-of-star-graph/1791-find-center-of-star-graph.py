class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        deg={}
        
        for edge in edges:
            if edge[0] not in deg:
                deg[edge[0]]=1
            else:
                deg[edge[0]]+=1
            
            if edge[1] not in deg:
                deg[edge[1]]=1
            else:
                deg[edge[1]]+=1
                
        n=len(deg)
        
        for v in deg:
            if(deg[v]==n-1):
                return v