class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])

        def test(i):
            for j in xrange(m):
                i2 = i + grid[j][i]
                if i2 < 0 or i2 >= n or grid[j][i2] != grid[j][i]:
                    return -1
                i = i2
            return i
        return map(test, range(n))
