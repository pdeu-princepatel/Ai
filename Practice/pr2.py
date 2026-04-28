from collections import deque
from math import gcd
# jug1,jug2 == capacitys
#a,b =initial/intermediate state

def possible_steps(jug1,jug2,a,b):
    return[
        # completely filled
        (jug1,b),
        (a,jug2),
        # empty one
        (0,b),
        (a,0),
        # transfer
        ((a-min(a,jug2-b)),(b+min(a,jug2-b))),
        ((a+min(jug1-a ,b)),(b-min(jug1-a,b))),
    ]


def is_solvable(jug1,jug2,target):
    if max(jug1,jug2) >= target:
        if target % gcd(jug1,jug2) == 0:
            return True
    return False 

def bfs(jug1,jug2,target):
    if not is_solvable(jug1,jug2,target):
        return "Not Possible"
    start =(0,0)
    queue =deque([(0,0,[start])])
    visited =set([start])
    
    while queue:
        a,b,path= queue.popleft()
        
        if a == target or b == target:
            return path
        
        for na,nb in possible_steps(jug1,jug2,a,b):
            if (na,nb) not in visited:
                visited.add((na,nb))
                queue.append((na,nb,path+[(na,nb)]))
    return None

def dfs(jug1,jug2,target):
    if not is_solvable(jug1,jug2,target):
        return "Not Possible"
    start = (0,0)
    visited =set([start])
    stack = [(0,0,[start])]

    while stack:
        a,b,path = stack.pop()

        if a==target or b==target:
            return path
        
        for na,nb in possible_steps(jug1,jug2,a,b):
            if (na,nb) not in visited:
                visited.add((na,nb))
                stack.append((na,nb,path+[(na,nb)]))
    return None

print("BFS path:", bfs(10,2,6))
print("DFS path:", dfs(10,2,8))