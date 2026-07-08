class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        q = deque()
        visited = set()
        def traverse(r, c):
            if(min(r,c) < 0 or r == ROW or c == COL or
                grid[r][c] == -1 or (r,c) in visited):
                return
            q.append([r,c])
            visited.add((r,c))

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                traverse(r + 1, c)
                traverse(r - 1, c)
                traverse(r, c + 1)
                traverse(r, c - 1)
            dist += 1

