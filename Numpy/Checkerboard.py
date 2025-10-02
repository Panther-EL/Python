import numpy as np
board = np.random.randint(0,11, size=(6,6))
print(f'Board: {board}')

#Extracting checkerboard sets
def extract_board(board):
    set_A = board[0:5:2, 0:5:2] #Extracting even rows and even columns
    print(f'Set A(Black squares): {set_A}')
    even_rows_odd_cols = board[0:5:2, 1:6:2]
    odd_rows_even_cols = board[1:6:2, 0:5:2]
    set_B = even_rows_odd_cols + odd_rows_even_cols #Extracting one index even and the other odd
    print(f'SetB(White squares): {set_B}')
    return set_A,set_B

#Storing results
results = []
results.append(extract_board(board))

#Displaying results
print(results)
 
