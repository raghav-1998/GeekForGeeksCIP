class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = max_cost = 0
        n=len(colors)
        for i in range(n):
            if i > 0 and colors[i] !=colors[i - 1]:
                max_cost = 0
            res += min(max_cost, neededTime[i])
            max_cost = max(max_cost, neededTime[i])
        return res