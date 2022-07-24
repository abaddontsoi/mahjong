from mod.Card import Card
from mod.Deck import Deck


class Bar:
    PONG = 'PONG'
    SEONG = 'SEONG'
    GONG = 'GONG'

    def __init__(self, name = "" ):
        self.name = name
        self.cards = []

    def collectCard(self, theCard):
        if isinstance(theCard, Card):
            self.cards.append(theCard)
            pass

    def createSet(self, theCard: Card, choice: int):
        setList = [self.pong_list(theCard)] + [self.seong_list(theCard)] + [self.seong_list(theCard)]
        pass


    def drawCardFromDeck(self, deck: Deck):
        drawn = deck.pop()
        self.cards.append(drawn)
        print(f'You have drawn a: {drawn}')

    def displayCards(self):
        self.sortCards()
        print(self.cards)

    def sortCards(self):
        for i in range(len(self.cards)):
            for j in range(len(self.cards)-i-1):
                if self.cards[j].cardID > self.cards[j+1].cardID:
                    self.cards[j], self.cards[j+1] = self.cards[j+1], self.cards[j]
            pass
        pass

    def playCard(self, cardIndex: int):
        self.sortCards()
        print(f'{self.name} played a {self.cards[cardIndex]}')
        return self.cards.pop(cardIndex)


    def is_empty(self):
        return len(self.cards) == 0

    def same_type(self, theCard: Card):
        if theCard:
            return [ i for i in self.cards if i.type == theCard.type]
        else:
            return []

    def can_pong(self, theCard: Card):
        awaitList = self.pong_list(theCard)
        return len(awaitList) == 3

    def pong_list(self, theCard: Card):
        awaitList = [i for i in self.same_type(theCard) if i.point == theCard.point]
        awaitList.append(theCard)
        return awaitList

    # find the set that can form a sequence of card including 'theCard'
    def can_seong(self, theCard: Card):
        sameTypeList = self.same_type(theCard)
        lowerList = [ i for i in sameTypeList if i.point == theCard.point - 1]
        higherList = [ i for i in sameTypeList if i.point == theCard.point + 1]
        return lowerList != [] and higherList != []

    def seong_list(self, theCard: Card):
        sameTypeList = self.same_type(theCard)
        lowerList = [ i for i in sameTypeList if i.point == theCard.point - 1]
        higherList = [ i for i in sameTypeList if i.point == theCard.point + 1]
        return lowerList + higherList

    def can_gong(self, theCard: Card):
        awaitList = self.gong_list(theCard)
        return len(awaitList) == 4

    def gong_list(self, theCard: Card):
        awaitList = [i for i in self.same_type(theCard) if i.point == theCard.point]
        awaitList.append(theCard)
        return awaitList
    
    def check_combins(self, theCard = None):
        if theCard:
            if self.can_pong(theCard):
                print(f'pong list: {self.pong_list(theCard)}')

            if self.can_seong(theCard):
                print(f'seong list: {self.seong_list(theCard)}')
            
            if self.can_gong(theCard):
                print(f'gong list: {self.gong_list(theCard)}')        

            return self.can_pong(theCard) or self.can_seong(theCard) or self.can_gong(theCard)
            # may create some "set combinations" using class
            # as the return value, driver code may also be changed
        else:
            return False