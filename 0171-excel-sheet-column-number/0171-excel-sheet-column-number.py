class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        d={}
        m=1
        n=0
        for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            d[i]=m
            m+=1
        l=d.values()
        for j in range(-1, -(len(columnTitle))-1, -1):
            if j==-1:
                n+=d[columnTitle[-1]]
            if j==-2:
                n+=26*d[columnTitle[-2]]
            if j==-3:
                n+=26*26*d[columnTitle[j]]
            if j==-4:
                n+=26*26*26*d[columnTitle[j]]
            if j==-5:
                n+=26*26*26*26*d[columnTitle[j]]
            if j==-6:
                n+=26*26*26*26*26*d[columnTitle[j]]
            if j==-7:
                n+=26*26*26*26*26*26*d[columnTitle[j]]
        return n