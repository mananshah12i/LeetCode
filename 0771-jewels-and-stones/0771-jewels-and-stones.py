class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        n=0
        for i in jewels:
            n+=stones.count(i)
        return n