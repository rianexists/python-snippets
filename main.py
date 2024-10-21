import random


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        self.__cards = list()
        self.create_deck()

    def create_deck(self):
        for suit in DeckOfCards.SUITS:
            for card in DeckOfCards.RANKS:
                self.__cards.append((card,suit))

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        try:

            result = self.__cards[-1]
            self.__cards.pop()
            return result
        except:
            return None

    # don't touch below this line

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"
