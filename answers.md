# CMPS 2200 Recitation 10## Answers

**Name:**______Amara Midouhas___________________
**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)** Its O(n+m) because it runs linearly with the number of nodes and edges in the graph where O(n) represents the node and O(m) represents edges. In the while loop, each edge and and node is explored at most once so O(n+m).

- **4)** The worst case would be if it is equal to the number of nodes in the graph like if there are n amount of connected nodes and reachable had to call all n nodes to check its connectivity then that's the worst case

- **5)** The work is O(n+m). It iterates through the graph to get a starting point so O(n)(depends on size), then it calls reachable which is doing O(n+m) , then connection compares the length of reachable nodes to total number of nodes in graph so this depends on length so O(n). Since the majority of work is done in reachable so O(n+m).

- **7)** If we switched, the adjacency matrix would take up more space O(n^2) because it exemplifies all the edges between nodes even if the nodes dont exist in the actual graph. To find neighbors it will go through every column and row and check for an edge. So now reachable would be O(n^2).
