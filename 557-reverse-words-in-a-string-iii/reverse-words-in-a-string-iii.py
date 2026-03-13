class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        words = s.split()
        for w in words:
            res.append(w[::-1])
        return " ".join(res)