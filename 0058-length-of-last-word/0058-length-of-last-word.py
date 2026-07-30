class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1=s.strip()
        if len(s1)>1 and s1.count(" ")>0:
            s2=[]
            for i in range(len(s1)-1, -1, -1):
                s2.append(s1[i])
            return s2.index(' ')
        else:
            return len(s1)