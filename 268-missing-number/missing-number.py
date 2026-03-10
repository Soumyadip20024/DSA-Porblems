class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        s = (n*(n+1))//2
        sum =0

        for i in range(n):
            sum = sum + nums[i]

        return (s - sum)
        