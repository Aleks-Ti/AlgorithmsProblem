class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for k in range(i + 1, len(nums)):
                if nums[i] + nums[k] == target:
                    return i, k





asd = Solution()
asd.twoSum([2,5,5,11], 10)