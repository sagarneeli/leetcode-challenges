class Solution:
    def minJumps(self, arr: List[int]) -> int:
        """
        1. Build Graph
        2. Run BFS
        """
        min_steps = 0
        n = len(arr)
        if n <= 1:
            return min_steps
        
        graph = defaultdict(list)
        
        for i, val in enumerate(arr):
            graph[val].append(i)
            
        queue = deque([0])
        visited = {0}
        
        while queue:
            nex = []

            # iterate the layer
            for node in queue:
                # check if reached end
                if node == n - 1:
                    return min_steps

                # check same value
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)

                # clear the list to prevent redundant search
                graph[arr[node]].clear()

                # check neighbors
                for child in [node-1, node+1]:
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)

            queue = nex
            min_steps += 1
            
        return min_steps
            
        