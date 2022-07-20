from mod.Bar import Bar
from mod.Card import Card
from mod.CombSet import CombSet
from mod.Controller import Controller
from mod.DeckDump import DeckDump
from mod.SelfDump import SelfDump

barList = [
    Bar("p1"),
    Bar("p2"),
    Bar("p3"),
    Bar("p4"),
]

controller = Controller(barList)


while(controller.getGameStatus() == Controller.RUNNING):

    controller.setGameStatus(Controller.ENDED)
    