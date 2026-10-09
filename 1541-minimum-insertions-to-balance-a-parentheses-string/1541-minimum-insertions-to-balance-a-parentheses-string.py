class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_needed = 0  # Number of ')' needed
        
        for char in s:
            if char == '(':
                # If we needed an odd number of ')', we complete the pair first
                if open_needed % 2 != 0:
                    insertions += 1
                    open_needed -= 1
                open_needed += 2
            else:  # char == ')'
                open_needed -= 1
                # Encountered unmatched ')'
                if open_needed < 0:
                    insertions += 1  # Insert '('
                    open_needed += 2  # '(' expects two ')' (one is char itself)
                    
        return insertions + open_needed