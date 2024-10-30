#INSIGHT -> BFS vs DFS

BFS

Shortest Path / Minimum Number of Steps -> BFS explores all nodes at the present "depth" level before moving on to nodes at the next depth level, guaranteeing that the first time it reaches the target node, it has taken the shortest path.

DFS

Explore all possible paths in a graph -> particularly if you are looking for any path rather than the shortest path. It’s useful in scenarios like backtracking (e.g., solving puzzles, generating combinations or permutations).

Finding connected components in a graph, as it explores all nodes in a connected component before backtracking.

Cycle Detection -> DFS is typically used in algorithms for cycle detection in directed and undirected graphs, like in topological sorting.

BFS -> QUEUE -> BFS explores all nodes at the current level (or depth) before moving on to the nodes at the next level. The queue ensures that nodes are explored in the order they were discovered. Nodes are added to the back of the queue, and the node at the front of the queue is processed first, ensuring level-wise traversal.

DFS -> Stack or recursion -> go to all left elements recursively then visit the parent before visiting the rights. Also called in-order traversal