from itertools import product
from card import Card


class Deck:
    suits = ['H', 'S']
    values = ['1', '2', '3']

    def __init__(self):
        self.cards = []
        self.dealt_cards = []
        self.build()

    def build(self):
        card_list = [self.values, self.suits]

        deck = product(*card_list)
        for pair in deck:
            card = Card("{}{}".format(*pair))
            self.cards.append(card)

    def list(self):
        ret_obj = []
        for c in self.cards:
            ret_obj.append(c.card)
        return ret_obj

    def build_dev(self, deal_type):
        self.cards.clear()

        if deal_type == 1:
            self.cards.append(Card('1H'))
            self.cards.append(Card('2S'))
            self.cards.append(Card('1S'))

            self.cards.append(Card('2H'))
            self.cards.append(Card('3S'))
            self.cards.append(Card('3H'))

        else:
            self.cards.append(Card('2H'))
            self.cards.append(Card('1H'))
            self.cards.append(Card('1S'))

            self.cards.append(Card('3S'))
            self.cards.append(Card('2S'))
            self.cards.append(Card('3H'))


    def is_empty(self):
        return len(self.cards) == 0

    def draw_card(self):
        return self.cards.pop()

    def deal(self, players, num_cards=999):

        players_nb = len(players)

        for i in range(num_cards):

            if self.is_empty():
                break  # break if out of cards

            player = players[i % players_nb]
            player.draw(self)

        for p in players:
            self.dealt_cards.append(p.get_hand())
