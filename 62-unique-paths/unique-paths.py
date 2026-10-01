class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[-1] * n for _ in range(m)]
        
        return self.solve(0, 0, m, n, dp)


    def solve(self, i, j, m, n, dp):
        if i>=m or j>=n:
            return 0
        if i==m-1 or j==n-1:
            return 1

        if dp[i][j] != -1:
            return dp[i][j]

        r = self.solve(i+1, j, m, n, dp)
        d = self.solve(i, j+1, m, n, dp)

        dp[i][j] = r+d

        return r+d
        
        