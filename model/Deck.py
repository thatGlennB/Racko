import random

class Deck:    
    def __init__(self):
        self.cards = list()
        i = 1
        while i <= 60:
            self.cards.append(i)
            i = i + 1
        random.shuffle(self.cards)
        print("deck created")
        return
    
    def draw(self):
        return self.cards.pop(0)
    
    def drawMany(self, numCards):
        i = 0
        output = list()
        while i < numCards:
            output.append(self.draw())
            i = i + 1
        return output