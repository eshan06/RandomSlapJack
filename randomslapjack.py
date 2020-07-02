
import random

# Making the different ranks of cards
ranks = ('Two','Three','Four','Five','Six','Seven','Eight',
         'Nine','Ten','Jack','Queen','King', 'Ace')

# Card Class
class Card:
    def __init__(self, rank):
        self.rank = rank
    def __str__(self):
        return "The card is a " + self.rank

# Make the deck Deck Class
class Deck():
    
    # Sets up the deck
    def __init__(self):
        self.deck = []
        for i in ranks:
            for e in range(4): 
                self.deck.append(i)
    
    # Function to shuffle cards using random library
    def shuffle(self):
        random.shuffle(self.deck)
    
    # Function to deal out cards to each player
    def deal(self):
        return self.deck.pop()
        

# Player class
class Player():
    
    # Sets up each players deck
    def __init__(self, name):
        self.name = name
        self.cards = []
    
    def __str__(self):
        return "Name:" + self.name + ' Cards:' + str(len(self.cards))
    
    # Returns one card from the players deck
    def play(self):
        return self.cards.pop(0)
        
    # Adds cards to the players deck if they win the slap jack
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)
        

# Game starting

# Sets up each player
one = Player("One")
two = Player("Two")

# Sets up deck and shuffles it
deck = Deck()
deck.shuffle()

# Deals cards to each player
for i in range(26):
    one.add_cards(deck.deal())
    two.add_cards(deck.deal())

game = True
rounds = 0
# Sets up each players cards that are in play at the moment
onecards = []
twocards = []

while game:
    # Adds A Round
    rounds +=1
    print(f"Round number: {rounds}")
    
    # Adds a card to the list of cards that are currently in play if the person has more than one card in their deck
    if len(one.cards) > 0:
        onecards.append(one.play())
    if len(two.cards) > 0:
        twocards.append(two.play())
        
    # Shows the user the each players cards
    print(f"Player 1 Card: {onecards[-1]}\nPlayer 2 Card: {twocards[-1]}")
    
    # Checks if there is a jack
    if twocards[-1] == 'Jack' or onecards[-1] == 'Jack':
        print('SLAP THE JACK!')
        
        # Random module used to determine who wins the slap jack
        win = random.randint(1, 2)
        if win == 1:
            # Adds the cards from the table to the players hand
            for i in twocards:
                one.add_cards(i)
            twocards.clear()
            print('Player 1 Slapped The Jack first.')
            # Checks if the player has 0 cards to check if they lose
            if len(two.cards) == 0:
                print('Player 1 wins. Player 2 has no more cards and did not slap the Jack.')
                break
        else:
            # Adds the cards from the table to the players hand
            for i in onecards:
                two.add_cards(i)
            onecards.clear()
            print('Player 2 Slapped The Jack first.')
            # Checks if the other player has 0 cards to check if they lose
            if len(one.cards) == 0:
                print('Player 2 wins. Player 1 has no more cards and did not slap the Jack.')
                break