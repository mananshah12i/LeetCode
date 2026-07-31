class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        if rowIndex>1:
            n=1
            l = [[1],[1,1]]
            while n!=rowIndex:
                m=[1]
                for i in range(len(l[-1])-1):
                    m.append(l[-1][i]+l[-1][i+1])
                m.append(1)
                l.append(m)
                n+=1
            return l[rowIndex]