from view.index import View

class Discard:    
    def __init__(self):
        self.cards = list()
        self.view = View().getDisplay()
        return
    
    def add(self, card):
        self.cards.append(card)
        self.view.setDiscard(self.cards)
        return
    
    def peek(self):
        return self.cards[-1]
    
    def draw(self):
        return self.cards.pop()
    
    def all(self):
        return self.cards