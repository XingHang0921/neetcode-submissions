class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROW, COL = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= ROW or c < 0 or c >= COL or grid[r][c] != 1: return 0
            grid[r][c] = -1
            area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            return area
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res