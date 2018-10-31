import random
from Const import Const
from Move import Move
from Game import Game

class MyAgent2:
    # This agent uses a set depth when analyzing the moves graph
    def __init__(self, side, depth):
        if side != Const.MARK_O and side != Const.MARK_X:
            raise ValueError("side must be MARK_X or MARK_O")
        if depth < 0:
            raise ValueError("Depth must be 0 or greater")
        self.side = side
        self.depth = depth

    def value(self,game,depth):
        ans = None
        state = game.getState()
        if state == Const.STATE_WIN_O:
            if self.side == Const.MARK_O: ans =depth+1
            else: ans = -depth
        elif state == Const.STATE_WIN_X:
            if self.side == Const.MARK_X: ans = depth+1
            else: ans = -depth
        elif state == Const.STATE_DRAW:
                ans = 0

        if ans != None: return (ans,0)

        iside = 0
        if self.side == Const.MARK_O: iside = 1
        else: iside = -1

        iturn = 0
        if state == Const.STATE_TURN_O: iturn = 1
        else: iturn = -1

        myTurn = (iside == iturn)
        myOptions = 0


        for move in game.getMoves():
            move.play(game)
            (moveValue,moveOptions)=self.value(game,depth-1)
            move.unplay(game)
            myOptions = myOptions + 1 + moveOptions 
            if ans== None:
                ans=moveValue
            if myTurn:
                ans = max(ans,moveValue)
            else:
                ans = min(ans,moveValue)

        return (ans,myOptions)

    
    def move(self,game):
        (maxValue,maxOptions)=(0,0)
        if game.isEmptyBoard():
            return Move(random.randint(0,Const.ROWS-1),random.randint(0,Const.COLS-1),self.side)
        
        if self.depth>0:
            (maxValue,maxOptions)=self.value(game,self.depth)
            
        else:
            print("critical error: no maxValue could be calculated")
       
        if(maxValue,maxOptions)==(0,0):
            raise ValueError("level should not be 0 here!")
        
        playable = []
        maxPlayableOption =0
        valueList = []
        for move in game.getMoves():
            move.play(game)
            (moveValue,moveOptions)=self.value(game, self.depth)
            move.unplay(game)
            valueList.append(moveValue)
            #had to subtract 1, if too high sometimes a better move than current state does not exist
            if moveValue>=maxValue:
                playable.append((move,moveOptions))
            maxPlayableOption = max(maxPlayableOption,moveOptions)
        print(valueList)
        bestPlayable=[]
   
      

        for (move, options) in playable:
            if options == maxPlayableOption:
                bestPlayable.append(move)
        
        if len(bestPlayable)>0:
            spot=random.randint(0,len(bestPlayable)-1)
            print("i found a good spot")
            return bestPlayable[spot]
        
        elif len(playable)>0:
            print("i found an alright spot")
            return playable[0][0]
        
        else:
            print("No move will bring me to victory, you win")
            return game.getMoves()[0]
    
    
    def nearbySpot(self, game,side):
        mySpots=[]
        myPlayable=[]
        for row in range(Const.ROWS):
            for col in range(Const.COLS):
                if game._board[row][col]==side:
                    mySpots.append((row,col))
                if game._board[row][col]==Const.MARK_NONE:
                    myPlayable.append((row,col))
        bestSpot=None
        bestScore=0
        for play in myPlayable:
            playscore=0
            for spot in mySpots:
                if play[0]==spot[0]-1 or play[0]==spot[0]+1 and \
                play[1]==spot[1]-1 or play[0]==spot[1]+1:
                    playscore+=1
            if playscore>bestScore:
                bestSpot=play
                bestScore=playscore
        return Move(bestSpot[0],bestSpot[1],side)
              