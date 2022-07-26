from mod.Bar import Bar
from mod.Card import Card


class CombinChecker:

    def __init__(self) -> None:
        self.currentHolding = None
        pass

    def check(self, theBar: Bar, theCard: Card):
        self.currentHolding = theBar.cards
        pass


    # for pong, seong and gong
    def findSequence(self, theCard: Card):
        tempList = self.currentHolding + [theCard]
        returnList = []
        for i in range(len(tempList)):
            if tempList[i].point > 0 and tempList[i+1] and tempList[i+2]:
                returnList.append([tempList[i], tempList[i+1], tempList[i+2]])

    def findPong(self, theCard: Card):
        awaitList = [i for i in self.currentHolding if i.point == theCard.point and i.type == theCard.type]
        if len(awaitList) == 3:
            return awaitList[:3]
        else:
            return None

    def findGong(self, theCard: Card):
        awaitList = [i for i in self.currentHolding if i.point == theCard.point and i.type == theCard.type]
        if len(awaitList) == 4:
            return awaitList[:4]
        else:
            return None

