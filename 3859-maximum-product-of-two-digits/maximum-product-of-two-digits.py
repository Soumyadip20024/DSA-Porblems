class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = []
        org = n
        while n>0:
            rem = n%10
            arr.append(rem)
            n = n//10
        n1 = len(arr)
        arr.sort()
        if(n1 == 1):

            return org
        
        return arr[n1-1]*arr[n1-2]



        