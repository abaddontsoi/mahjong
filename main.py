from mod.Bar import Bar
from mod.Card import Card
from mod.CombSet import CombSet
from mod.Controller import Controller
from mod.Deck import Deck
from mod.DeckDump import DeckDump
from mod.SelfDump import SelfDump
from mod.botBar import BotBar

barList = [
    Bar("p1"),
    BotBar("p2"),
    BotBar("p3"),
    BotBar("p4"),
]

theDeck = Deck()
controller = Controller(barList, theDeck)


currentPlayer = barList[0]
theDeckDump = DeckDump()
controller.setGameStatus(Controller.INITIATE)
for i in barList:
    for j in range(13):
        i.collectCard(theDeck.pop())

controller.setGameStatus(Controller.RUNNING)

while controller.getGameStatus() != Controller.ENDED and not currentPlayer.is_empty():
    # current player draw a card
    currentPlayer.drawCardFromDeck(theDeck)

    # set up a variable for played card
    playedCard = None

    if isinstance(currentPlayer, BotBar):
        playedCard = currentPlayer.autoPlay()
    else:
        print('Your cards > ', end='')
        currentPlayer.displayCards()
        print(f'Please play a card(0 - {len(currentPlayer.cards)-1}): ')
        cardIndex = int(input())
        playedCard = currentPlayer.playCard(cardIndex)
    
    # deck dump collect
    theDeckDump.collect(playedCard)

    # all other player check "combination"
    topDeck = theDeckDump.peak()
    otherBarList = [i for i in barList if i is not currentPlayer]

    # display other players' cards
    for other in otherBarList:
        # print('Others > ', end='')
        # other.displayCards()
        if other.check_combins(topDeck):
            # interrupt sequence for "pong, seong, gong"
            # First, change the current player to 'other'
            # Second, collect the playedd card
            # Third, choose the set of combination that is going to selfDump.
            # Fourth, place the set to self dump
            # Fifth, call the controller to move to next player
            pass

    # change to next player
    currentPlayer = barList[controller.nextPlayer(currentPlayer)]



for i in barList:
    i.displayCards()

controller.setGameStatus(Controller.ENDED)

if theDeck.is_empty():
    controller.setGameStatus(Controller.ENDED)
