from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
def bfs(graph, start_node):
    visited = set()    
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        node = queue.popleft() 
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("BFS Traversal:")
bfs(graph, 'A') 