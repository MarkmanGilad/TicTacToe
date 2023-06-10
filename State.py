import numpy as np


class State:
    def __init__(self, board = None, player = 1):
        if board is not None:
            self.board = board
        else:
            self.board = self.init_state()
        self.player = 1
        self.end_of_game = 0

    def init_state(self):
        board = np.zeros((3,3))
        return board
    
    def __eq__(self, other) ->bool:
        return np.equal(self.board, other.board).all() and self.player == other.player

    def __hash__(self) -> int:
        return hash(repr(self.board) + repr(self.player))
    
    def copy (self):
        newBoard = np.copy(self.board)
        return State(board=newBoard, player=self.player)