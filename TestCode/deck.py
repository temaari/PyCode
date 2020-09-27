from enum import Enum
import random

class Suit(Enum):
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4
    
class Card:
    def __init__(self, value=0, suit=Suit.HEARTS):
        self.value = value
        self.suit = suit
    def printCard(self):
        print (self.value,"of",self.suit.name)

class Deck:
    def __init__(self):
        self.s = Suit.HEARTS
        self.cards = []
        self.v = 1
        for i in range(52):
            if i%13 is 0:
                self.v = 1
            if i > 38:
                self.s = Suit.SPADES
            elif i > 25 and i < 38:
                self.s = Suit.CLUBS
            elif i > 12 and i < 25:
                self.s = Suit.DIAMONDS
            self.cards.append(Card(self.v,self.s))
            self.v += 1
    def cut(self):
        self.num = random.randint(21,36)
        #this will then split the deck into two decks
    def tableWashShuffle(self):
        pass
    def riffleShuffle(self):
        pass
    

d = Deck()
d.cards[51].printCard()
print (Deck.cut(d))
#input()
