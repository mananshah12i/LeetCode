class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        d={}
        l=[]
        c=0
        ans=""
        for i in range(numRows):
            d[i]=[]
        while c!=numRows:
            l.append(c)
            c+=1
        c-=1
        while c!=0:
            c-=1
            l.append(c)
        if len(l)!=1:
            l.pop(-1)
        x=l*(len(s))
        for j in range(len(x)-len(s)):
            x.pop()
        for k in range(len(x)):
            d[x[k]].append(s[k])
        for m in d:
            for n in d[m]:
                ans+=n
        return ans