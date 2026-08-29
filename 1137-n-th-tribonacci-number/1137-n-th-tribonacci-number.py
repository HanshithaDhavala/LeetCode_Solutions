class Solution:
    def tribonacci(self, n: int) -> int:
        F = [0]*38 
        F[0] = 0
        F[1] = 1
        F[2] = 1
        for i in range(n-2):
            F[i+3] = F[i] + F[i+1] + F[i+2]
        return F[n]


        