# DEPRECATED

# ''' Returns a list of all possible states where we add a queen on the next row '''
# def succesors(state):
#     result = []
#     for i in reversed(range(BOARD_SIZE)):
#         succ = deepcopy(state)
#         succ.append(i)
#         result.append(succ)
#     return result

# def backtracking():
#     states = [[]]
#     while states:
#         state = states.pop()
#         if is_final(state):
#             return state
#         for succ in succesors(state):
#             if is_valid(succ):
#                 states.append(succ)