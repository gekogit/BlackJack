class Card:
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Hand:
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

def main():
    card1 = Card(rank='A', suit='c')
    card2 = Card(rank='2', suit='c')
    card3 = Card(rank='3', suit='c')
    card4 = Card(rank='4', suit='c')
    card5 = Card(rank='5', suit='c')
    my_hand = Hand()
    print('\nInside Hande:')
    print(my_hand)
    print('\nA few instances of Cards class::')
    print(card1)
    print(card2)
    print(card3)
    print(card4)
    print(card5)
    my_hand.add(card1)
    my_hand.add(card2)
    my_hand.add(card3)
    my_hand.add(card4)
    my_hand.add(card5)
    print('\nHand after adding 5 cards:')
    print(my_hand)


if __name__ == '__main__':
    main()
