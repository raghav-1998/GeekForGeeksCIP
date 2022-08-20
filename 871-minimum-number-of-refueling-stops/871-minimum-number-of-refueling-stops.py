class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        
        n = len(stations)
        # dp[j]: in former i stations, pick j stations to fuel, how far it can mostly reach
        dp = [startFuel] + [0] * n
        rst = sys.maxsize
        for i in range(1, n + 1):
            # since dp[i][j] relates to dp[i - 1][j] and dp[i - 1][j - 1],
            # if updating the compressed 1-d dp array left -> right, dp[j - 1] is updated before dp[j] with row i's dp[i][j - 1] value, which replaced the target value dp[i - 1][j - 1]
            # if updating the compressed 1-d dp array right -> left, dp[j - 1] hasn't been udpated when calculating dp[j], which remains the target value dp[i - 1][j - 1]
            for j in range(i, 0, -1): 
                if dp[j - 1] >= stations[i - 1][0]:
                    dp[j] = max(dp[j], dp[j - 1] + stations[i - 1][1])
                if dp[j] >= target:
                    rst = min(rst, j)
        return rst if rst != sys.maxsize else -1