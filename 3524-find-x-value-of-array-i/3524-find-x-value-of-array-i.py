class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        # dp[r] will store the number of valid subarrays ending at the previous index with product % k == r
        dp = [0] * k
        
        for num in nums:
            rem = num % k
            next_dp = [0] * k
            
            # Start a new subarray consisting of just the current element
            next_dp[rem] += 1
            
            # Extend existing subarrays ending at the previous element
            for prev_rem in range(k):
                if dp[prev_rem] > 0:
                    new_rem = (prev_rem * rem) % k
                    next_dp[new_rem] += dp[prev_rem]
            
            dp = next_dp
            
            # Add counts of subarrays ending at current index to the total answer
            for r in range(k):
                ans[r] += dp[r]
                
        return ans