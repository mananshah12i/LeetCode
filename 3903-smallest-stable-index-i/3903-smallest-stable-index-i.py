class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        x=0
        y=1
        for i in range(len(nums)):
            if max(nums[0:y])-min(nums[x::])<=k:
                return i
            x+=1
            y+=1
        return -1