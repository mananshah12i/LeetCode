class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        p = 1
        su = 0
        s = str(n)

        for i in s:
            su += int(i)
            p *= int(i)

        if n % (su + p) == 0:
            return True
        else:
            return False