from collections import deque
from math import gcd

def possible(a,b,x,y):
    return [
        (a,y),
        (x,b),
        (0,y),
        (x,0),
        (x -min(x,b-y) ,y +min(x,b-y)),
        (x +min(y,a-x) ,y-min(y,a-x))
    ]

def w_bfs(a,b,c):
    if c > max(a,b) or c % gcd(a,b) !=0:
        return None
    start = (0,0)
    visited ={start}
    queue = deque([(0,0,[start])])
    while queue:
        x,y,history = queue.popleft()

        if x == c or y == c:
            return history
        
        for nx,ny in possible(a,b,x,y):
            if (nx,ny) not in visited:
                visited.add((nx,ny))
                queue.append((nx,ny,history+[(nx,ny)]))
    return None

def w_dfs(a,b,c):
    if c > max(a,b) or c % gcd(a,b) !=0:
        return None
    start = (0,0)
    visited ={start}
    stack = [(0,0,[start])]
    while stack:
        x,y,history = stack.pop()
        
        if x==c or y==c:
            return history
        for nx,ny in possible(a,b,x,y):
            if (nx,ny) not in visited:
                visited.add((nx,ny))
                stack.append((nx,ny,history+[(nx,ny)]))
    return None

a = int(input("Enter the Jug1 capacity:"))
b = int(input("Enter the Jug2 capacity:"))
c = int(input("Enter the Target:"))


bfs =  w_bfs(a,b,c)
if bfs:
    print("BFS Path to reach goal:")
    for step in bfs:
        print(step)
else:
    print("No solution possible.")


dfs =  w_dfs(a,b,c)
if dfs:
    print("DFS Path to reach goal:")
    for step in dfs:
        print(step)
else:
    print("No solution possible.")