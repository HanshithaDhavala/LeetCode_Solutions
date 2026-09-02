class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0
        for num in accounts:
            maxi = max(maxi,sum(num))
        return maxi
        