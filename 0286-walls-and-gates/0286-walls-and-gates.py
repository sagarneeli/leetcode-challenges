class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        1. Some sort of traversal
        2. BFS - hint nearest gate
        3. INF - not reachable gate
        4. 0 - Gate
        
        ALGO
        1. Identify the gates in the grid
        2. From each gate, RUN a BFS algo
        3. For each determine the lowest value between the current value and calculated value
        """         
        m, n = len(rooms), len(rooms[0])
        queue = deque([])
        EMPTY = 2147483647
        GATE = 0
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                    
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    queue.append([r, c])
        while queue:
            row, col = queue.popleft()
            for dr, dc in dirs:
                r, c = row + dr, col + dc
                if 0 <= r < len(rooms) and 0 <= c < len(rooms[0]) and rooms[r][c] == EMPTY:
                    rooms[r][c] = rooms[row][col] + 1
                    queue.append([r, c])
                        
            
        
        