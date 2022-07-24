class Card:
    MAANZI = "MAAN"
    TUNGZI = "TUNG"
    SOKZI = "SOK"
    DUNG = "DUNG"
    NAAM = "NAAM"
    SAAI = "SAAI"
    BAK = "BAK"
    ZUNG = "ZUNG"
    FAAT = "FAAT"
    BAAKBAAN = "BAAKBAAN"

    def __init__(self, type, point = 0, cardid = 0, next = None):
        self.type = type
        self.point = point
        self.cardID = cardid
        self.next = next

    def __repr__(self) -> str:

        if self.point == 0 : 
            return f'{self.type}'
            # return f'{self.cardID}'
        else:
            return f'{self.point}{self.type}'
            # return f'{self.cardID}'
        # return f'{self.cardID}'