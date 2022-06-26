class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        
        left,right=k-1,n-1
        
        current_sum=sum(cardPoints[:k])
        max_val=current_sum
        
        for _ in range(k):
            current_sum+=(cardPoints[right]-cardPoints[left])
            max_val=max(max_val,current_sum)
            
            left,right=left-1,right-1
            
        return max_val
        