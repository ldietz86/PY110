import random

SUITS = ['♣', '♦', '♥', '♠']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

DECK = []
for suit in SUITS:
    for rank in RANKS:
        DECK.append([suit, rank])

def prompt(message):
    print(f"=> {message}")

def shuffle(deck):
    random.shuffle(deck)

def deal_cards(deck):
    shuffle(deck)

    player_cards = [deck.pop(), deck.pop()]
    dealer_cards = [deck.pop(), deck.pop()]

    return player_cards, dealer_cards