class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        st = [] 
        for ch in path.split("/"):
            if ch == '' or ch == '.':
                continue
            elif ch == '..':
                if st:
                    st.pop()
            else:
                st.append(ch)
        return "/" + "/".join(st)
        