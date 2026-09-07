class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        # Stores the count of distinct subsequences ending with each character 'a'-'z'
        last = [0] * 26
        
        for char in s:
            idx = ord(char) - ord('a')
            # New count for char is (sum of all current subsequences + 1 for char itself)
            last[idx] = (sum(last) + 1) % MOD
            
        return sum(last) % MOD