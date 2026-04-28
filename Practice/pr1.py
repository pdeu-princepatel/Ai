from collections import deque

graph =  {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': ['G'], 'F': [], 'G': []
}

def bfs(start,goal):
    queue = deque([(start,[start])])
    visited = set([start])

    while queue:
        node,path = queue.popleft()
        
        if node == goal:
            return path
        
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour,path+[neighbour]))
    return None

def dfs(start,goal,visited =None,path=None):
        if visited is None : visited = set()
        if path is None : path =[]

        visited.add(start)
        path = path +[start]

        if start == goal:
            return path
        
        for neighbour in graph[start]:
            if neighbour not in visited:
                result = dfs(neighbour,goal,visited,path)
                if result: return result       
        return None


print("BFS path:", bfs('A', 'G'))
print("DFS path:", dfs( 'A', 'G'))