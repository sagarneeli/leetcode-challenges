class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        dirs = [[-1, 1], [1, -1], [0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1]]
        start = (0, 0)
        visited = set([start])
        queue = deque([start])
        length = 1
        m, n = len(grid), len(grid[0])
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == m - 1 and c == n - 1:
                    return length
                
                for x, y in dirs:
                    rx, ry = r + x, c + y
                    if 0 <= rx < m and 0 <= ry < n and (rx, ry) not in visited and grid[rx][ry] == 0:
                        queue.append((rx, ry))
                        visited.add((rx, ry))
            
            length += 1
                
        return -1
        