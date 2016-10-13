import copy

class Node:
    def __init__(self, state, action, move_type):
        self.state = state
        self.action = action
        self.move_type = move_type


def minMaxDecision(state, player):
    list_of_utility_score = []
    # v = max_value(state, player, 0)
    if player == "X":
        nextPlayer = "O"
    else:
        nextPlayer = "X"
    Successors = get_successors_of_current_state(state, player)
    for s in Successors:
        list_of_utility_score.append(minMaxValue(s.state, nextPlayer, 1))

    v = max(list_of_utility_score)
    index = list_of_utility_score.index(v)
    # print("Result  : ")
    # print(list_of_utility_score)
    # print(Successors[index].state)
    # print(Successors[index].action)
    # print("XOXO")
    return Successors[index]

def minMaxValue(state, player, depth):
    current_depth = copy.deepcopy(depth)
    current_player = copy.deepcopy(player)
    current_state = copy.deepcopy(state)
    if current_player == "X":
        nextPlayer = "O"
    elif current_player == "O":
        nextPlayer = "X"

    if (terminal_test(current_state, current_depth)):
        return utility(current_state, current_player)
    elif current_player == globalplayer:
        v = -float('inf')
        Successors = get_successors_of_current_state(state, current_player)
        for s in Successors:
            v = max(v, minMaxValue(s.state, nextPlayer, current_depth + 1))

    else:
        v = float('inf')
        Successors = get_successors_of_current_state(state, current_player)
        for s in Successors:
            v = min(v, minMaxValue(s.state, nextPlayer, current_depth + 1))
    return v
#
# def max_value(state, player, depth, alpha, beta):
#     current_depth = copy.deepcopy(depth)
#     current_player = copy.deepcopy(player)
#     if (terminal_test(state, current_depth)):
#         return utility(state, current_player)
#     #v = -float('inf')
#     Successors = get_successors_of_current_state(state, current_player)
#     if current_player == "X":
#         nextPlayer = "O"
#     elif current_player == "O":
#         nextPlayer = "X"
#     for s in Successors:
#         alpha = max(v, min_value(s.state,nextPlayer, current_depth+1,  alpha, beta))
#         if alpha >= ft:
#           return ft
#     # print("Max : At depth ", end="");
#     # print(depth, end="")
#     # print(v)
#     return alpha
#
# def min_value(state, player, depth, alpha, ft):
#     current_depth = copy.deepcopy(depth)
#     current_player = copy.deepcopy(player)
#     if (terminal_test(state, current_depth)):
#         return utility(state, current_player)
#     #v = float('inf')
#     Successors = get_successors_of_current_state(state, current_player)
#     if current_player == "X":
#         nextPlayer = "O"
#     elif current_player == "O":
#         nextPlayer = "X"
#     for s in Successors:
#         ft = min(v, max_value(s.state, nextPlayer, current_depth+1, alpha, beta))
#         if ft < alpha:
#           return alpha
#     print("Min : At depth ", end="");
#     print(depth, end="")
#     print(v)
#     return alpha

def utility(state,player):
    sumX = 0
    sumO = 0
    utility_score = 0
    for i in range(int(n)):
        for j in range(int(n)):
            if state[i][j] == "X":
                sumX = sumX + int(cell_values[i][j])
            elif state[i][j] == "O":
                sumO = sumO + int(cell_values[i][j])
    if globalplayer == "X":
        utility_score = sumX - sumO
    else:
        utility_score = sumO - sumX

    # print(utility_score, end="")
    # print(" ====> ", end="")
    # print(state)

    return utility_score

def terminal_test(state, current_depth):
    isTerminal = False;
    if(current_depth >= int(cutting_depth) - 0):
        isTerminal = True
    else:
        for i in range(int(n)):
            for j in range(int(n)):
                if(state[i][j] == '.'):
                    isTerminal = False
                    return isTerminal
    return isTerminal

def check(row, col, state, player):
    if row < 0 or col < 0 or col >= int(n) or row >= int(n):
        return 0
    elif state[row][col] == player:
        return 1
    else:
        return 0

def isRaid(row, col, current_state, player):
    a = check(row, col + 1, current_state, player)
    b = check(row + 1, col, current_state, player)
    c = check(row - 1, col, current_state, player)
    d = check(row, col - 1, current_state, player)
    if a == 1 or b == 1 or c == 1 or d == 1:
        return True
    else:
        return False

def get_successors_of_current_state(state, player):
    successors = []
    for i in range(int(n)):
        for j in range(int(n)):
            temp_state = copy.deepcopy(state)
            if(state[i][j] == '.'):
                if isRaid(i, j, temp_state, player):
                    temp_state[i][j] = player
                    raided_state = calculate_next_raided_state(i,j,temp_state, player)
                    action = str(chr(65 + j)) + str(i+1)
                    temp_node = Node(raided_state, action,"Raid")
                    successors.append(temp_node)
                else:
                    temp_state[i][j] = player
                    action = str(chr(65 + j)) + str(i+1)
                    temp_node = Node(temp_state,action,"Stake")
                    successors.append(temp_node)
                    # staked_state = calculate_next_staked_state(i,j,state)
    return successors

def calculate_next_raided_state(row, col, state, player):
    if player == "X":
        opponent = "O"
    else:
        opponent = "X"
    if check(row, col + 1, state, opponent) == 1:
        state[row][col+1] = player
    if check(row + 1, col, state, opponent) == 1:
        state[row+1][col] = player
    if check(row - 1, col, state, opponent) == 1:
        state[row-1][col] = player
    if check(row, col - 1, state, opponent) == 1:
        state[row][col - 1] = player
    return state

def main():
    file = open("input.txt","r")
    global n
    global globalplayer
    global cutting_depth
    global boardState
    global cell_values

    n = file.readline().strip()
    mode = file.readline().strip()
    globalplayer = file.readline().strip()
    cutting_depth = file.readline().strip()
    cell_values = []

    boardState = []
    cell_valuesRow = []
    boardStateRow = []

    for i in range(int(n)):
        cell_valuesRow = file.readline().split()
        cell_values.append(cell_valuesRow)
    for line in file:
        boardStateRow = []
        for j in line:
            boardStateRow.append(j)
        boardState.append(boardStateRow)

    result_action = minMaxDecision(boardState, globalplayer)

    output = open("output.txt","w")
    output.write(result_action.action + " " + result_action.move_type)
    output.write("\n")
    for i in range(int(n)):
        for j in range(int(n)):
            output.write(result_action.state[i][j])
        output.write("\n")
    output.close()

main()