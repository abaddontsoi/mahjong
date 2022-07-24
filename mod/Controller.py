from mod.Bar import Bar
from mod.Deck import Deck


class Controller:
    INITIATE = 'INITIATE'
    RUNNING = 'RUNNING'
    ENDED = 'ENDED'

    def __init__(self, bars: list, deck: Deck) -> None:
        self.deck = deck
        self.players = bars
        self.gameStat = self.RUNNING

    def setGameStatus(self, stat):
        self.gameStat = stat

    def getGameStatus(self):
        print(
            f'The game is now {self.gameStat}, {self.deck.showSize()} cards left'
            )
        return self.gameStat

    def nextPlayer(self, currentPlayer: Bar):
        currentIndex = self.players.index(currentPlayer)
        if currentIndex == len(self.players) - 1:
            return 0
        else:
            return currentIndex+1