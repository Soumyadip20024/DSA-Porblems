class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[-1]*n for _ in range(m)]

        return self.solve(obstacleGrid, 0, 0, m, n, dp)

    def solve(self, grid, i, j, m, n, dp):
        if i>=m or j>=n or grid[i][j]==1 :
            return 0
        if i==m-1 and j==n-1:
            return 1

        if dp[i][j] != -1:
            return dp[i][j]

        r = self.solve(grid, i+1, j, m, n, dp)
        d = self.solve(grid, i, j+1, m, n, dp)

        dp[i][j] = r+d

        return r+d
        