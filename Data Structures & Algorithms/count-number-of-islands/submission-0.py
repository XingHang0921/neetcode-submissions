class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res = 0
        visited = set()
        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= len(grid) or c >= len(grid[0]) or
                grid[r][c] == '0' or
                (r,c) in visited):
                return 

            visited.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c) 
            dfs(r, c + 1)
            dfs(r, c - 1)
        for r in range(0,len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    res += 1
        return res