class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zeros = 0
        maxl = 0
        r=0
        n=len(nums)
        while r<n:
            if nums[r] == 0:
                zeros += 1
            # Shrink the window from the left until zeros <= k
            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1 
            maxl = max(maxl, r - l + 1)
            r+=1
            
        return maxl