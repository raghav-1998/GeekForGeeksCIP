class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        for x in [2, 3, 5]:
            while n % x == 0:
                n = n // x
        return n == 1