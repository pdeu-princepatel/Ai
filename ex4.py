def find_blank(state):
    return state.index(0)

def get_neighbors(state):
    pos = find_blank(state)
    row, col = divmod(pos, 3)
    moves = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right
    for dr, dc in directions:
        nr, nc = row + dr, col + dc 
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_pos = nr * 3 + nc
            new_state = list(state)
            new_state[pos], new_state[new_pos] = new_state[new_pos], new_state[pos]
            moves.append(tuple(new_state))
    return moves

def distance(state, goal):
    """Heuristic function: sum of distances of tiles from goal positions."""
    distance = 0
    for i in range(9):
        tile = state[i]
        if tile != 0:
            curr_row, curr_col = divmod(i, 3)
            goal_idx = goal.index(tile)
            goal_row, goal_col = divmod(goal_idx, 3)
            distance += abs(curr_row - goal_row) + abs(curr_col - goal_col)
    return distance

def get_best_node(open_list):
    """Manually find and remove the node with the lowest f_score (f = g + h)."""
    best_idx = 0
    for i in range(1, len(open_list)):
        if open_list[i][0] < open_list[best_idx][0]:
            best_idx = i
    return open_list.pop(best_idx)

def solve_a_star(initial_str, goal_str):
    initial = tuple(map(int, initial_str.split(',')))
    goal = tuple(map(int, goal_str.split(',')))
    
    if len(initial) != 9 or len(goal) != 9:
        return "Invalid input length", -1

    h_score = distance(initial, goal)
    open_list = [[h_score, 0, initial]]
    
    parent_map = {initial: None}
    g_score = {initial: 0}
    
    while open_list:
        f, cost, curr = get_best_node(open_list)
        
        if curr == goal:
            path = []
            while curr is not None:
                path.append(curr)
                curr = parent_map[curr]
            return path[::-1], cost

        for neighbor in get_neighbors(curr):
            new_g = cost + 1
            
            if neighbor not in g_score or new_g < g_score[neighbor]:
                g_score[neighbor] = new_g
                f_score = new_g + distance(neighbor, goal)
                parent_map[neighbor] = curr
                open_list.append([f_score, new_g, neighbor])
    return None, -1

def print_path(path):
    for i, state in enumerate(path):
        print(f"Step {i}:")
        for r in range(3):
            print(' '.join(map(str, state[r*3:(r+1)*3])))
        print("-" * 10)

if __name__ == "__main__":
    print("Enter initial state (9 numbers 0-8 comma-separated, 0=blank):")
    i_str = input().strip()
    print("Enter goal state (9 numbers 0-8 comma-separated):")
    g_str = input().strip()
    
    path, steps = solve_a_star(i_str, g_str)
    
    if path:
        print(f"\nSolution found in {steps} steps!")
        print_path(path)
    else:
        print("\nNo solution found.")
