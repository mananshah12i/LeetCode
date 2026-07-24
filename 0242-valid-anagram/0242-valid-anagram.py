class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        r=True
        for i in s:
            if i not in t:
                r=False
                break
            elif s.count(i)!=t.count(i):
                r=False
                break
        for j in t:
            if j not in s:
                r=False
                break
            elif s.count(i)!=t.count(i):
                r=False
                break
        if len(s)!=len(t):
            r=False
        return r
            