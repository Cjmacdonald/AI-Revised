from Const import Const
from Move import Move
from Game import Game
from GamePlay import GamePlay
from RandomAgent import RandomAgent
from MyAgent2 import MyAgent2

class MinMaxVsRandomGamePlay(GamePlay):
    def createGame(self): return Game()
    def createAgentO(self): return RandomAgent()
    def createAgentX(self): return MyAgent2(Const.MARK_X,1)

if __name__ == '__main__':
    gameplay = MinMaxVsRandomGamePlay()
    gameplay.play()
