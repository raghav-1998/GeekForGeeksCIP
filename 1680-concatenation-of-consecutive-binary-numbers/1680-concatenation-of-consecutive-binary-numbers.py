class Solution:
    def concatenatedBinary(self, n: int) -> int:
        def bin_pow(num): return [1<<i for i, b in enumerate(bin(num)[:1:-1]) if b == "1"]
        ans, MOD, q = 0, 10**9 + 7, len(bin(n)) - 3

        B = bin_pow((1<<q) - 1) + bin_pow(n - (1<<q) + 1)[::-1]
        C = list(range(1, q+1)) + [q+1]*(len(B) - q)
        D = list(accumulate(i*j for i,j in zip(B[::-1], C[::-1])))[::-1][1:] + [0]
        
        for a, b, c, d in zip(accumulate(B), B, C, D):
            t1 = pow(2, b*c, MOD) - 1
            t2 = pow(pow(2, c, MOD)-1, MOD - 2, MOD)
            ans += t2*((a-b+1+t2)*t1-b)*pow(2, d, MOD)

        return ans % MOD