class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        p=sorted(s)
        q=sorted(t)
        for i in q:
            if i in p:
                p.remove(i)
            else:
                return i