from mod.Card import Card


class Bar:

    def __init__(self, name = "" ):
        self.name = name
        self.cards = []

    def collectCard(self, theCard):
        if isinstance(theCard, Card):
            self.cards.append(theCard)
            pass

    def displayCards(self):
        self.sortCards()
        print(self.cards)
        pass

    def sortCards(self):
        for i in range(len(self.cards)):
            for j in range(len(self.cards)-i-1):
                if self.cards[j].cardID > self.cards[j+1].cardID:
                    self.cards[j], self.cards[j+1] = self.cards[j+1], self.cards[j]
            pass
        pass

    def playCard(self, cardIndex: int):
        return self.cards.pop(cardIndex)


    def is_empty(self):
        return len(self.cards) == 0