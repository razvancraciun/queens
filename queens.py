from copy import deepcopy
from tabulate import tabulate
from termcolor import colored

BOARD_SIZE = 8

def backtracking():
    states = [[]]
    while states:
        state = states.pop()
        if is_final(state):
            return state
        for succ in succesors(state):
            if is_valid(succ):
                states.append(succ)

''' Returns a list of all possible states where we add a queen on the next row '''
def succesors(state):
    result = []
    for i in reversed(range(BOARD_SIZE)):
        succ = deepcopy(state)
        succ.append(i)
        result.append(succ)
    return result

''' Returns True if no queens are attacking each other, False otherwise '''
def is_valid(state):
    # horizontal check is implied by the way the state is stored

    # vertical check
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j]:
                return False

    # diagonal check
    # ╲╱ check
    for i in range(len(state)):
        for j in range(i - 1, -1, -1):
            if state[j] in {state[i] - j + i, state[i] + j - i}:
                return False
    # ╱╲ check
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[j] in {state[i] - j + i, state[i] + j - i}:
                return False

    return True
    
''' Returns True if each row has a queen, False otherwise '''
def is_final(state):
    if len(state) == BOARD_SIZE:
        return True
    return False

def display(state):
    result = []
    for i in range(BOARD_SIZE):
        result.append([])
        for j in range(BOARD_SIZE):
            result[i].append('')
    
    for i in range(len(state)):
        result[i][state[i]] = colored('⬤', 'white')

    print(tabulate(result, headers=range(BOARD_SIZE), showindex='always', tablefmt='fancy_grid'))