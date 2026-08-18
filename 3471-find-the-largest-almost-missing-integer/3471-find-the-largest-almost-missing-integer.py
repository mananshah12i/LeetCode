class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m=-1
        d={}
        for i in range(len(nums)):
            if i+k<=len(nums):
                l=nums[i:i+k]
                for j in l:
                    if j in d:
                        d[j]+=1
                    else:
                        d[j]=1
        print(d)
        e=d.values()
        f=d.keys()
        for i in range(len(e)):
            if e[i]==1 and f[i]>m:
                m=f[i]
        if len(nums)==k:
            return max(f)
        else:
            return m