class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r1=[nums[0]]
        r2=[nums[1]]
        for i in range(2, len(nums)):
            if r1[-1]>r2[-1]:
                r1.append(nums[i])
            else:
                r2.append(nums[i])
        return r1+r2