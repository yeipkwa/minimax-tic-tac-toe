from game import Game, Board

grid = [[None for i in range(0, 3)] for j in range(0, 3)]

board = Board(grid, parent=None)

game = Game(board)

while not game.terminal():
    if game.player() == "X":
        valid_moves = game.actions()

        print("Valid moves:")
        for move in valid_moves.items():
            if move[1]:
                print(f"Type {move[0]} to select this move")
                print(move[1])

        player_move = int(input("Please make a move by typing its corresponding number "))

        if not valid_moves[player_move]:
            print("Please make a valid move")
            continue

        game.result(action=valid_moves[player_move])
    else:
        print("Computers turn")
        valid_moves = set(game.actions().values())
        best_value = float("inf")
        best_move = None

        for move in valid_moves:
            current_value = game.max_value(move)
            if current_value < best_value:
                best_value = current_value
                best_move = move
        computers_move = best_move

        print(computers_move)

        game.result(computers_move)

    winner_val = float("inf")
    if game.terminal():
        winner_val = game.utility()

        if winner_val == 1:
            print("X Wins")
        elif winner_val == -1:
            print("O Wins")
        else:
            print("Nobody Wins")




