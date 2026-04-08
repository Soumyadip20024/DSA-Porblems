class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        n1 = nums1[:m]
        n2 = nums2[:n]
        n3 = n1 + n2
        n3.sort()
        
        for i in range(len(n3)):
            nums1[i] = n3[i]
        