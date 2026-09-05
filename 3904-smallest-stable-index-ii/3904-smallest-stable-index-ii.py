class Solution:

    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Precompute suffix minimums
        suff_min = [0] * n
        suff_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])

        # Track prefix maximum and check stability score
        pref_max = float("-inf")
        for i in range(n):
            pref_max = max(pref_max, nums[i])
            instability_score = pref_max - suff_min[i]

            if instability_score <= k:
                return i

        return -1