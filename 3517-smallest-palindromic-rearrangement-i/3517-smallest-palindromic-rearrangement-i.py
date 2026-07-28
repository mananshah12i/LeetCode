class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)%2==0:
            w=[]
            s1=s[0:len(s)/2]
            for i in s1:
                w.append(i)
            t1="".join(sorted(w))
            t=t1+t1[-1::-1]
            return t
        else:
            w=[]
            a=s[len(s)//2]
            s1=s[0:len(s)//2]
            for i in s1:
                w.append(i)
            t1="".join(sorted(w))
            t=t1+a+t1[-1::-1]
            return t