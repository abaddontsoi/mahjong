from mod.Bar import Bar
from mod.Deck import Deck

class BotBar(Bar):

    def __init__(self, name=""):
        self.lastPlayedCard = None
        super().__init__(name)

    def drawCardFromDeck(self, deck: Deck):
        drawn = deck.pop()
        self.cards.append(drawn)

    def autoPlay(self):
        self.lastPlayedCard = self.cards.pop()
        print(f'{self.name} played a {self.lastPlayedCard}')
        return self.lastPlayedCard

    def check_combins(self, theCard = None):
        if theCard:
            if self.can_pong(theCard):
                # print(f'pong list: {self.pong_list(theCard)}')
                pass
            if self.can_seong(theCard):
                # print(f'seong list: {self.seong_list(theCard)}')
                pass
            if self.can_gong(theCard):
                # print(f'gong list: {self.gong_list(theCard)}')
                pass
        else:
            pass