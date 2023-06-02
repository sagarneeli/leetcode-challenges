# Intuition
- Recursive - because one bomb sets off another and the other bomb can set off multiple different bombs.
- Graph problem + Directed (because it depends on the blast radius)
# Approach
1. Build an adjacency list and for each node and determine which bombs it can set off and add them as neighbors i.e bomb -> [list of bombs it can detonate]
2. Then run DFS or BFS graph algorithm
3. Every source bomb
# Complexity
## Time complexity:
O(n^3 )
## Space complexity:
O(n^2 )