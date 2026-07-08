class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        visited = [False] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(ndoe):
            for neighbor in adj[ndoe]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)
        res = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                res += 1
        return res