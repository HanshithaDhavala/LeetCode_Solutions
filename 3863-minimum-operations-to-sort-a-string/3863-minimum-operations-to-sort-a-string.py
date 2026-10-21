class Solution:
    def minOperations(self, s: str) -> int:
        if s == ''.join(sorted(s)):
            return 0
        if len(s) == 2:
            return -1
        
        mn = min(s)
        mx = max(s)
        
        # If the minimum character is at the start (and not the whole string)
        # or the maximum character is at the end (and not the whole string)
        if s[0] == mn or s[-1] == mx:
            return 1
            
        # If no minimum character exists in any proper prefix and no maximum in any proper suffix
        if mn not in s[:-1] and mx not in s[1:]:
            return 3
            
        return 2