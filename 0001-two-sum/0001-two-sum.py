class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            j=nums.index(i)
            nums[nums.index(i)]=(2**9)+1
            if target-i in nums:
                return[j,nums.index(target-i)]
