SUITS = ['♣', '♦', '♥', '♠']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

DECK = []
for suit in SUITS:
    for rank in RANKS:
        DECK.append([suit, rank])