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

currentPlayer = barList[1]
theDeckDump = DeckDump()
controller.setGameStatus(Controller.INITIATE)
for i in barList:
    for j in range(13):
        i.collectCard(theDeck.pop())

controller.setGameStatus(Controller.RUNNING)

while controller.getGameStatus() != Controller.ENDED and not currentPlayer.is_empty():
    print('Your cards > ', end='')
    currentPlayer.displayCards()
    print(f'Please play a card( 0 - {len(currentPlayer.cards)-1} ): ')
    cardIndex = int(input())
    
    # deck dump collect
    theDeckDump.collect(currentPlayer.playCard(cardIndex))

    # all player check "combination"
    topDeck = theDeckDump.peak()
    currentPlayer.check_combins(topDeck)




for i in barList:
    i.displayCards()

controller.setGameStatus(Controller.ENDED)

if theDeck.is_empty():
    controller.setGameStatus(Controller.ENDED)
