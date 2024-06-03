from model.Deck import Deck
from model.Discard import Discard
from model.Rack import Rack

class GameModel:
    def __init__(self):
        self.players = list()
        self.discard = Discard()
        self.deck = Deck()
        return
    
    def createPlayers(self, numPlayers):
        i = 0
        while i < numPlayers:
            self.players.append(Rack(self.discard, self.deck.drawMany(10)))
            i = i + 1
            
    def getDiscard(self):
        return self.discard
    
    def getRack(self, player) -> Rack:
        if len(self.players) == 0:
            return None
        return self.players[player % len(self.players)]
            
    def draw(self,fromDeck):
        if fromDeck:
            return self.deck.draw()
        else:
            return self.discard.draw()
        
    
    
    
    