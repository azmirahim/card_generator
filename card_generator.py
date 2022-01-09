# Card Class
from graphics import*
import random

class Card:
    
    """A card is generated using its center point, rank, and suit.
    The getRank() method returns the rank of the card.
    The getSuit() method returns the suit of the card.
    The __str__() method returns a print statement that tells the user
    what type of card was generated.
    The draw() method draws the card that has been generated."""
    
    def __init__(self, win, rank, suit, centerpoint):
        """ Creates a card, eg:
        card = Card(window, "5", "d", Point(150, 150)) """
        
        self.center = centerpoint
        self.win = win

        self.ranklist = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
        self.rankposition = rank
        self.rank = self.ranklist[self.rankposition - 1]
        
        self.suitposition = suit.upper()
        if suit == "d":
            self.suit = "Diamonds"
        elif suit == "c":
            self.suit = "Clubs"
        elif suit == "h":
            self.suit = "Hearts"
        else:
            self.suit = "Spades"

    def getRank(self):
        "Returns the rank of the card."
        return self.rank

    def getSuit(self):
        "Returns the suit of the card."
        return self.suit      

    def __str__(self):
        "Prints out a statement of the rank and suit of the card"
        return "{0} of {1}.".format(self.rank, self.suit)

    def draw(self):
        "Draws the card in the graphics window."
        self.card = Image(self.center, "{0}{1}.png".format(self.rank, self.suitposition))
        self.card.draw(self.win)

# Question 3 and Question 4

def main():
    cards = int(input("Enter how many cards you'd like to generate: "))
    graphics_size = 189 + (cards*122.2)
    win = GraphWin("Cards", graphics_size, 500)
    win.setCoords(0, 0, graphics_size, 500)

    center_point = 160
    for cards in range (0, cards):
        card_suit = random.choice("dchs")
        card_rank = random.randint(1, 13)
        card = Card(win, card_rank, card_suit, Point(center_point, 250))
        print(card)
        card.getRank()
        card.getSuit()
        card.draw()
        center_point += 122.2

main()
