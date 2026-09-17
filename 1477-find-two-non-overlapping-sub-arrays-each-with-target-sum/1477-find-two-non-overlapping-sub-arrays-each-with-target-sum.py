class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        
        # min_len[i] stores the minimum length of a valid subarray ending at or before index i
        min_len = [float('inf')] * n
        
        ans = float('inf')
        current_sum = 0
        left = 0
        min_so_far = float('inf')
        
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink window if current_sum exceeds target
            while current_sum > target:
                current_sum -= arr[left]
                left += 1
            
            # Found a valid subarray with sum equal to target
            if current_sum == target:
                curr_len = right - left + 1
                
                # Check if there is a valid non-overlapping subarray before 'left'
                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, curr_len + min_len[left - 1])
                
                # Update minimum length found up to the current right index
                min_so_far = min(min_so_far, curr_len)
            
            min_len[right] = min_so_far
        
        return ans if ans != float('inf') else -1