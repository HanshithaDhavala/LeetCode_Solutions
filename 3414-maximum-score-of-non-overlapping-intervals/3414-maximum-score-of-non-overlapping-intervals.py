from bisect import bisect_right
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # Store (l, r, weight, original_index)
        n = len(intervals)
        arr = sorted([(l, r, w, i) for i, (l, r, w) in enumerate(intervals)], key=lambda x: x[1])
        
        rights = [x[1] for x in arr]
        
        # dp[k][i] = (max_score, tuple_of_sorted_indices)
        # Using 4 intervals max
        dp = [[(0, ())] * (n + 1) for _ in range(5)]
        
        for i in range(1, n + 1):
            l, r, w, idx = arr[i - 1]
            
            # Find largest index j such that rights[j - 1] < l
            j = bisect_right(rights, l - 1)
            
            for k in range(1, 5):
                # Option 1: Skip current interval
                op1_score, op1_indices = dp[k][i - 1]
                
                # Option 2: Take current interval
                prev_score, prev_indices = dp[k - 1][j]
                op2_score = prev_score + w
                op2_indices = tuple(sorted(prev_indices + (idx,)))
                
                # Pick the choice with maximum score, break ties lexicographically
                if op2_score > op1_score:
                    dp[k][i] = (op2_score, op2_indices)
                elif op2_score == op1_score:
                    if not op1_indices or op2_indices < op1_indices:
                        dp[k][i] = (op2_score, op2_indices)
                    else:
                        dp[k][i] = (op1_score, op1_indices)
                else:
                    dp[k][i] = (op1_score, op1_indices)
                    
        # Find the best result across using up to 4 intervals
        best_score = -1
        best_indices = ()
        
        for k in range(1, 5):
            score, indices = dp[k][n]
            if score > best_score:
                best_score = score
                best_indices = indices
            elif score == best_score:
                if not best_indices or indices < best_indices:
                    best_indices = indices
                    
        return list(best_indices)