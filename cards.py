#  This is a simple card game. We represent a deck of 52 cards comprising 13 ranks in each of the four suits: Clubs, Diamonds, Hearts, Spades.
#  Each suit includes an Ace, a two, a three, a four, a five, a six, a seven, an eight, a nine, a ten, a Jack, a Queen, and a King. 
# two computer players will compete with each other
# There are five cards in each hand and the player with more Ace cards is the winner. 
# If both players have the same number of Ace cards (tie), the deck is created anew, the deck is shuffled and each player is dealt a new hand.

import random # import random from python3 to the code

# User - defined classes

class Card:

    def __init__(self, rank, suit):
        #  Initialize a card with a given suit and a rank
        #  rank - an integer between 1-13
        #  suit- a string ("Clubs", "Diamonds", "Hearts", "Spades") 

        self.rank = rank
        self.suit = suit

    def get_rank(self):
        #  Return the rank of a card
        return self.rank

    def display(self):
        #   Display a card as a string with the name of the rank and the name of the suit (e.g. 'Jack of Diamonds', 'Three of Clubs')
        print(self.rank + " of " + self.suit) # display card name, be using it in player class too
    

class Deck:

    def __init__(self):
        #  Initialize a deck by generating one of each possible card using the Card class.
        #  The deck should contain one Card object for each of the 4*13=52 different cards.

        self.cards = []
        self.ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        self.suits =  ["Clubs", "Diamonds", "Hearts", "Spades"]
 
        for i in range(len(self.suits)):            
            for j in range(len(self.ranks)):
                self.cards.append(Card(self.ranks[j], self.suits[i])) # adding the 52 cards in self.cards by using for loop
        
    def shuffle(self):
        #  Randomly shuffle the deck of cards
        random.shuffle(self.cards)

    def deal(self):
        #  Return a card from the top of the deck, and remove that card from the deck.
        return self.cards.pop()

    
class Player: 

    def __init__(self):
        # Initialize a player who can keep track of the cards in their hand. Initially, the hand should be empty (no cards in it).        
        self.hand = [] #  adding player the card in player, currently empty
    
    def add(self, card):
        #  Add a card to the player’s hand
        #  card - An instance of the Card class.
        self.hand.append(card)

    def ace_cards(self):
        #  Returns the number of Ace cards in the player’s hand.

        ace_count = 0
        for card in self.hand:
            if card.get_rank() == "Ace":
                ace_count += 1 # count the ace cards in each player hand by using loop and if 
        return ace_count # return ace count

    def display(self):
        #  Display the player’s hand. This method should call the display() method of each card object in the player's hand.
        for card in self.hand:
            card.display()

# User - defined functions

def main():
    # the object in this function will:
    # -Create one deck
    # -Shuffle the deck
    # -Create both players
    # -Populate the player's hands with 5 cards each
    # -Display the player's hands
    # -Display the number of Ace cards in each player’s hand
    # -Display the winner. 
    # -If the game ends in a tie, then restart the game from step a.

    # Assign starting ace count and space to use in main function
    ace1 = 0

    ace2 = 0

    space = ""

    # Start game loop
    while ace1 == ace2:

        # Create deck (include 52 cards)
        deck = Deck() 

        #Shuffle deck of cards
        deck.shuffle()

        #Create 2 players
        p1 = Player() # p1 is player 1
        p2 = Player() # p2 is player 2

        # Add 5 cards in player hand
        for i in range(5):
            p1.add(deck.deal())
            p2.add(deck.deal())

        print("This is the hand of player 1:")
        p1.display() # Displaying p1 cards

        print(space)

        print("This is the hand of player 2:")
        p2.display() # Displaying p2 cards

        ace1 = p1.ace_cards() # assign ace cards count to ace1
        ace2 = p2.ace_cards() # assign ace cards count to ace2

        # For this part below, displaying ace card for both
        print(space)
        print("Number of ace cards in each player's hand:")
        print("Player 1 has ",  str(ace1), " aces") 
        print("Player 2 has ",  str(ace2), " aces")
        print(space)

        # Displaying result of the game
        print("Result:")
        if ace1 == ace2:
            print("No winner, shuffle again")

        elif ace1 > ace2:
            print("Player 1 is the winner")

        else:
            print("Player 2 is the winner")

        print(space)
main()
# End