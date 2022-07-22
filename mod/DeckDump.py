from mod.Card import Card


class DeckDump:
    """All cards played from bars goes here first."""

    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def collect(self, theCard: Card):
        theCard.next = self.top
        self.top = theCard
        pass

    def peak(self):
        return self.top

    def pop(self):
        oldTop = self.top
        self.top = self.top.next
        return oldTop