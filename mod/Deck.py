from .Card import Card

class Deck:
    def __init__(self) -> None:
        self.deck = self.CardGen()

    def CardGen(self):
        shuffled_cards = []
        idcounter = 0

        for i in range(1,10):
            for j in range(4):
                shuffled_cards.append(Card(Card.MAANZI, i, idcounter))
                idcounter += 1

            for j in range(4):
                shuffled_cards.append(Card(Card.TUNGZI, i, idcounter))
                idcounter += 1
            
            for j in range(4):
                shuffled_cards.append(Card(Card.SOKZI, i, idcounter))
                idcounter += 1

        for j in range(4):
            shuffled_cards.append(Card(Card.DUNG, 0, idcounter))
            idcounter += 1

        for j in range(4):
            shuffled_cards.append(Card(Card.NAAM, 0, idcounter))
            idcounter += 1

        for j in range(4):
            shuffled_cards.append(Card(Card.SAAI, 0, idcounter))
            idcounter += 1

        for j in range(4):
            shuffled_cards.append(Card(Card.BAK, 0, idcounter))
            idcounter += 1

        for j in range(4):
            shuffled_cards.append(Card(Card.ZUNG, 0, idcounter))
            idcounter += 1

        for j in range(4):
            shuffled_cards.append(Card(Card.FAAT, 0, idcounter))
            idcounter += 1

        for j in range(4):
            shuffled_cards.append(Card(Card.BAAK, 0, idcounter))
            idcounter += 1
                    
        return shuffled_cards