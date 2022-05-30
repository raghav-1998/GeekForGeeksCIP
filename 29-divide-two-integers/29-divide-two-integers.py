class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        isNeg = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        q = 0
        for n in range(31, -1, -1):
            divmul = divisor << n
            if divmul <= dividend:
                q += 2**n
                dividend -= divmul
                
        return q if not isNeg else -q