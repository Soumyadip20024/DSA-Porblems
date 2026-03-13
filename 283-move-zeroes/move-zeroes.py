class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nonzero = []
        zero = []

        for i in range(len(nums)):
            if nums[i] == 0:
                zero.append(nums[i])
            else:
                nonzero.append(nums[i])
        nums[:]= nonzero + zero
        
        