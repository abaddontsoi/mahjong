class Card:
    MAANZI = "MAANZI"
    TUNGZI = "TUNGZI"
    SOKZI = "SOKZI"
    DUNG = "DUNG"
    NAAM = "NAAM"
    SAAI = "SAAI"
    BAK = "BAK"
    ZUNG = "ZUNG"
    FAAT = "FAAT"
    BAAK = "BAAK"

    def __init__(self, type, point = 0, cardid = 0):
        self.type = type
        self.point = point
        self.cardID = cardid