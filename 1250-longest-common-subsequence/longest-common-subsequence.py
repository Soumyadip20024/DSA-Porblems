class Solution(object):
    def longestCommonSubsequence(self, s1, s2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(s1)
        n = len(s2)

        dp = [[-1]*n for _ in range(m)]

        return self.solve(0, 0, s1, s2, dp)
    
    def solve(self, i, j, s1, s2, dp):
        
        m = len(s1)
        n = len(s2)

        if i<0 or j<0 or i>=m or j>=n:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if s1[i] == s2[j]:
            dp[i][j] = 1 + self.solve(i+1, j+1, s1, s2, dp)
            return 1 + self.solve(i+1, j+1, s1, s2, dp)

        dp[i][j] = max(self.solve(i+1, j, s1, s2, dp), self.solve(i, j+1, s1, s2, dp))

        return max(self.solve(i+1, j, s1, s2, dp), self.solve(i, j+1, s1, s2, dp))
        