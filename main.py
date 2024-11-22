import random

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

        valid_moves = game.actions()
        moves = []
        scores = []
        depths = []
        best_move = None
        best_depth = float("inf")
        best_score = float("inf")
        for move in valid_moves.items():
            moves.append(move[1])
            scores.append(game.utility(move[1])[0])
            depths.append(game.utility(move[1])[1])

        print(scores)
        print(depths)
        for i in range(len(moves)):
            if scores[i] <= best_score:
                best_score = scores[i]
                best_move = moves[i]
                best_depth = depths[i]

        for i in range(len(moves)):
            if scores[i] > best_score:
                moves[i] = None
                scores[i] = None
                depths[i] = None

        for i in range(len(moves)):
            if not depths[i]:
                continue
            if depths[i] > best_depth:
                best_depth = depths[i]

        for i in range(len(moves)):
            if not depths[i]:
                continue
            if depths[i] < best_depth:
                moves[i] = None
                scores[i] = None
                depths[i] = None

        moves = [i for i in moves if i]
        scores = [i for i in scores if i]
        depths = [i for i in depths if i]

        best_move = random.choice(moves)

        computers_move = best_move

        print(computers_move)

        game.result(computers_move)

    if game.terminal():
        winner_val = game.utility()[0]

        if winner_val == 1:
            print("X Wins")
        elif winner_val == -1:
            print("O Wins")
        else:
            print("Nobody Wins")

# grid = [
#     [None, None, None],
#     [None, "O", None],
#     ["O", None, None]
# ]
#
# board = Board(grid, parent=None)
#
# game = Game(board)
#
# print(game.terminal())
#
# print(game.utility())
