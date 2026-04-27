from collections import deque

def bfs(graph, src, target):
    if src == target:
        return [src]
    
    q = deque()
    q.append([src])
    seen = set()

    while q:
        current_path = q.popleft()
        last = current_path[-1]

        if last in seen:
            continue
        seen.add(last)

        for adj in graph.get(last, []):
            path = current_path + [adj]
            if adj == target:
                return path
            q.append(path)

    return None


def dfs(graph, src, target, path=None, seen=None):
    if path is None:
        path = [src]
    if seen is None:
        seen = set()

    if src == target:
        return path

    seen.add(src)

    for adj in graph.get(src, []):
        if adj not in seen:
            found = dfs(graph, adj, target, path + [adj], seen)
            if found:
                return found

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['G'],
    'G': []
}

s = input("Enter the source node (S): ").upper()
g = input("Enter the goal node (G): ").upper()

bfs_path = bfs(graph, s, g)
dfs_path = dfs(graph, s, g)

print(f"\nBFS Path: {bfs_path}")
print(f"DFS Path: {dfs_path}")