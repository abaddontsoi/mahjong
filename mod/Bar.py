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

    def same_type(self, theCard: Card):
        if theCard:
            return [ i for i in self.cards if i.type == theCard.type]
        else:
            return []

    def can_pong(self, theCard: Card):
        awaitList = [i for i in self.same_type(theCard) if i.point == theCard.point]
        print(awaitList)
        return len(awaitList) == 2

    def pong_list(self, theCard: Card):
        awaitList = [i for i in self.same_type(theCard) if i.point == theCard.point]
        awaitList.append(theCard)
        return awaitList

    def can_seong(self, theCard: Card):
        sameTypeList = self.same_type(theCard)
        lowerList = [ i for i in sameTypeList if i.point == theCard.point - 1]
        higherList = [ i for i in sameTypeList if i.point == theCard.point + 1]
        return lowerList is not None and higherList is not None

    def seong_list(self, theCard: Card):
        sameTypeList = self.same_type(theCard)
        lowerList = [ i for i in sameTypeList if i.point == theCard.point - 1]
        higherList = [ i for i in sameTypeList if i.point == theCard.point + 1]
        return lowerList + higherList

    def can_gong(self, theCard: Card):
        awaitList = [i for i in self.same_type(theCard) if i.point == theCard.point]
        print(awaitList)
        return len(awaitList) >= 3

    def gong_list(self, theCard: Card):
        awaitList = [i for i in self.same_type(theCard) if i.point == theCard.point]
        awaitList.append(theCard)
        return awaitList
    
    def check_combins(self, theCard = None):
        if theCard:
            if self.can_pong(theCard):
                print(self.pong_list(theCard))
            if self.can_seong(theCard):
                print(self.seong_list(theCard))
            if self.can_gong(theCard):
                print(self.gong_list(theCard))
        else:
            pass