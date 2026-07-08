class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW,COL = len(grid), len(grid[0])
        visited = set()
        q = deque()
        def bfs(r, c):
            if (r == ROW or c == COL or min(r,c) < 0 or
                (r, c) in visited or grid[r][c] == -1):
                return
            visited.add((r,c))
            q.append([r,c])
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r,c))
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)
            dist += 1