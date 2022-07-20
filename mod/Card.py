class Card:
    MAANZI = "MAANZI"
    TUNGZI = "TUNGZI"
    ZOKZI = "SOKZI"
    DUNG = "DUNG"
    NAAM = "NAAM"
    SAAI = "SAAI"
    BAK = "BAK"
    ZUNG = "ZUNG"
    FAAT = "FAAT"
    BAAK = "BAAK"

    def __init__(self, type, point = 0) -> None:
        self.type = type
        self.point = point