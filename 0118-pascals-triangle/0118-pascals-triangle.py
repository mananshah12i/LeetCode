class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        if numRows>2:
            n=2
            l = [[1],[1,1]]
            while n!=numRows:
                m=[1]
                for i in range(len(l[-1])-1):
                    m.append(l[-1][i]+l[-1][i+1])
                m.append(1)
                l.append(m)
                n+=1
            return l
