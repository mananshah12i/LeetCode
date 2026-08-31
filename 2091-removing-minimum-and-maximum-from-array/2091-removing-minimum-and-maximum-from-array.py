class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=nums.index(max(nums))
        n=nums.index(min(nums))
        if m>n:
            return min([m+1, len(nums)-n, n+1+len(nums)-m])
        else:
            return min([n+1, len(nums)-m, m+1+len(nums)-n])