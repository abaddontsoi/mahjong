from mod.Bar import Bar
from mod.Card import Card
from mod.CombSet import CombSet
from mod.Controller import Controller
from mod.Deck import Deck
from mod.DeckDump import DeckDump
from mod.SelfDump import SelfDump

barList = [
    Bar("p1"),
    Bar("p2"),
    Bar("p3"),
    Bar("p4"),
]

controller = Controller(barList)

theDeck = Deck()

controller.setGameStatus(Controller.INITIATE)

while(controller.getGameStatus() != Controller.ENDED):
    
    if controller.getGameStatus() == Controller.INITIATE:
        for i in barList:
            for j in range(13):
                i.collectCard(theDeck.pop())

    for i in barList:
        i.displayCards()


    controller.setGameStatus(Controller.ENDED)

    if theDeck.is_empty():
        controller.setGameStatus(Controller.ENDED)
    