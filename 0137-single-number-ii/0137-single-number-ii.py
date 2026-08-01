class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in nums:
            d[i]=nums.count(i)
        m=d.keys()
        n=d.values()
        for i in n:
            if i==1:
                return m[n.index(i)]