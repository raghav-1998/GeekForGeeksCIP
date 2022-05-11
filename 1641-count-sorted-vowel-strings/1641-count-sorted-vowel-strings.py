class Solution:
    def countVowelStrings(self, n: int) -> int:
        counts = []
        for i in range(5):
            counts.append(1)
   
        for i in range(2, n + 1):
            for j in range(3, -1, -1):
                counts[j] += counts[j + 1]
   
        ans = 0
    
        for c in counts:
            ans += c
        
        return ans