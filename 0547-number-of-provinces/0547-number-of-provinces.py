class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def dfs(i):
            if visited[i]:
                return
            
            visited[i] = 1
            for j in range(n):
                if M[i][j] == 1:
                    dfs(j)
            
        n = len(M)
        count = 0
        visited = [0] * n
        for i in range(n):
            # Not in visited
            if visited[i] == 0:
                dfs(i)
                count += 1
                
        return count
        