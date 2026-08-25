class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        x=max(nums)
        y=(x-x%k)/k
        for i in range(1,y+1):
            if i*k not in nums:
                return i*k
        return k*(y+1)