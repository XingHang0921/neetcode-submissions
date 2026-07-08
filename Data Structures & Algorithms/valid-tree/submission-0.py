class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)} ##place holder for hashmap

        for e, v in edges:          ##building the connection hashmap for the nodes
            adj[e].append(v)
            adj[v].append(e)
        
        visited = set()     
        def dfs(i, prev):
            if i in visited:        ##check if already visited if so False
                return False
            
            visited.add(i)          ##add to visited
            for nei in adj[i]:          ##for each neighbor associated check if neighbor was visited
                if nei == prev:        ##as well except the previous spot
                    continue
                if not dfs(nei,i):
                    return False
            return True     ##otherwise true
        return dfs(0, -1) and n == len(visited) ##last case we need to make sure the graph is all
        ##connected