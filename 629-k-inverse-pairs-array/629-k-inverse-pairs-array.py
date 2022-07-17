class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        ds = [0] + [1] * (k + 1)
        for i in range(2, n+1):
            new = [0]
            for j in range(k+1):
                v = ds[j+1]
                v -= ds[j-i+1] if j >= i else 0
                new.append( (new[-1] + v) % MOD )
            ds = new
        return (ds[k+1] - ds[k]) % MOD