class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        l=s.split()
        d={}
        t=[]
        q=[]
        if len(pattern)==len(l):
            for i in range(len(l)):
                if (pattern[i],l[i]) not in d.items() and pattern[i] not in d.keys():
                    d[pattern[i]]=l[i]
            for j in pattern:
                t.append(d[j])
            for k in d.values():
                if k not in q:
                    q.append(k)
            if t==l and len(d.keys())==len(q):
                return True
            else:
                return False
        else:
            return False