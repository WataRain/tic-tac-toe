# Tic-tac-toe

def print_board(board):
    for i, val in enumerate(board):
        if i % 3 == 0:
            print()
        if val > 0:
            print("X ", end="")
        elif val < 0:
            print("O ", end="")
        else:
            print(i, end=" ")
    print()
    return

winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
    [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
    [0, 4, 8], [2, 4, 6]             # Diagonal
    ]

while True:
    input("Press enter to begin a game of tic-tac-toe")
    board = [
    0, 0, 0, # A value of 1 would be an X
    0, 0, 0, # While a value of -1 would be a O
    0, 0, 0
    ]
    turn = 0
    end = False
    while True:
        turn += 1
        print_board(board)
        if end:
            break
        while True:
            selection = input(f"[Player {(turn%2)+1}, Turn {turn}] Select an available number: ")
            try:
                selection = int(selection)
                if board[selection] == 0:
                    break
                else:
                    print("That spot is already taken.")
            except:
                continue
        board[selection] = [1, -1][turn%2]
        # Check for win
        for combination in winning_combinations:
            board_slice = [board[tile] for tile in combination]
            if sum(board_slice) == 3:
                print("X wins!")
                end = True
                break
            elif sum(board_slice) == -3:
                print("O wins!")
                end = True
                break
