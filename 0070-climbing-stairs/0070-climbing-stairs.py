class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        new = 2
        old = 1
        
        for i in range(3, n + 1):
            curr = new + old
            old = new
            new = curr
            
        return new