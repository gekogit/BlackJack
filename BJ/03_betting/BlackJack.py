import game_cards, games


class BJ_Card(game_cards.Card):

    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v


class BJ_Deck(game_cards.Deck):
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))


class BJ_Hand(game_cards.Hand):
    def __init__(self, name: object) -> object:
        super(BJ_Hand, self).__init__()
        self.name = name
        self.credit = 0
        self.bet = 0

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")" + "\tCredit :" + str(self.credit)
        return rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None

        t = 0
        for card in self.cards:
            t += card.value

        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        if contains_ace and t <= 11:
            t += 10

        return t

    def is_busted(self):
        return self.total > 21


class BJ_Player(BJ_Hand):
    def bet(self) -> object:
        temp = int(input(f'{self.name}, How much you bet? Max({self.credit}):'))
        self.credit = self.credit - temp
        return temp

    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ", do you want the next card? (Y/N): ")
        return response == "y"

    def bust(self):
        print(self.name, "has cart.")
        self.lose()

    def lose(self):
        print(self.name, "loose.")

    def win(self, people, money):
        plot = money/people
        self.credit += plot
        print(self.name, "win ", plot, 'Current credit: ', self.credit)

    def push(self):
        print(self.name, "draw.")


class BJ_Dealer(BJ_Hand):

    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "has cart.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BjGame(object):

    def __init__(self, names):
        self.players = []
        self.pool = 0

        for name in names:
            player = BJ_Player(name)
            wallet = None
            while wallet not in range(0, 1000):
                try:
                    wallet = int(input(f'{name}, how much money do you have in the pocket for game (0-1000):'))
                except Exception:
                    print('Not recognised number. Type again.')
            player.credit = wallet
            self.players.append(player)

        self.dealer = BJ_Dealer('Dealer')
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()


    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting() and player.credit != 0:
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        # 2 cards for each player
        self.deck.deal(self.players + [self.dealer], per_hand=2)

        self.dealer.flip_first_card()  # hide first card
        for player in self.players:
            print(player)
            temp = None
            while temp not in range(0, player.credit):
                try:
                    temp = int(input(f'{player.name}, How much you bet? Max({player.credit}):'))
                except Exception:
                    print('Not recognised number. Type integers')

            player.credit = player.credit - temp
            self.pool += temp

        print(self.dealer)
        print('Pool in round', self.pool)

        # deal additional cards
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()  # show first dealer's card

        if not self.still_playing:
            # all players cart, show dealer hand
            print(self.dealer)
        else:
            # additional cards for dealer
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                # Everyone wins who in game
                for player in self.still_playing:
                    player.win(len(self.still_playing), self.pool)
            else:
                # compare players points to dealer
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win(len(self.still_playing), self.pool)
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        # removed players cards
        for player in self.players:
            player.clear()

        # removed dealer cards
        self.dealer.clear()


def main():

    print("\n\t\t 'Blackjack'!\n")
    names = []
    number = games.ask_number("How many players (1 - 7): ", low=1, high=8)

    for i in range(number):
        name = input("Player name: ")
        names.append(name)
    print()

    game = BjGame(names)

    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nPlay again (Y/N)?: ")


if __name__ == '__main__':
    main()
    input("\n\nPress Enter to exit.")