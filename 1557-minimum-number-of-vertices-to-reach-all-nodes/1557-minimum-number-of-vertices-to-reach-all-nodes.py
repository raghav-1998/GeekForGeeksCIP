class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indeg={}
        
        for edge in edges:
            if edge[0] not in indeg:
                indeg[edge[0]]=0
            
            if edge[1] not in indeg:
                indeg[edge[1]]=1
            else:
                indeg[edge[1]]+=1
        
        ans=[]
        
        for vertex in indeg:
            if indeg[vertex]==0:
                ans.append(vertex)
        
        return ans