from copy import deepcopy

BOARD_SIZE = 25

def backtracking():
    states = [ [] ]
    while states:
        current = states.pop()
        if final_state(current):
            return current
        for succ in succesor(current):
            if not attacking(succ):
                states.append(succ)


''' Returns a list of all possible states where we add a queen on the next row'''
def succesor(state):
    result = []
    for i in reversed(range(BOARD_SIZE)):
        succ = deepcopy(state)
        succ.append(i)
        result.append(succ)
    return result


''' Returns True if any two queens are attacking eachother, False otherwise'''
def attacking(state):
    # vertical is implied by the way we code a state

    # horizontal
    for i in range(len(state)):
        for j in range(len(state)):
            if i != j and state[i] == state[j]:
                return True

    # TODO diagonal
    return False
    
''' If each column has a queen is full '''
def final_state(state):
    if len(state) == BOARD_SIZE:
        return True
    return False


def display(state):
    # pretty print the state
    pass