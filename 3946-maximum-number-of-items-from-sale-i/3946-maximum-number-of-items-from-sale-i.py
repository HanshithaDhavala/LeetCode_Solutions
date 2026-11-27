class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_factor = max(item[0] for item in items)
        
        freq = [0] * (max_factor + 1)
        for f, p in items:
            freq[f] += 1
            
        multiples_count = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if freq[f] > 0:
                for multiple in range(f, max_factor + 1, f):
                    multiples_count[f] += freq[multiple]
                    
        dp = [0] * (budget + 1)
        
        for f, p in items:
            if p > budget:
                continue
            free_copies = multiples_count[f] - 1
            
            next_dp = [-1] * (budget + 1)
            for b in range(p, budget + 1):
                next_dp[b] = dp[b - p] + 1 + free_copies
                
            for b in range(2 * p, budget + 1):
                if next_dp[b - p] + 1 > next_dp[b]:
                    next_dp[b] = next_dp[b - p] + 1
                    
            for b in range(p, budget + 1):
                if next_dp[b] > dp[b]:
                    dp[b] = next_dp[b]
                    
        return max(dp)