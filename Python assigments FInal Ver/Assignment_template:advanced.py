def relationship_status(from_member, to_member, social_graph):
    if to_member in social_graph.get(from_member, {}).get("following", []):
        if from_member in social_graph.get(to_member, {}).get("following", []):
            return "friends"
        return "followed by"
    elif from_member in social_graph.get(to_member, {}).get("following", []):
        return "follower"
    return "no relationship"

def tic_tac_toe(board):
    size = len(board)
    # Check rows
    for i in range(size):
        if len(set(board[i])) == 1 and board[i][0] != "":
            return board[i][0]
    # Check columns
    for i in range(size):
        if len(set([board[j][i] for j in range(size)])) == 1 and board[0][i] != "":
            return board[0][i]
    # Check diagonals
    if len(set([board[i][i] for i in range(size)])) == 1 and board[0][0] != "":
        return board[0][0]
    if len(set([board[i][size - 1 - i] for i in range(size)])) == 1 and board[0][size - 1] != "":
        return board[0][size - 1]
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    total_time = 0
    current_stop = first_stop
    while current_stop != second_stop:
        key = (current_stop, route_map[current_stop])
        total_time += route_map[key]["travel_time_mins"]
        current_stop = route_map[current_stop]
    return total_time
