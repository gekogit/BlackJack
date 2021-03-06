class Card:
    """ Karta do gry. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Unprintable_Card(Card):

    """ Karta, której ranga i kolor nie są ujawniane przy jej wyświetleniu. """

    def __str__(self):
        return "<secret>"

class Positionable_Card(Card):
    """ Karta, która może być odkryta lub zakryta. """

    def __init__(self, rank, suit, face_up=True):
        super(Positionable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super().__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


def main():
    card1 = Card("A", "c")
    card2 = Unprintable_Card("A", "d")
    card3 = Positionable_Card("A", "h")
    print("Card instance:")
    print(card1)
    print("\nUnprintable_Card instance:")
    print(card2)
    print("\nPositionable_Card instance:")
    print(card3)
    card3.flip()
    print("Fliped Positionable_Card:")
    print(card3)
    card3.flip()
    print("Fliped Positionable_Card:")
    print(card3)

    input("\n\nPress Enter to closed.")


if __name__ == '__main__':
    main()


