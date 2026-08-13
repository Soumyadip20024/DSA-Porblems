class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        freq = [0]*26

        for ch in s:
            freq[ord(ch) - ord('a')] = freq[ord(ch) - ord('a')] +1

        for i in range(n):
            ch = s[i]
            if freq[ord(ch) - ord('a')] == 1:
                return i
        return -1


        