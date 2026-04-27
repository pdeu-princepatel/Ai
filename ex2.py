from collections import deque
from math import gcd

def possible_states(x, y, cap_x, cap_y):
    return [
        (cap_x, y),
        (x, cap_y),
        (0, y),
        (x, 0),
        (x - min(x, cap_y - y), y + min(x, cap_y - y)),
        (x + min(y, cap_x - x), y - min(y, cap_x - x))
    ]

def water_jug_bfs(cap_x, cap_y, goal):
    if goal > max(cap_x, cap_y) or goal % gcd(cap_x, cap_y) != 0:
        return None

    start = (0, 0)
    visited = {start}
    queue = deque([(0, 0, [start])])

    while queue:
        x, y, history = queue.popleft()

        if x == goal or y == goal:
            return history

        for nx, ny in possible_states(x, y, cap_x, cap_y):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, history + [(nx, ny)]))

    return None


def water_jug_dfs(cap_x, cap_y, goal):
    if goal > max(cap_x, cap_y) or goal % gcd(cap_x, cap_y) != 0:
        return None

    start = (0, 0)
    visited = {start}
    stack = [(0, 0, [start])]

    while stack:
        x, y, history = stack.pop()

        if x == goal or y == goal:
            return history

        for nx, ny in possible_states(x, y, cap_x, cap_y):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                stack.append((nx, ny, history + [(nx, ny)]))

    return None


m = int(input("Enter capacity of Jug 1: "))
n = int(input("Enter capacity of Jug 2: "))
y = int(input("Enter target amount: "))

result = water_jug_bfs(m, n, y)
if result:
    print("BFS Path to reach goal:")
    for step in result:
        print(step)
else:
    print("No solution possible.")

m_dfs = int(input("Enter capacity of Jug 1: "))
n_dfs = int(input("Enter capacity of Jug 2: "))
y_dfs = int(input("Enter target amount: "))

result = water_jug_dfs(m_dfs, n_dfs, y_dfs)
if result:
    print("DFS Path to reach goal:")
    for step in result:
        print(step)
else:
    print("No solution possible.")