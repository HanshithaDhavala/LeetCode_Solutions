class Solution:
    def maxPower(self, s: str) -> int:
        max_len = 1
        current_len = 1 
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current_len += 1
            else:
                max_len = max(max_len, current_len)
                current_len = 1
                
        return max(max_len, current_len)