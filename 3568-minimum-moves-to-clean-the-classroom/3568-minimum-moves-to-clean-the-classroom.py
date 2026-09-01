from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])
        # Find start and give each litter an index
        start_r = start_c = 0
        litter_id = {}
        count = 0
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = count
                    count += 1
        if count == 0:
            return 0
        full_mask = (1 << count) - 1
        # best[r][c][mask] = maximum energy seen
        best = [[[-1] * (1 << count) for _ in range(n)]
                for _ in range(m)]
        q = deque()
        q.append((start_r, start_c, energy, 0))
        best[start_r][start_c][0] = energy
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        moves = 0
        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()
                if mask == full_mask:
                    return moves
                if e == 0:
                    continue
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if classroom[nr][nc] == 'X':
                        continue
                    # Moving costs 1 energy
                    ne = e - 1
                    new_mask = mask
                    # Collect litter
                    if classroom[nr][nc] == 'L':
                        bit = litter_id[(nr, nc)]
                        new_mask |= (1 << bit)
                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        ne = energy
                    # If we've already reached this state
                    # with MORE energy, don't visit again
                    if ne <= best[nr][nc][new_mask]:
                        continue
                    best[nr][nc][new_mask] = ne
                    q.append((nr, nc, ne, new_mask))
            moves += 1
        return -1