class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        l, r = 0, k - 1
        sum = 0
        for i in range(l, r + 1):
            sum += nums[i]
        maxi = sum
        while r < n - 1:
            sum -= nums[l]
            l += 1
            r += 1
            sum += nums[r]
            maxi = max(maxi, sum)
        avg = maxi/k
        return avg
        