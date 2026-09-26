class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        l=len(str(num))
        while l!=1:
            s=0
            p=str(num)
            for i in range(l):
                s+=int(p[i])
            num=s
            l=len(str(num))
        return num
