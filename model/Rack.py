from model.Discard import Discard

class Rack:
    def __init__(self, discard: Discard, cards: list):
        self.discard = discard
        self.cards = cards
        return
    
    def swap(self, card: int, position: int):
        if position >= 0 and position < len(self.cards):
            self.discard.add(self.cards.pop(position))
            self.cards.insert(position, card)
        return
    
    def view(self):
        return self.cards
    
    def __str__(self):
        output = list()
        for x in self.cards:
            output.append(str(x))
        return output