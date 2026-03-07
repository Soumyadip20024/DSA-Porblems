class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        uplimit = 2147483647
        lowlimit = -2147483648

        if x > 0:
            rev = 0
            rem=0
            while(x != 0):
                rem = x % 10
                rev = rev * 10 + rem
                x = x//10
            if rev>uplimit or rev<lowlimit :
                    return 0
            return rev
        else:
            x = -x
            rev = 0
            rem=0
            while(x != 0):
                rem = x % 10
                rev = rev * 10 + rem
                x = x//10
            if rev>uplimit or rev<lowlimit :
                    return 0
            return -rev