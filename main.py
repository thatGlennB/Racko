from view.index import View
from model.index import GameModel


# TODO
#  - create class object to encapsulate commands
#  - add slow crawl effect to text in transitions
#  - alter format to make it more appealing to the eye

def DD(value):
    print(value)
    inpt = input()
    if str(inpt).upper() == "X":
        exit()

view = View()
model = GameModel()

numPlayers = 0

validInput = False
while not validInput:
    control = view.getControls()
    control.setPrompt("add players","how many players are playing?",dict())
    numPlayers = view.refresh()
    if numPlayers.upper() == "Q":
        exit()
    elif not str(numPlayers).isnumeric():
        view.transition("Invalid input: the entry must be a number")
    elif int(numPlayers) <= 0 or int(numPlayers) > 4:
        view.transition("Invalid input: this game can only be played with 1 - 4 players")
    else:
        validInput = True

model.createPlayers(int(numPlayers))

gameEnd = False
i = 0
while not gameEnd:
    rack = model.getRack(i)
    discard = model.getDiscard().all()
    currentPlayer = (i % int(numPlayers)) + 1
    view.transition("Next turn: player "+ str(currentPlayer))
    view.getDisplay().setPlayer(currentPlayer)
    view.getDisplay().setRack(rack)
    view.getDisplay().setDiscard(discard)
    view.getDisplay().updateDiscard()
    
    
    
    if len(discard) > 0:
        message = "You may either pick up the top discard or draw a card from the deck"
        options = {"X": "Pick up discard", "Y": "Draw from deck"}
    else:
        message = "You may draw a card from the deck"
        options = {"Y": "Draw from deck"}
    view.getControls().setPrompt("Select draw card", message, options)
    validInput = False
    while not validInput:
        output = view.refresh()
        drawCard = None
        if output.upper()=="X" and len(discard)>0:
            drawCard = model.draw(False)
            validInput=True
        elif output.upper()=="Y":
            drawCard = model.draw(True)
            validInput=True
        elif output.upper()=="Q":
            exit()
        else:
            validInput=False
            
    view.getControls().setPrompt("Select draw card","The draw card is "+str(drawCard)+".\n To switch it with a card in your rack, enter the relevant index value. To discard the card, press D",{"D": "Discard the draw card"})
    validInput = False
    while not validInput:
        output = view.refresh()
        if output.upper()=="D":
            model.getDiscard().add(drawCard)
            validInput=True
        elif str(output).isnumeric:
            if int(output) > 0 and int(output) <= 10:
                rack.swap(drawCard, int(output) - 1)
                validInput=True
        elif output.upper()=="Q":
            exit()
        else:
            validInput=False
            
            
    j = 1
    isSequential = True
    while(j < len(rack.cards)):
        isSequential = (rack.cards[j] > rack.cards[j - 1]) and isSequential
        j = j + 1
    if isSequential:
        gameEnd = True
        view.transition("Player "+str(currentPlayer)+"has won with the rack ["+",".join(rack.view())+"]")
    
    
    
    view.transition("Player "+str(currentPlayer)+" has won with the rack ["+",".join(rack.__str__())+"]")
    i = i + 1



print("\n\n\nEND")

