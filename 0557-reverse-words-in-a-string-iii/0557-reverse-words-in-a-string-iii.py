class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        p=""
        for i in s.split():
            p+=i[-1::-1]+" "
        return p.strip()