class Game:

    def __init__(self, board):
        self.board = board
        self.winner = None

    def player(self, board=None):
        if not board:
            board = self.board
        count = 0
        for row in board.state:
            for col in row:
                if col:
                    count += 1
        if count % 2 == 0:
            return "X"
        return "O"

    def actions(self, board=None):

        if not board:
            board = self.board
        else:
            board = board
        player = self.player(board)
        actions = {}
        action_id = 0

        for row in range(len(board.state)):
            for col in range(len(board.state[row])):
                if board.state[row][col] is None:
                    new_state = [row_i.copy() for row_i in board.state]
                    new_state[row][col] = player
                    actions[action_id] = Board(new_state, board)
                else:
                    actions[action_id] = None
                action_id += 1
        rt = {}
        for action in actions.items():
            if action[1]:
                rt[action[0]] = action[1]

        return rt

    def result(self, action):
        self.board = action

    def terminal(self, board=None):
        state = None
        if not board:
            state = self.board.state
        else:
            state = board.state

        ## Check for empty cells
        rt = True
        for row in state:
            if None in row:
                rt = False

        ## Check for completed row
        for row in state:
            row_completed = True
            value = row[0]
            for col in range(1, len(row)):
                if row[col] != value:
                    row_completed = False
                    break
            if value and row_completed:
                return True

        ## Check for completed column
        for col in range(len(state[0])):
            col_completed = True
            value = state[0][col]
            for row in range(1, len(state)):
                if state[row][col] != value:
                    col_completed = False
                    break
            if value and col_completed:
                return True

        ## Check for completed left diagonal
        diag_completed = True
        value = state[0][0]
        for i in range(1, len(state)):
            if state[i][i] != value:
                diag_completed = False
                break
        if diag_completed and value:
            return True

        ## Check for completed right diagonal
        diag_completed = True
        value = state[len(state) - 1][0]
        for i in range(len(state) - 2, -1, -1):
            if state[i][len(state) - i - 1] != value:
                diag_completed = False
                break
        if diag_completed and value:
            return True

        return rt

    def utility(self, bd=None):
        """ Utility is a function that returns the value of the board if the board is in a terminal state
        """
        winner = None
        if not bd:
            bd = self.board
        state = bd.state

        ## Check for completed row
        if not winner:
            for row in state:
                row_completed = True
                value = row[0]
                for col in range(1, len(row)):
                    if row[col] != value:
                        row_completed = False
                        break
                if value and row_completed:
                    winner = value

        if not winner:
            ## Check for completed column
            for col in range(len(state[0])):
                col_completed = True
                value = state[0][col]
                for row in range(1, len(state)):
                    if state[row][col] != value:
                        col_completed = False
                        break
                if value and col_completed:
                    winner = value

        if not winner:
            ## Check for completed left diagonal
            diag_completed = True
            value = state[0][0]
            for i in range(1, len(state)):
                if state[i][i] != value:
                    diag_completed = False
                    break
            if diag_completed and value:
                winner = value

        if not winner:
            ## Check for completed right diagonal
            diag_completed = True
            value = state[len(state) - 1][0]
            for i in range(len(state) - 2, -1, -1):
                if state[i][len(state) - i - 1] != value:
                    diag_completed = False
                    break
            if diag_completed and value:
                winner = value

        # print(bd)

        if winner == "X":
            return 1
        elif winner == "O":
            # print(bd)
            return -1
        else:
            return 0

    def min_value(self, bd):
        if self.terminal(bd):
            return self.utility(bd)
        v = float("-inf")
        actions = self.actions(bd)
        for action in actions.items():
            v = min(v, self.max_value(action[1]))
        return v

    def max_value(self, bd):
        if self.terminal(bd):
            return self.utility(bd)
        v = float("-inf")
        actions = self.actions(bd)
        for action in actions.items():
            v = max(v, self.min_value(action[1]))
        return v


class Board:

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0

    def __str__(self):
        s = ""

        for row in self.state:
            s += f"{row[0] if row[0] else '':<1}|{row[1] if row[1] else '':<1}|{row[2] if row[2] else '':<1}\n"

        return s

