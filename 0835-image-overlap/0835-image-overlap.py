class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        
        # 1. Extract coordinates of all 1s in both matrices
        p1 = []
        p2 = []
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    p1.append((r, c))
                if img2[r][c] == 1:
                    p2.append((r, c))
        
        # 2. Count frequencies of transformation vectors
        shifts = {}
        max_overlap = 0
        
        for r1, c1 in p1:
            for r2, c2 in p2:
                vec = (r2 - r1, c2 - c1)
                shifts[vec] = shifts.get(vec, 0) + 1
                if shifts[vec] > max_overlap:
                    max_overlap = shifts[vec]
                    
        return max_overlap