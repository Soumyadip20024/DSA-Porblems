class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = list(s)
        v = "aeiouAEIOU"

        l = 0
        r = len(arr) -1

        while(l<r):
            if arr[l] not in v:
                l = l+1

            elif arr[r] not in v:
                r = r-1
            
            else:
                arr[l],arr[r] = arr[r],arr[l]
                l=l+1
                r=r-1

        return "".join(arr)
        