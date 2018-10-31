import random
from Const import Const
from Move import Move
from State import State

"""This agent prioritizes consecutive moves by placing marks on spots that are next spots that already
have marks on them otherwise it defaults to random playable spots"""

class MyAgent:
    def __init__(self):
        pass

    def move(self,state):
        mark = None
        if state.getState() == Const.STATE_TURN_O:
            mark = Const.MARK_O
        if state.getState() == Const.STATE_TURN_X:
            mark = Const.MARK_X
        if mark == None:
            raise ValueError("state must be playable")
        board = state.getBoard()
        playable = []
        for row in range(Const.ROWS):
            for col in range(Const.COLS):
                if board[row][col] == Const.MARK_NONE:
                    
                    # Added checks to see if next move wins (if there is 2 O's in a row already)
                    # TODO: make win moves work
                    if row+2 < Const.ROWS and board[row+1][col] == Const.MARK_O and board[row+2][col] == Const.MARK_O:
                        spot=board[row][col]
                        playable.append([row,col])
                        print("win move1")
                        return Move(playable[spot][0],playable[spot][1],mark)
                    if row-2 >= 0 and board[row-1][col] == Const.MARK_O and board[row-2][col] == Const.MARK_O:
                        spot=board[row][col]
                        playable.append([row,col])
                        print("win move2")
                        return Move(playable[spot][0],playable[spot][1],mark)
                    if col+2 < Const.COLS and board[row][col+1] == Const.MARK_O and board[row][col+2] == Const.MARK_O:
                        spot=board[row][col]
                        playable.append([row,col])
                        print("win move3")
                        return Move(playable[spot][0],playable[spot][1],mark)
                    if col-2 >= 0 and board[row][col-1] == Const.MARK_O and board[row][col-2] == Const.MARK_O:
                        spot=board[row][col]
                        playable.append([row,col])
                        print("win move4")
                        return Move(playable[spot][0],playable[spot][1],mark)
                    if col+2 < Const.COLS and row+2 < Const.ROWS and board[row+1][col+1] == Const.MARK_O and board[row+2][col+2] == Const.MARK_O:
                        spot=board[row][col]
                        playable.append([row,col])
                        print("win move5")
                        return Move(playable[spot][0],playable[spot][1],mark)
                    if col-2 >= 0 and row-2 >= 0 and board[row-1][col-1] == Const.MARK_O and board[row-2][col-2] == Const.MARK_O:
                        spot=board[row][col]
                        playable.append([row,col])
                        print("win move6")
                        return Move(playable[spot][0],playable[spot][1],mark)
                    if col-2 >= 0 and row+2 < Const.ROWS and board[row+1][col-1] == Const.MARK_O and board[row+2][col-2] == Const.MARK_O:
                        spot=board[row][col]
                        playable.append([row,col])
                        print("win move7")
                    if col+2 < Const.COLS and row-2 >= 0 and board[row-1][col+1] == Const.MARK_O and board[row-2][col+2] == Const.MARK_O:
                        spot=board[row][col]
                        playable.append([row,col])
                        print("win move8")

                    # TODO: add if checks to block opponents win




                    # each of these if checks check to see if an O mark is next to a playable spot in all directions adjacent to the playable spot
                    # Compared to random agentO vs random agentX, this agent should result in more wins for agentO (assumming you assign MyAgent to agentO and Random to agentX)
                    if row+1 < Const.ROWS and board[row+1][col] == Const.MARK_O:
                        spot=board[row][col]
                        playable.append([row,col])
                        print("priority move1")
                        return Move(playable[spot][0],playable[spot][1],mark)
                    if row-1 >= 0 and board[row-1][col] == Const.MARK_O:
                        spot=board[row][col]
                        playable.append([row,col])
                        print("priority move2")
                        return Move(playable[spot][0],playable[spot][1],mark)
                    if col+1 < Const.COLS and board[row][col+1] == Const.MARK_O:
                        spot=board[row][col]
                        playable.append([row,col])
                        print("priority move3")
                        return Move(playable[spot][0],playable[spot][1],mark)
                    if col-1 >= 0 and board[row][col-1] == Const.MARK_O:
                        spot=board[row][col]
                        playable.append([row,col])
                        print("priority move4")
                        return Move(playable[spot][0],playable[spot][1],mark)
                    if row+1 < Const.ROWS and col+1 < Const.COLS and board[row+1][col+1] == Const.MARK_O:
                        spot=board[row][col]
                        playable.append([row,col])
                        print("priority move5")
                        return Move(playable[spot][0],playable[spot][1],mark)
                    if row+1 < Const.ROWS and col-1 >= 0 and board[row+1][col-1] == Const.MARK_O:
                        spot=board[row][col]
                        playable.append([row,col])
                        print("priority move6")
                        return Move(playable[spot][0],playable[spot][1],mark)
                    if row-1 >= 0 and col+1 < Const.COLS and board[row-1][col+1] == Const.MARK_O:
                        spot=board[row][col]
                        playable.append([row,col])
                        print("priority move7")
                        return Move(playable[spot][0],playable[spot][1],mark)
                    if row-1 >= 0 and col-1 >= 0 and board[row-1][col-1] == Const.MARK_O:
                        spot=board[row][col]
                        playable.append([row,col])
                        print("priority move8")
                        return Move(playable[spot][0],playable[spot][1],mark)

                    # TODO: add if checks to prioritize edge moves over random moves

                    # TODO: add if checks to prioritize center move over random moves

                    else:
                        #defaults to random move if no consecutive move possibility exists
                        playable.append([row,col])
        spot=random.randint(0,len(playable)-1)
        print("random move")
        return Move(playable[spot][0],playable[spot][1],mark)
