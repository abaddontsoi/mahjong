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

        