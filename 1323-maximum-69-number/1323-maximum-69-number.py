class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        s=str(num)
        i=s.find('6')
        if i>=0:
            return int(s[0:i]+'9'+s[i+1::])
        else:
            return num