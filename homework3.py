import copy


class Node:
    def __init__(self, state, action, move_type, utility_score):
        self.state = state
        self.action = action
        self.move_type = move_type
        self.utility_score = utility_score


def minMaxDecision(state, player):
    list_of_actions = []
    # v = max_value(state, player, 0)
    if player == "X":
        nextPlayer = "O"
    else:
        nextPlayer = "X"
    Successors = get_successors_of_current_state(state, player)
    for s in Successors:
        list_of_actions.append(minMaxValue(s, nextPlayer, 1))

    # v = list_of_utility_score[0]
    # list = []
    # for node in list_of_utility_score:
    #     list.append(node.utility_score)
    # index = list.index(max(list))
    # v = Successors[index]

    max_value = list_of_actions[0]
    # can store index i so taht  i dont have to find it using list.index() method -- for optimizing
    for i in range(1,list_of_actions.__len__()):
        max_value = max_score(max_value,list_of_actions[i])
    next_action = Successors[list_of_actions.index(max_value)]

    return next_action


def minMaxValue(state_Node, player, depth):
    current_depth = copy.deepcopy(depth)
    current_player = copy.deepcopy(player)
    current_state = copy.deepcopy(state_Node.state)

    if current_player == "X":
        nextPlayer = "O"
    elif current_player == "O":
        nextPlayer = "X"

    if (terminal_test(current_state, current_depth)):
        return utility(state_Node, current_player)
    elif current_player == globalplayer:
        v = Node([[]],'','',-float('inf'))
        Successors = get_successors_of_current_state(current_state, current_player)
        for s in Successors:
            v = max_score(v, minMaxValue(s, nextPlayer, current_depth + 1))
        # print("Max : At depth ", end="")
        # print(depth, end="")
        # print(v.utility_score)
    else:
        v = Node([[]], '', '', float('inf'))
        Successors = get_successors_of_current_state(current_state, current_player)
        for s in Successors:
            v = min_score(v, minMaxValue(s, nextPlayer, current_depth + 1))
        # print("Min : At depth ", end="")
        # print(depth, end="")
        # print(v.utility_score)
    return v


def alpha_beta_search(state, player):

    list_of_actions = []
    Successors = get_successors_of_current_state(state, player)

    if player == "X":
        nextPlayer = "O"
    else:
        nextPlayer = "X"

    state_Node = Node(state,'','',0)
    alpha_Node = Node([[]], '', '', -float('inf'))
    beta_Node = Node([[]], '', '', float('inf'))

    # alpha_Node = min_value(Successors[0],nextPlayer,1,alpha_Node,beta_Node)


    for index in range(0,Successors.__len__()):
        alpha_Node = max_score(alpha_Node, min_value(Successors[index], nextPlayer, 1, alpha_Node, beta_Node))
        list_of_actions.append(alpha_Node)

    # v = max_value(state_Node, player, 0, alpha_Node, beta_Node)
    maximumScoreValue = list_of_actions[0]
    # can store index i so taht  i dont have to find it using list.index() method -- for optimizing
    for i in range(1, list_of_actions.__len__()):
        # print(list_of_actions[i].utility_score)
        maximumScoreValue = max_score(maximumScoreValue, list_of_actions[i])
    next_action = Successors[list_of_actions.index(maximumScoreValue)]

    # nextAction = Node([[]],'','',0)
    # for s in Successors:
    #     if s.utility_score == v.utility_score:
    #         nextAction = s
    return next_action

def max_value(state_Node, player, depth, alpha, beta):
    current_depth = copy.deepcopy(depth)
    current_player = copy.deepcopy(player)
    current_state = copy.deepcopy(state_Node.state)
    local_alpha = copy.deepcopy(alpha)
    local_beta = copy.deepcopy(beta)

    if (terminal_test(current_state, current_depth)):
        return utility(state_Node, current_player)
    # v = -float('inf')
    v = Node([[]], '', '', -float('inf'))
    Successors = get_successors_of_current_state(current_state, current_player)
    if current_player == "X":
        nextPlayer = "O"
    elif current_player == "O":
        nextPlayer = "X"

    for s in Successors:
        local_alpha = max_score(local_alpha, min_value(s,nextPlayer, current_depth+1,  local_alpha, local_beta))
        if max_score(local_alpha,local_beta).state == local_alpha.state:
          return local_beta
        # alpha = max_score(alpha,v)
    # print("Max : At depth ", end="");
    # print(depth, end="")
    # print(v.utility_score)

    return local_alpha

def min_value(state_Node, player, depth, alpha, beta):
    current_depth = copy.deepcopy(depth)
    current_player = copy.deepcopy(player)
    current_state = copy.deepcopy(state_Node.state)
    local_alpha = copy.deepcopy(alpha)
    local_beta = copy.deepcopy(beta)

    if (terminal_test(current_state, current_depth)):
        return utility(state_Node, current_player)

    # v = float('inf')
    v = Node([[]], '', '', float('inf'))
    Successors = get_successors_of_current_state(current_state, current_player)
    if current_player == "X":
        nextPlayer = "O"
    elif current_player == "O":
        nextPlayer = "X"

    for s in Successors:
        local_beta = min_score(local_beta, max_value(s, nextPlayer, current_depth+1, local_alpha, local_beta))
        if min_score(local_beta,local_alpha).state == local_beta.state:
          return local_alpha
        # beta = min_score(beta,v)
    # print("Min : At depth ", end="");
    # print(depth, end="")
    # print(v.utility_score)
    return local_beta

def utility(state_Node,player):
    sumX = 0
    sumO = 0
    utility_score = 0
    curr_state = state_Node.state
    for i in range(int(n)):
        for j in range(int(n)):
            if curr_state[i][j] == "X":
                sumX = sumX + int(cell_values[i][j])
            elif curr_state[i][j] == "O":
                sumO = sumO + int(cell_values[i][j])
    if globalplayer == "X":
        utility_score = sumX - sumO
        state_Node.utility_score = utility_score
    else:
        utility_score = sumO - sumX
        state_Node.utility_score = utility_score

    # print(state_Node.utility_score, end="")
    # print(" is the utility score for state ===> ", end="")
    # print(state_Node.state)

    return state_Node

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
                    if raided_state != 0:
                        temp_node = Node(raided_state, action, "Raid", 0)
                    else:
                        temp_node = Node(temp_state, action, "Stake", 0)

                    successors.append(temp_node)
                else:
                    temp_state[i][j] = player
                    action = str(chr(65 + j)) + str(i+1)
                    temp_node = Node(temp_state,action,"Stake",0)
                    successors.append(temp_node)
                    # staked_state = calculate_next_staked_state(i,j,state)
    return successors

def calculate_next_raided_state(row, col, state, player):
    if player == "X":
        opponent = "O"
    else:
        opponent = "X"
    no_of_conquered_squares = 0
    if check(row, col + 1, state, opponent) == 1:
        state[row][col+1] = player
        no_of_conquered_squares += 1
    if check(row + 1, col, state, opponent) == 1:
        state[row+1][col] = player
        no_of_conquered_squares += 1
    if check(row - 1, col, state, opponent) == 1:
        state[row-1][col] = player
        no_of_conquered_squares += 1
    if check(row, col - 1, state, opponent) == 1:
        state[row][col - 1] = player
        no_of_conquered_squares += 1
    if no_of_conquered_squares > 0:
        return state
    return 0

def max_score(a, b):
    max_value = a
    if b.utility_score > a.utility_score:
        max_value = b
    elif a.utility_score == b.utility_score:
        if a.move_type == b.move_type:
            max_value = a
        elif (a.move_type == "Stake") and (b.move_type == "Raid"):
            max_value = a
        elif (b.move_type == "Stake") and (a.move_type == "Raid"):
            max_value = b
    return max_value

def min_score(a,b):
    min_value = a
    if b.utility_score < a.utility_score:
        min_value = b
    elif a.utility_score == b.utility_score:
        if a.move_type == b.move_type:
            min_value = a
        elif (a.move_type == "Stake") and (b.move_type == "Raid"):
            min_value = a
        elif (b.move_type == "Stake") and (a.move_type == "Raid"):
            min_value = b
    return min_value

def isequal(a, b):
    try:
       return a.upper() == b.upper()
    except AttributeError:
       return a == b

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

    if isequal(mode,"MINIMAX"):
        result_action = minMaxDecision(boardState, globalplayer)
    elif isequal(mode,"ALPHABETA"):
        result_action = alpha_beta_search(boardState, globalplayer)

    output = open("output.txt","w")
    output.write(result_action.action + " " + result_action.move_type)
    output.write("\n")
    for i in range(int(n)):
        for j in range(int(n)):
            output.write(result_action.state[i][j])
        output.write("\n")
    output.close()

main()