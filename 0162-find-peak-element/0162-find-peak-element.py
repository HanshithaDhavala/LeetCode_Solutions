class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        ans  = max(nums)
        idx = nums.index(ans)
        return idx
        