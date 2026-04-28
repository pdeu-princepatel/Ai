def get_neighbors(state):
    pos = state.index(0)
    row,col = divmod(pos,3)
    moves =[]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for dr , dc in directions:
        nr, nc = row+dr,col+dc
        if 0<=nr<3 and 0<=nc<3:
            new_pos = nr*3 +nc
            new_state =list(state)
            new_state[pos], new_state[new_pos] = new_state[new_pos], new_state[pos]
            moves.append(tuple(new_state))
    return moves
    
# manhatten distance for heuristics
def disatnce(state,goal):
    distance =0
    for i in range(9):
        tile = state[i]
        if tile != 0:
            cr ,cc =divmod(i,3)
            gi = goal.index(tile)
            gr,gc = divmod(gi,3)
            distance += abs(cr-gr) + abs(cc-gc)
    return distance

# fn lowest value output
def best_node(open_list):
    besti = 0
    for i in range(1,len(open_list)):
        if open_list[i][0] < open_list[besti][0]:
            besti = i
    return open_list.pop(besti)

def solve(intial_str,goal_str):
    initial = tuple(map(int,intial_str.split(' ')))
    goal = tuple(map(int,goal_str.split(' ')))
    
    if len(initial) != 9 or len(goal) != 9 or sorted(initial) != [0,1,2,3,4,5,6,7,8]:
        return "invalid input"

    h_score = disatnce(initial,goal)
    open_list = [[h_score,0,initial]]
    parent_map = {initial:None}
    g_score = {initial:0}

    while open_list:
        f,cost,curr = best_node(open_list)

        if curr == goal:
            path =[]
            while curr is not None:
                path.append(curr)
                curr = parent_map[curr]
            return path[::-1],cost

        for neighbor in get_neighbors(curr):
            new_g = cost + 1

            if neighbor not in g_score or new_g < g_score[neighbor]:
                g_score[neighbor] = new_g
                f_score = new_g + disatnce(neighbor,goal)
                parent_map[neighbor] = curr
                open_list.append([f_score,new_g,neighbor])
    return None,-1

def print_path(path):
    for i,state in enumerate(path):
        print(f"step{i}:")
        for r in range(3):
            print(' '.join(map(str,state[r*3:(r+1)*3])))
        print()

print_path(solve("0 1 2 3 4 5 6 7 8", "8 7 6 5 4 3 2 1 0")[0])
