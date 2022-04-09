import random


class Card:
    """ Karta do gry. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Hand:
    """ Ręka - karty do gry w ręku gracza. """

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<pusta>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):

    """ Talia kart do gry. """

    def populate(self):

        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))  # !

    def shuffle(self):
        random.shuffle(self.cards)

        def deal(self, hands, per_hand=1):
            pass


def main():
    deck1 = Deck()
    print("Deck:")
    print(deck1)

    deck1.populate()
    print("Populated deck:")
    print(deck1)

    deck1.shuffle()
    print("\nshuffle deck.")
    print(deck1)

if __name__ == '__main__':
    main()
