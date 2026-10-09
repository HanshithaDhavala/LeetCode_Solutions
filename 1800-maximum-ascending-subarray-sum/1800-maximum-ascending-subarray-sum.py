class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        maxi = nums[0]
        curr = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                curr += nums[i]
            else:
                curr = nums[i]
            maxi = max(curr,maxi)
        return maxi        