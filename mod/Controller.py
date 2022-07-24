from mod.Bar import Bar


class Controller:
    INITIATE = 'INITIATE'
    RUNNING = 'RUNNING'
    ENDED = 'ENDED'

    def __init__(self, bars: list) -> None:
        self.players = bars
        self.gameStat = self.RUNNING

    def setGameStatus(self, stat):
        self.gameStat = stat

    def getGameStatus(self):
        print(f'The game is now {self.gameStat}')
        return self.gameStat

    def nextPlayer(self, currentPlayer: Bar):
        currentIndex = self.players.index(currentPlayer)
        if currentIndex == len(self.players) - 1:
            return 0
        else:
            return currentIndex+1