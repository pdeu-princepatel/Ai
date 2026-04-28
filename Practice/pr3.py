from collections import deque

def get_neighbour(state):
    pos = state.index(0)
    row,col = divmod(pos,3) # or pos//3,pos%3
    moves =[]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for dr,dc in directions:
        nr,nc = row+dr,col+dc
        if 0<= nr < 3 and 0<= nc<3:
            new_pos = nr*3+nc
            new_state = state[:]
            new_state[pos], new_state[new_pos] = new_state[new_pos], new_state[pos]
            moves.append(new_state)
    return moves

def print_path(path):
    for i,state in enumerate(path):
        print(f"step{i}:")
        for r in range(3):
            print(' '.join(map(str,state[r*3:(r+1)*3])))
        print()

def solve(initial_str,goal_str,method):
    initial = list(map(int,initial_str.split(' ')))
    goal = list(map(int,goal_str.split(' ')))

    if len(initial) != 9 or len(goal) != 9 or sorted(initial) != [0,1,2,3,4,5,6,7,8]:
        return "invalid input"
    
    if method.lower() == 'bfs':
        queue = deque([(initial,0,None)])
        visited = set()
        visited.add(tuple(initial))
        parent_map = {}

        while queue:
            state,steps,parent = queue.popleft()
            if state == goal:
                path = []
                current = state
                while current is not None:
                    path.append(current)
                    current = parent_map.get(tuple(current))
                path.reverse()
                return path,steps
            for neighbor in get_neighbour(state):
                nt = tuple(neighbor)
                if nt not in visited:
                    visited.add(nt)
                    parent_map[nt] = tuple(state)
                    queue.append((neighbor,steps+1,tuple(state)))

    elif method.lower() =='dfs':
        stack = [(initial,0,None)]
        visited = set()
        visited.add(tuple(initial))
        parent_map ={}
        
        while stack:
            state,steps,parent=stack.pop()
            if state == goal:
                path =[]
                current = state
                while current is not None:
                    path.append(current)
                    current = parent_map.get(tuple(current))
                return path, steps
            
            for neighbor in get_neighbour(state):
                nt = tuple(neighbor)
                if nt not in visited:
                    visited.add(nt)
                    parent_map[nt] = tuple(state)
                    stack.append((neighbor,steps+1,tuple(state)))

    return None,-1

print(solve("0 1 2 3 4 5 6 7 8", "8 7 6 5 4 3 2 1 0", 'bfs')[1])
print(solve("0 1 2 3 4 5 6 7 8", "8 7 6 5 4 3 2 1 0", 'dfs')[1])