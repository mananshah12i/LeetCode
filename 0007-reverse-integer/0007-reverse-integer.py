class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>0:
            w=str(x)
            z=w[-1::-1]
            if int(z)>((2**31)-1):
                return 0
            else:
                return int(z)
        elif x<0:
            w=str(-x)
            z=w[-1::-1]
            if -(int(z))<-(2**31):
                return 0
            else:
                return -(int(z))
        else:
            return 0