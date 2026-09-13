class Solution(object):
    def rotate(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(mat)
        #transpose
        for i in range(n):
            for j in range(i, n):
                #swap mat[i][j] & mat[j][i]
                temp = mat[i][j]
                mat[i][j] = mat[j][i]
                mat[j][i] = temp

        for i in range(n):
            for j in range(n//2):
                #swap mat[i][j] & mat[i][n-j+1]
                temp = mat[i][j]
                mat[i][j] = mat[i][n-j-1]
                mat[i][n-j-1] = temp
