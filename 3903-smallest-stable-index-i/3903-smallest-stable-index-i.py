class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            pre_max = max(nums[:i + 1])
            suf_min = min(nums[i:]) 
            if pre_max - suf_min <= k:
                return i        
        return -1