from collections import defaultdict

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        N = len(bombs)
        
        for b1 in range(N):
            for b2 in range(b1 + 1, N):          
                x1, y1, r1 = bombs[b1]
                x2, y2, r2 = bombs[b2]
                d = sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))         
                if d <= r1:
                    graph[b1].append(b2)
                if d <= r2:
                    graph[b2].append(b1)

        # DFS to get the number of nodes reachable from a given node cur
        def dfs(bomb, visited):
            if bomb in visited:
                return 0
            visited.add(bomb)
            for neib in graph[bomb]:
                dfs(neib, visited)
            return len(visited)
        
        answer = 0
        for bomb in range(N):
            visited = set()
            answer = max(answer, dfs(bomb, visited))
        
        return answer
        