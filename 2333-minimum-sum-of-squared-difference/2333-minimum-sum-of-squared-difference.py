from collections import Counter

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # Total operations available
        total_k = k1 + k2
        
        # Calculate absolute differences and count their frequencies
        diff_counts = Counter(abs(a - b) for a, b in zip(nums1, nums2))
        
        # Get unique differences sorted in descending order
        unique_diffs = sorted(diff_counts.keys(), reverse=True)
        
        # Greedily reduce the largest differences
        for i in range(len(unique_diffs)):
            d = unique_diffs[i]
            if d == 0:
                break
            
            count = diff_counts[d]
            # Next smaller difference level (0 if we are at the last level)
            next_d = unique_diffs[i + 1] if i + 1 < len(unique_diffs) else 0
            
            # Difference we can bridge between current level and next level
            diff_drop = d - next_d
            total_reduction_needed = diff_drop * count
            
            if total_k >= total_reduction_needed:
                # We can reduce all elements at this difference level down to next_d
                total_k -= total_reduction_needed
                diff_counts[next_d] += count
                diff_counts[d] = 0
            else:
                # We can only partially reduce elements at this level using remaining total_k
                full_steps = total_k // count
                remainder = total_k % count
                
                new_val = d - full_steps
                diff_counts[d] -= count
                diff_counts[new_val] += count - remainder
                diff_counts[new_val - 1] += remainder
                total_k = 0
                break
        
        # Calculate the final sum of squared differences
        ans = 0
        for d, count in diff_counts.items():
            if count > 0:
                ans += (d ** 2) * count
                
        Ans = ans
        return ans